import json

class JSONConfigManager:
    def __init__(self, config_file):
        self.config_file = config_file
        self.data = {}
        self.load_config()

    def load_config(self):
        try:
            with open(self.config_file, 'r') as file:
                self.data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # Handle errors if the file doesn't exist or is invalid JSON
            self.data = {}

    def save_config(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.data, file, indent=4)

    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.data[key] = value
        self.save_config()

    def delete(self, key):
        if key in self.data:
            del self.data[key]
            self.save_config()
