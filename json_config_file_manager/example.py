from json_config_file_manager import JSONConfigManager

# Create JSONConfigManager instance and specify your configuration
# json file (e.g., "configs.json", "keys.json" etc.)
config = JSONConfigManager("configs.json")

# Set configuration values
config.set("username", "myuser")
config.set("api_key", "myapikey")

# Get configuration values
username = config.get("username")
api_key = config.get("api_key")

print(f"Username: {username}, API Key: {api_key}")

# Update configuration values
config.set("api_key", "newapikey")
new_api_key = config.get("api_key")
print(f"Updated API Key: {new_api_key}")

# Delete a configuration value
config.delete("api_key")

# Check if the deleted value is still accessible
deleted_api_key = config.get("api_key")
if deleted_api_key is None:
    print("API Key deleted successfully!")
else:
    print("API Key still exists!")
