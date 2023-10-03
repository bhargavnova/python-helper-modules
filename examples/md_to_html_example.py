from md_to_html import md_to_html

if __name__ == "__main__":
    input_file = input("Enter the input Markdown file name (e.g., input.md): ")
    output_file = input("Enter the output HTML file name (e.g., output.html): ")

    md_to_html.convert(input_file, output_file)
