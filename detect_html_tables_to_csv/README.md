# HTML Table Scraper

## Introduction

This Python script allows you to extract all tables from a HTML file and export each one of them to a csv. The extraction is done for all the tables in the page and the csv export can be customized for filenames & destination.

## Usage

### Prerequisites

Before using this script, ensure you have the following:

- Python installed on your system.
- Required libraries: `BeautifulSoup`,`csv`,`Path`,`requests`,`datetime`,`argparse`.

### Running the Script

1. Place the PDF file you want to extract images from in the same directory as this script.

2. Replace the `input_file` variable with the name of your PDF file.

```python3 detect_html_tables_to_csv/detect_html_tables_to_csv.py --prefix exp_table```

### Output

The script will generate the csv files in the ```python-helper-modules/detect_html_tables_to_csv/tables/``` directory.

##### License
This script is released under the __MIT License__. Feel free to use, modify, and distribute it as needed.
