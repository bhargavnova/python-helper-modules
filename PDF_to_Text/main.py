import PyPDF2

def pdf_to_text(pdf_path, text_path):
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            
            text = ''
            
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                text += page.extractText()
            
            with open(text_path, 'w', encoding='utf-8') as text_file:
                text_file.write(text)
            
            print(f'Text extracted successfully and saved to {text_path}')
    
    except Exception as e:
        print(f'Error: {str(e)}')

if __name__ == "__main__":
    pdf_path = input("Enter the path to the PDF file: ")
    text_path = input("Enter the path to save the text file: ")
    
    pdf_to_text(pdf_path, text_path)
