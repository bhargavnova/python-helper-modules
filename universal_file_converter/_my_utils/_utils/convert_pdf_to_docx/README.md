# PDF to DOCX Converter

A Python script for converting PDF files to DOCX format with image and text extraction.

## Prerequisites

Before using the PDF to DOCX Converter, ensure you have the required libraries installed on your system:

- `PyPDF2` for PDF handling.
- `python-docx` for DOCX generation.
- `pdf2image` for image extraction from PDF.

You can install these libraries using pip:

```bash
pip install PyPDF2 python-docx pdf2image
```

- Additionally, you need to have `poppler-utils` installed, which is required by `pdf2image` for PDF to image conversion.

### Installing poppler-utils
#### Ubuntu or Debian:
```bash
sudo apt-get install -y poppler-utils
```

#### macOS (using Homebrew):
```bash
brew install poppler
```

#### Windows:
Download the pre-built binaries from the [XpdfReader](https://github.com/xpdfreader/xpdf/releases) releases page. Extract the contents and add the bin directory to your system's PATH.

## Example usage of the converter

```python
from convert_pdf_to_docx import PDFtoDOCXConverter

# Initialize the converter with input PDF file and output DOCX file
pdf_converter = PDFtoDOCXConverter("input.pdf", "output.docx")

# Convert the PDF to DOCX
pdf_converter.convert()
```

Don't forget to replace _input.pdf_ with the path to your input PDF file and _output.docx_ with the desired output DOCX file.
