# DOCX to PDF Converter

This script converts .docx files to .pdf using the docx2pdf library. It provides a simple class to handle the conversion process, allowing you to specify the input and output file paths.

## Requirements

-   Python 3.x
-   docx2pdf package

You can install the necessary package using:

```bash
pip install docx2pdf
```

## Usage

1. Set the file_name variable to the path of your .docx file.
2. Set the out_path variable to the desired output .pdf file path.

### Example

```python
file_name = "input.docx"
out_path = "output.pdf"
converter = DOCXtoPDFConverter(file_name, out_path)
converter.convert_docx_to_pdf()
```

If no out_path is provided, the PDF will be saved in the same directory as the input .docx file.
