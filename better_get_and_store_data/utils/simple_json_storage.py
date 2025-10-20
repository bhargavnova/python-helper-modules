from pathlib import Path
import json

class SimpleJsonStorage:
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self._data = []
        self._next_id = 1

    def load(self):
        if self.file_path.exists():
            try:
                raw = json.loads(self.file_path.read_text(encoding="utf-8"))
                self._data = raw.get("data", [])
                self._next_id = int(raw.get("meta", {}).get("next_id", 1))
            except Exception:
                # fallback if file is broken
                self._data = []
                self._next_id = 1
        else:
            self._commit()

    def _commit(self):
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        payload = {"data": self._data, "meta": {"next_id": self._next_id}}
        self.file_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def _match(self, row, filters):
        for k, v in filters.items():
            if row.get(k) != v:
                return False
        return True

    # API mirror
    def store_data(self, **kwargs):
        row = dict(kwargs)
        row["id"] = self._next_id
        self._next_id += 1
        self._data.append(row)
        self._commit()
        return row["id"]

    def update_data(self, search_tuple, **kwargs):
        key, val = search_tuple
        updated = False
        for row in self._data:
            if row.get(key) == val:
                for k, v in kwargs.items():
                    row[k] = v
                updated = True
        if updated:
            self._commit()
        return updated

    def read_data(self, **filters):
        return [row for row in self._data if self._match(row, filters)]

    def get_data(self, **filters):
        return self.read_data(**filters)