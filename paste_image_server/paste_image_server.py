from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse
from pathlib import Path
import argparse, threading, time, os, json, secrets, hashlib, mimetypes

try:
    from PIL import Image
    from io import BytesIO
    PIL_OK = True
except Exception:
    PIL_OK = False

def now_stamp():
    return time.strftime("%Y%m%d-%H%M%S")

def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def safe_join(base: Path, *parts) -> Path:
    p = (base / Path(*parts)).resolve()
    base = base.resolve()
    if not str(p).startswith(str(base) + os.sep) and p != base:
        raise PermissionError("forbidden")
    return p

class PasteHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.out_dir = kwargs.pop("out_dir")
        self.token = kwargs.pop("token")
        self.convert_format = kwargs.pop("convert_format")
        self.quality = kwargs.pop("quality")
        self.index_file = kwargs.pop("index_file")
        self.dedupe = kwargs.pop("dedupe")
        self.max_size_mb = kwargs.pop("max_size_mb")
        self.static_dir = kwargs.pop("static_dir")
        self.files_route = "/files/"
        super().__init__(*args, **kwargs)

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/":
            return self._serve_index()
        if path.startswith(self.files_route):
            rel = path[len(self.files_route):]
            return self._serve_file(rel)
        if path == "/recent.json":
            return self._serve_recent()
        if path.startswith("/static/"):
            rel = path[len("/static/"):]
            return self._serve_static(rel)
        self.send_error(404, "not found")

    def do_POST(self):
        path = urlparse(self.path).path
        if path == "/upload":
            if self.headers.get("x-token") != self.token:
                self.send_error(403, "bad token")
                return
            return self._handle_upload()
        self.send_error(404, "not found")

    def _serve_index(self):
        idx = self.static_dir / "index.html"
        if not idx.exists():
            self.send_error(500, "index.html missing")
            return
        html = idx.read_text(encoding="utf-8")
        html = html.replace("__TOKEN__", self.token)
        html = html.replace("__OUT_DIR__", str(self.out_dir))
        data = html.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _serve_static(self, rel):
        try:
            p = safe_join(self.static_dir, rel)
        except PermissionError:
            self.send_error(403)
            return
        if not p.exists():
            self.send_error(404)
            return
        ctype = mimetypes.guess_type(str(p))[0] or "application/octet-stream"
        bs = p.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(bs)))
        self.end_headers()
        self.wfile.write(bs)

    def _serve_file(self, rel_path: str):
        try:
            file_path = safe_join(self.out_dir, rel_path)
        except PermissionError:
            self.send_error(403)
            return
        if not file_path.exists():
            self.send_error(404)
            return
        ctype = mimetypes.guess_type(str(file_path))[0] or "application/octet-stream"
        with open(file_path, "rb") as f:
            bs = f.read()
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(bs)))
        self.end_headers()
        self.wfile.write(bs)

    def _serve_recent(self):
        items = []
        if self.index_file.exists():
            try:
                idx = json.loads(self.index_file.read_text(encoding="utf-8"))
                items = idx.get("items", [])[-180:][::-1]
            except Exception:
                items = []
        payload = json.dumps({"ok": True, "items": items}).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def _handle_upload(self):
        ctype = self.headers.get("Content-Type", "")
        if not ctype.startswith("multipart/form-data"):
            return self._json_err("need multipart")
        length = int(self.headers.get("Content-Length", 0))
        if not length or length > self.max_size_mb * 1024 * 1024:
            return self._json_err("payload too large")
        boundary = None
        for part in ctype.split(";"):
            part = part.strip()
            if part.startswith("boundary="):
                boundary = part.split("=", 1)[1].strip().strip('"')
        if not boundary:
            return self._json_err("bad boundary")
        data = self.rfile.read(length)
        b = ("--" + boundary).encode()
        sections = data.split(b)

        index = {"items": []}
        if self.index_file.exists():
            try:
                index = json.loads(self.index_file.read_text(encoding="utf-8"))
            except Exception:
                index = {"items": []}

        prefix = ""
        for sec in sections:
            if b"Content-Disposition" in sec and b'name="prefix"' in sec:
                hb = sec.split(b"\r\n\r\n", 1)
                if len(hb) == 2:
                    body = hb[1].rstrip(b"\r\n--")
                    prefix = body.decode("utf-8", "ignore").strip()[:60]

        saved = []
        for sec in sections:
            if b"Content-Disposition" not in sec or b'name="file"' not in sec:
                continue
            header_body = sec.split(b"\r\n\r\n", 1)
            if len(header_body) != 2:
                continue
            headers_raw, body = header_body
            body = body.rstrip(b"\r\n--")
            hdr = headers_raw.decode("utf-8", "ignore")

            filename = "pasted"
            for token in hdr.split(";"):
                token = token.strip()
                if token.startswith("filename="):
                    fn = token.split("=", 1)[1].strip().strip('"')
                    if fn:
                        filename = Path(fn).name

            mime = "application/octet-stream"
            for line in hdr.split("\r\n"):
                if line.lower().startswith("content-type:"):
                    mime = line.split(":", 1)[1].strip().lower()

            if len(body) > self.max_size_mb * 1024 * 1024:
                continue

            file_hash = sha256_bytes(body)
            if self.dedupe:
                ex = next((it for it in index["items"] if it.get("sha256") == file_hash), None)
                if ex:
                    saved.append(ex)
                    continue

            ts = now_stamp()
            base = prefix if prefix else "pasted"
            ext = {
                "image/png": ".png",
                "image/jpeg": ".jpg",
                "image/webp": ".webp",
                "image/gif": ".gif",
            }.get(mime, Path(filename).suffix or ".png")

            final_bytes = body
            if self.convert_format != "original" and PIL_OK:
                fmt = self.convert_format.upper()
                try:
                    im = Image.open(BytesIO(body))
                    if fmt in ("JPG", "JPEG", "WEBP"):
                        im = im.convert("RGB")
                    buf = BytesIO()
                    save_kwargs = {}
                    if fmt in ("JPG", "JPEG", "WEBP") and self.quality:
                        save_kwargs["quality"] = self.quality
                    im.save(buf, fmt, **save_kwargs)
                    final_bytes = buf.getvalue()
                    ext = "." + ("jpg" if fmt in ("JPG", "JPEG") else fmt.lower())
                except Exception:
                    final_bytes = body

            name = f"{base}-{ts}-{file_hash[:8]}{ext}"
            out_path = safe_join(self.out_dir, name)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            with open(out_path, "wb") as f:
                f.write(final_bytes)

            item = {
                "name": name,
                "url": f"{self.files_route}{name}",
                "bytes": len(final_bytes),
                "sha256": file_hash,
                "ts": ts,
            }
            index["items"].append(item)
            saved.append(item)

        try:
            self.index_file.write_text(json.dumps(index, indent=2), encoding="utf-8")
        except Exception:
            pass

        return self._json_ok({"files": saved})

    def _json_ok(self, obj=None):
        payload = {"ok": True}
        if obj:
            payload.update(obj)
        data = json.dumps(payload).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _json_err(self, msg):
        data = json.dumps({"ok": False, "error": msg}).encode("utf-8")
        self.send_response(400)
        self.send_header("Content-Type", "application/json")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

def run_server(out_dir: Path, port: int, open_browser: bool, convert_format: str, quality: int, dedupe: bool, max_size_mb: int, static_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    static_dir.mkdir(parents=True, exist_ok=True)
    index_file = out_dir / "pasted_index.json"
    token = secrets.token_hex(8)

    def factory(*args, **kwargs):
        return PasteHandler(
            *args,
            out_dir=out_dir,
            token=token,
            convert_format=convert_format,
            quality=quality,
            index_file=index_file,
            dedupe=dedupe,
            max_size_mb=max_size_mb,
            static_dir=static_dir,
            **kwargs
        )

    httpd = HTTPServer(("127.0.0.1", port), factory)
    print(f"[dir] {out_dir}")
    print(f"[url] http://127.0.0.1:{port}/")
    if open_browser:
        try:
            import webbrowser
            webbrowser.open(f"http://127.0.0.1:{port}/")
        except Exception:
            pass
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Paste images into a local page; auto-save to a folder.")
    p.add_argument("-d", "--dir", type=Path, default=Path.cwd() / "pasted_images")
    p.add_argument("-p", "--port", type=int, default=8090)
    p.add_argument("-o", "--open", action="store_true")
    p.add_argument("-f", "--format", choices=["original", "png", "jpg", "webp"], default="original")
    p.add_argument("-q", "--quality", type=int, default=92)
    p.add_argument("--dedupe", action="store_true")
    p.add_argument("--max-size-mb", type=int, default=30)
    p.add_argument("--static", type=Path, default=Path(__file__).parent / "static")
    args = p.parse_args()

    run_server(
        out_dir=args.dir,
        port=args.port,
        open_browser=args.open,
        convert_format=args.format,
        quality=args.quality,
        dedupe=args.dedupe,
        max_size_mb=args.max_size_mb,
        static_dir=args.static,
    )