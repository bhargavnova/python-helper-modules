from pathlib import Path
import json
import sys

class OnceFile:
    def __init__(self, path: Path | str = None):
        self.path = Path(path) if path else Path.cwd() / ".oncefile.json"
        self.data = {}
        self._loaded = False

    def load(self):
        if self._loaded:
            return
        if self.path.exists():
            try:
                self.data = json.loads(self.path.read_text(encoding="utf-8"))
            except Exception:
                self.data = {}
        else:
            self.data = {}
        self._loaded = True

    def save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.data, indent=2, ensure_ascii=False), encoding="utf-8")

    def get(self, key: str, prompt: str | None = None, default=None, cast=None):
        self.load()
        if key in self.data:
            return self.data[key]
        if prompt is None:
            return default
        try:
            inp = input(f"{prompt} " + (f"[{default}] " if default is not None else ""))
        except EOFError:
            inp = ""
        if not inp and default is not None:
            val = default
        else:
            val = inp
        if cast:
            try:
                val = cast(val)
            except Exception:
                pass
        self.data[key] = val
        self.save()
        return val

    def set(self, key: str, value):
        self.load()
        self.data[key] = value
        self.save()

    def delete(self, key: str):
        self.load()
        if key in self.data:
            del self.data[key]
            self.save()

    def as_dict(self):
        self.load()
        return dict(self.data)