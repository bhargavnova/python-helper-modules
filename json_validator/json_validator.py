import json
import sys

def validate_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            json.loads(content)
        print(f" The file '{file_path}' is valid JSON.")
        return True
    except json.JSONDecodeError as e:
        print(f" The file '{file_path}' is NOT valid JSON.")
        print(f"Error: {e.msg}")
        print(f"Line: {e.lineno}, Column: {e.colno}")
        return False
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return False
    except Exception as e:
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python json_validator.py <path_to_json_file>")
    else:
        validate_json_file(sys.argv[1])
