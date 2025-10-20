from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
from pathlib import Path
import argparse, json, os, webbrowser

def parse_dotenv(path: Path):
    env = {}
    if not path or not Path(path).exists():
        return env
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip()
    return env

def dump_dotenv(path: Path, env: dict):
    lines = [f"{k}={env[k]}" for k in sorted(env)]
    Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8")

class Handler(BaseHTTPRequestHandler):
    def __init__(self, *a, **kw):
        self.base_env_path = kw.pop("base_env_path")
        self.local_env_path = kw.pop("local_env_path")
        super().__init__(*a, **kw)

    def do_GET(self):
        p = urlparse(self.path).path
        if p == "/":
            self._index()
            return
        if p == "/api/env":
            self._api_env()
            return
        self.send_error(404)

    def do_POST(self):
        p = urlparse(self.path).path
        if p == "/api/save":
            self._api_save()
            return
        self.send_error(404)

    def _index(self):
        html = """
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>env manager</title>
<style>
body{font-family:system-ui,-apple-system,Segoe UI,Roboto,Ubuntu;margin:24px;}
table{border-collapse:collapse;width:100%;max-width:900px;}
th,td{border:1px solid #ddd;padding:8px;font-size:14px;}
th{background:#f5f5f5;text-align:left;}
.controls{margin:12px 0;display:flex;gap:8px;flex-wrap:wrap}
input[type=text]{padding:6px 8px;border:1px solid #ccc;border-radius:6px;width:100%;}
button{padding:8px 12px;border:0;border-radius:6px;cursor:pointer;}
.small{font-size:12px;color:#666;margin-top:8px}
</style>
</head>
<body>
<h1>env manager</h1>
<div class="controls">
  <button id="addRow">add</button>
  <button id="saveBtn">save</button>
</div>
<table id="tbl">
  <thead><tr><th>key</th><th>value</th><th></th></tr></thead>
  <tbody></tbody>
</table>
<div class="small" id="meta"></div>
<script>
const tbl = document.getElementById("tbl").querySelector("tbody");
const meta = document.getElementById("meta");

function row(k, v){
  const tr = document.createElement("tr");
  tr.innerHTML = `
    <td><input type="text" value="${k || ""}" data-k></td>
    <td><input type="text" value="${v || ""}" data-v></td>
    <td><button data-del>remove</button></td>
  `;
  tr.querySelector("[data-del]").onclick = () => tr.remove();
  return tr;
}

async function loadEnv(){
  const r = await fetch("/api/env");
  const j = await r.json();
  meta.textContent = ".env: " + j.base_path + "    .env.local: " + j.local_path;
  tbl.innerHTML = "";
  for (const [k,v] of Object.entries(j.effective)){
    tbl.appendChild(row(k, v));
  }
}

async function saveEnv(){
  const data = {};
  for (const tr of tbl.querySelectorAll("tr")){
    const k = tr.querySelector("[data-k]").value.trim();
    const v = tr.querySelector("[data-v]").value;
    if (k) data[k] = v;
  }
  const r = await fetch("/api/save", {method:"POST", headers:{"content-type":"application/json"}, body: JSON.stringify({data})});
  const j = await r.json();
  if (!j.ok) alert("save failed");
}

document.getElementById("addRow").onclick = () => tbl.appendChild(row("", ""));
document.getElementById("saveBtn").onclick = saveEnv;

loadEnv();
</script>
</body>
</html>
""".lstrip()
        b = html.encode("utf-8")
        self.send_response(200)
        self.send_header("content-type", "text/html; charset=utf-8")
        self.send_header("content-length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def _api_env(self):
        base = parse_dotenv(self.base_env_path) if self.base_env_path else {}
        local = parse_dotenv(self.local_env_path) if self.local_env_path else {}
        effective = dict(base)
        effective.update(local)
        payload = {
            "ok": True,
            "base_path": str(self.base_env_path) if self.base_env_path else "",
            "local_path": str(self.local_env_path) if self.local_env_path else "",
            "effective": effective
        }
        b = json.dumps(payload).encode("utf-8")
        self.send_response(200)
        self.send_header("content-type", "application/json")
        self.send_header("content-length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def _api_save(self):
        try:
            length = int(self.headers.get("content-length", "0"))
            body = self.rfile.read(length)
            data = json.loads(body.decode("utf-8"))
            env = data.get("data", {})
            if not self.local_env_path:
                self.send_error(400)
                return
            dump_dotenv(self.local_env_path, env)
            b = json.dumps({"ok": True}).encode("utf-8")
            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.send_header("content-length", str(len(b)))
            self.end_headers()
            self.wfile.write(b)
        except Exception as e:
            b = json.dumps({"ok": False, "error": str(e)}).encode("utf-8")
            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.send_header("content-length", str(len(b)))
            self.end_headers()
            self.wfile.write(b)

def serve(base_env: Path | None, local_env: Path | None, port: int, open_browser: bool):
    def factory(*a, **kw):
        return Handler(*a, base_env_path=base_env, local_env_path=local_env, **kw)
    httpd = HTTPServer(("127.0.0.1", port), factory)
    url = f"http://127.0.0.1:{port}/"
    print(url)
    if open_browser:
        try:
            webbrowser.open(url)
        except Exception:
            pass
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()

def main():
    ap = argparse.ArgumentParser(description="simple local env manager")
    ap.add_argument("--env", type=Path, default=Path.cwd() / ".env")
    ap.add_argument("--local", type=Path, default=Path.cwd() / ".env.local")
    ap.add_argument("--port", type=int, default=8787)
    ap.add_argument("-o", "--open", action="store_true")
    args = ap.parse_args()
    serve(args.env, args.local, args.port, args.open)

if __name__ == "__main__":
    main()