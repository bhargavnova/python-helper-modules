from pathlib import Path
import hashlib
import json
import os
import time

def sha256_file(path: Path, chunk=1024 * 1024):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            b = f.read(chunk)
            if not b:
                break
            h.update(b)
    return h.hexdigest()

def snapshot(root: Path, hash_mode: str = "hash"):
    root = Path(root).resolve()
    items = []
    for dirpath, _, filenames in os.walk(root):
        for name in filenames:
            p = Path(dirpath) / name
            try:
                st = p.stat()
            except FileNotFoundError:
                continue
            rel = str(p.relative_to(root))
            rec = {
                "path": rel,
                "size": st.st_size,
                "mtime": int(st.st_mtime),
            }
            if hash_mode == "none":
                rec["sha256"] = None
            elif hash_mode == "fast":
                # hash first 64KB + size
                h = hashlib.sha256()
                h.update(str(st.st_size).encode())
                with open(p, "rb") as f:
                    h.update(f.read(65536))
                rec["sha256"] = h.hexdigest()
            else:
                rec["sha256"] = sha256_file(p)
            items.append(rec)
    snap = {
        "root": str(root),
        "created": int(time.time()),
        "hash_mode": hash_mode,
        "items": sorted(items, key=lambda x: x["path"])
    }
    return snap

def save_snapshot(snap: dict, path: Path):
    Path(path).write_text(json.dumps(snap, indent=2), encoding="utf-8")

def load_snapshot(path: Path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def diff(old: dict, new: dict):
    a = {it["path"]: it for it in old.get("items", [])}
    b = {it["path"]: it for it in new.get("items", [])}
    added = sorted([p for p in b.keys() - a.keys()])
    removed = sorted([p for p in a.keys() - b.keys()])
    changed = []
    for p in sorted(set(a.keys()) & set(b.keys())):
        ai, bi = a[p], b[p]
        if ai.get("size") != bi.get("size") or ai.get("sha256") != bi.get("sha256"):
            changed.append(p)
    return {"added": added, "removed": removed, "changed": changed}