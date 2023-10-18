# File Finder

## Introduction

This python script can find files in the given directory which contain the given keywords. It uses the os and mmap library

## Usage

### Prerequisites

Before using this script, ensure you have the following:

- Python installed on your system.
- Required libraries: `os`, `mmap`.

### Running the Script

- Provide the directory in which you want to search in, then the list of keywords.
- The third paramter decides whether to return a list of files with matching keywords, if no value or 0 is passed. When value 1 is passed, it returns a dictionary, whose key are the keywords and corresponding value is a list of files that contain that keyword. If no match is found, then script returns 0.
- The fourth parameter, when passed boolean value False, performs case insensitive search. Default is True, i.e, by default the search is case sensitive.



```python
thepath = "sample/path/tofiles"
keywords = ["word1","word2"]
def find_files_by_keyword(path, keywords,feature=0,caseSensitive=True)
```
### Output

The script will print a statement displaying the file name, the keyword matched and the path of that file when a keyword is matched in a file. It returns the list or dictionaries according to the parameter provided.


##### License
This script is released under the __MIT License__. Feel free to use, modify, and distribute it as needed.