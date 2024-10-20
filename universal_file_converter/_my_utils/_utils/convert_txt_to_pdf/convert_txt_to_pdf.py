from fpdf import FPDF

class TextToPDFConverter:
    def __init__(self, text_filepath, pdf_filepath):
        self.text_filepath = text_filepath
        self.pdf_filepath = pdf_filepath

    def convert_txt_to_pdf(self):
        # Read the text file
        with open(self.text_filepath, 'r') as file:
            text_content = file.read()

        # Create a new PDF document
        pdf = FPDF()
        pdf.add_page()

        # Set the font and font size
        pdf.set_font('Arial', size=12)

        # Write the text content to the PDF
        pdf.multi_cell(0, 10, text_content)

        # Save the PDF to the specified filepath
        pdf.output(self.pdf_filepath)

if __name__ == "__main__":
    # Usage example
    text_filepath = 'input.txt'
    pdf_filepath = 'output.pdf'

    converter = TextToPDFConverter(text_filepath, pdf_filepath)
    converter.convert_txt_to_pdf()