# JSON Config File Manager

The JSON Config File Manager is a Python module that simplifies the management of configuration settings in various Python scripts. It allows you to read and write configuration settings to a JSON file, making it easy to maintain and reuse configurations without rewriting code each time.

## Features

- Load and save configuration settings to a JSON file.
- Easily get, set, and delete configuration values.
- Suitable for small to medium-sized projects.
- Helps in keeping your code clean and maintainable.

## Installation

To use this module in your Python project, follow these simple steps:

1. Clone the repository or download the `json_config_file_manager.py` file.

2. Place `json_config_file_manager.py` in the same directory as your Python script.

3. Import the `JSONConfigManager` class into your Python script.

```python
from json_config_file_manager import JSONConfigManager
```

## Usage

Here's how you can use the Configuration Manager in your script:

```python
# Create a Configuration Manager instance
config_manager = JSONConfigManager("config.json")

# Set configuration values
config_manager.set("key", "value")

# Get configuration values
value = config_manager.get("key")

# Delete a configuration value
config_manager.delete("key")
```

Make sure to customize the config.json filename according to your project's needs.

To explore detailed and practical usage of the **JSON Config File Manager** module, please refer to the `example.py` file within this directory.
