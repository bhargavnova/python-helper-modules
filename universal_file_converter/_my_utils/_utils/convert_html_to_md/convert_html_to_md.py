import html2text

class ConvertHTMLtoMD(object):

    def __init__(self, file_path, out_path):
        self.file_path = file_path
        self.out_path = out_path

    def convert_to_html_md(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
            md_content = html2text.html2text(html_content)

            with open(self.out_path, 'w', encoding='utf-8') as md_file:
                md_file.write(md_content)


if __name__ == "__main__":
    file_name = 'input.md'
    out_path = 'output.html'
    srt_object = ConvertHTMLtoMD(file_name, out_path)
    srt_object.convert_to_html_md()
