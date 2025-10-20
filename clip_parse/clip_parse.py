import re
import json
import sys
from dataclasses import dataclass

try:
    import pyperclip
    HAS_CLIP = True
except Exception:
    HAS_CLIP = False

URL_RE = re.compile(r'\bhttps?://[^\s)>\]]+', re.IGNORECASE)
EMAIL_RE = re.compile(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', re.IGNORECASE)
IPV4_RE = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
HEX_TOKEN_RE = re.compile(r'\b[a-f0-9]{32,}\b', re.IGNORECASE)
CODE_FENCE_RE = re.compile(r'```(\w+)?\n([\s\S]*?)```', re.MULTILINE)

def read_text(source: str | None):
    if source:
        return source
    if HAS_CLIP:
        try:
            return pyperclip.paste() or ""
        except Exception:
            pass
    return sys.stdin.read()

def parse_curl(txt: str):
    if not txt.strip().startswith("curl"):
        return None
    parts = re.findall(r"""'[^']*'|"[^"]*"|\S+""", txt)
    method = "GET"
    url = ""
    data = None
    headers = {}
    i = 0
    while i < len(parts):
        tok = parts[i].strip()
        val = tok.strip("'").strip('"')
        if val == "curl":
            i += 1
            continue
        if val.startswith("http"):
            url = val
            i += 1
            continue
        if val in ("-X", "--request") and i + 1 < len(parts):
            method = parts[i+1].strip("'").strip('"').upper()
            i += 2
            continue
        if val in ("-H", "--header") and i + 1 < len(parts):
            hv = parts[i+1].strip("'").strip('"')
            if ":" in hv:
                k, v = hv.split(":", 1)
                headers[k.strip()] = v.strip()
            i += 2
            continue
        if val in ("-d", "--data", "--data-raw") and i + 1 < len(parts):
            data = parts[i+1].strip("'").strip('"')
            method = "POST" if method == "GET" else method
            i += 2
            continue
        i += 1
    return {"type": "curl", "method": method, "url": url, "headers": headers, "data": data}

def parse(text: str):
    out = {
        "length": len(text),
        "lines": text.count("\n") + 1 if text else 0,
        "urls": URL_RE.findall(text),
        "emails": EMAIL_RE.findall(text),
        "ipv4": IPV4_RE.findall(text),
        "hex_tokens": HEX_TOKEN_RE.findall(text),
        "code_blocks": [],
        "curl": None
    }
    for m in CODE_FENCE_RE.finditer(text):
        lang = m.group(1) or ""
        body = m.group(2) or ""
        out["code_blocks"].append({"lang": lang, "text": body})
    if "curl" in text:
        curl = parse_curl(text.strip())
        if curl and curl.get("url"):
            out["curl"] = curl
            if curl["url"] and curl["url"] not in out["urls"]:
                out["urls"].append(curl["url"])
    out["urls"] = sorted(dict.fromkeys(out["urls"]))
    out["emails"] = sorted(dict.fromkeys(out["emails"]))
    out["ipv4"] = sorted(dict.fromkeys(out["ipv4"]))
    out["hex_tokens"] = sorted(dict.fromkeys(out["hex_tokens"]))
    return out

def main():
    import argparse
    ap = argparse.ArgumentParser(description="parse clipboard or text for useful bits")
    ap.add_argument("--text", help="explicit text (otherwise reads clipboard or stdin)")
    ap.add_argument("--json", action="store_true", help="print json")
    args = ap.parse_args()
    txt = read_text(args.text) or ""
    info = parse(txt)
    if args.json:
        print(json.dumps(info, indent=2, ensure_ascii=False))
    else:
        print(f"length: {info['length']}, lines: {info['lines']}")
        if info["urls"]:
            print("urls:")
            for u in info["urls"]: print(f"  - {u}")
        if info["emails"]:
            print("emails:")
            for e in info["emails"]: print(f"  - {e}")
        if info["ipv4"]:
            print("ipv4:")
            for i in info["ipv4"]: print(f"  - {i}")
        if info["hex_tokens"]:
            print("hex tokens:")
            for t in info["hex_tokens"]: print(f"  - {t}")
        if info["curl"]:
            c = info["curl"]
            print("curl:")
            print(f"  method: {c['method']}")
            print(f"  url: {c['url']}")
            if c["headers"]:
                print("  headers:")
                for k, v in c["headers"].items():
                    print(f"    {k}: {v}")
            if c["data"] is not None:
                print(f"  data: {c['data']}")
        if info["code_blocks"]:
            print("code blocks:")
            for i, cb in enumerate(info["code_blocks"], 1):
                lang = f" ({cb['lang']})" if cb["lang"] else ""
                preview = cb["text"].splitlines()[0] if cb["text"] else ""
                print(f"  [{i}]{lang} {preview[:80]}")

if __name__ == "__main__":
    main()