import PyPDF2

class PDFtoTextConverter:
    def __init__(self, input_filepath, output_filepath):
        self.input_filepath = input_filepath
        self.output_filepath = output_filepath

    def convert_pdf_to_txt(self):
        try:
            with open(self.input_filepath, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                text = ""
                for page_num in range(pdf_reader.getNumPages()):
                    page = pdf_reader.getPage(page_num)
                    text += page.extractText()

            with open(self.output_filepath, 'w', encoding='utf-8') as text_file:
                text_file.write(text)

            print("Conversion successful. Text saved to", self.output_filepath)
        except Exception as e:
            print("An error occurred:", str(e))

# Usage
if __name__ == "__main__":
    input_filepath = "input.pdf"
    output_filepath = "output.txt"
    pdf_to_text_converter = PDFtoTextConverter(input_filepath, output_filepath)
    pdf_to_text_converter.convert_pdf_to_txt()
