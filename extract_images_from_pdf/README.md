# PDF Image Extractor

## Introduction

This Python script allows you to extract images from a PDF file and save them to a specified directory. It utilizes the PyMuPDF library to process PDF files and the Pillow library to handle image manipulation.

## Usage

### Prerequisites

Before using this script, ensure you have the following:

- Python installed on your system.
- Required libraries: `os`, `fitz`, `io`, `PIL`.

### Running the Script

1. Place the PDF file you want to extract images from in the same directory as this script.

2. Replace the `input_file` variable with the name of your PDF file.

```python
input_file = 'sample-pdf-with-images.pdf'
python pdf_image_extractor.py
```
### Output

The script will create a directory named **IMAGES_FROM_PDF** in the same location as the script. Within this directory, a subdirectory will be created for each PDF file processed, named after the PDF file (excluding the extension).

Inside each subdirectory, the script will save the extracted images. Each image will be named with the following convention: **pdf_file_name_page_number_image_number.extension.**

#### Example:
For example, if you run the script with a PDF file named sample-pdf-with-images.pdf, it will create the following structure:

```
IMAGES_FROM_PDF/
    sample-pdf-with-images/
        sample-pdf-with-images_001_001.jpg
        sample-pdf-with-images_002_001.jpg
        ...
```

##### License
This script is released under the __MIT License__. Feel free to use, modify, and distribute it as needed.
