import markdown2

class ConvertMDtoHTML(object):

    def __init__(self, file_path, out_path):
        self.file_path = file_path
        self.out_path = out_path

    def convert_md_to_html(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
            html_content = markdown2.markdown(md_content)

            with open(self.out_path, 'w', encoding='utf-8') as html_file:
                html_file.write(html_content)


if __name__ == "__main__":
    file_name = 'input.md'
    out_path = 'output.html'
    srt_object = ConvertMDtoHTML(file_name, out_path)
    srt_object.convert_md_to_html()
