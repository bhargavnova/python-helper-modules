# JSON File Validator
--- 
A simple Python script to validate JSON files and report syntax errors with line numbers.

## Introduction
---  
This python script helps to quickly check if a JSON file is valid. If the file is invalid, it shows the exact line and column where the error occurs, making debugging easier.

## Features
---
- Validates JSON syntax.
- Reports exact line and column of errors.
- Handles file not found and other exceptions gracefully.


## Usage
---
### Prerequisites

Before using this script, ensure you have the following:
- Python 3.x installed on the system.

### Running the Script

1. Save the script as `json_validator.py`.
2. Open a terminal and navigate to the directory where the script is saved.
3. Run the script with the path to the JSON file:

   ```bash
   python json_validator.py path/to/file.json
   ```
   
### Output
The script will print a statment displaying whether the File, inputed by user is a valid JSON or not.    
In case the File is an invalid JSON file, the script will help in debugging by mentioning the that File is an invalid JSON with the line and probable suggestion to help fix the issue.   

### License
This script is released under the **MIT License**. Feel free to use, modify, and distribute it as needed.
