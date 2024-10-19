from docx2pdf import convert


class DOCXtoPDFConverter(object):
    def __init__(self, file_path, out_path):
        """
        Initialize the DOCXtoPDFConverter with input and output file paths.

        :param file_path: Path to the input DOCX file.
        :param out_path: Path to save the output PDF file.
        """
        self.file_path = file_path
        self.out_path = out_path

    def convert_docx_to_pdf(self):
        """
        Convert the DOCX file to PDF format.

        This method uses the docx2pdf library to convert the DOCX file specified
        in the file_path to a PDF file. If out_path is specified, the PDF is saved
        to that location. Otherwise, it is saved in the same location as the input file.
        """
        try:
            # Perform the conversion using docx2pdf
            if self.out_path:
                convert(self.file_path, self.out_path)
            else:
                convert(self.file_path)
            print(f"Successfully converted {self.file_path} to PDF.")
        except Exception as e:
            print(f"Error converting file: {e}")


if __name__ == "__main__":
    file_name = "input.docx"
    out_path = "output.pdf"
    srt_object = DOCXtoPDFConverter(file_name, out_path)
    srt_object.convert_docx_to_pdf()
