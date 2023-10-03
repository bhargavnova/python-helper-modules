import markdown
import os


def convert(input_file, output_file):
    # Check if the input Markdown file exists
    if not os.path.isfile(input_file):
        print(f"Input file '{input_file}' does not exist.")
        return

    # Read the Markdown content from the input file
    with open(input_file, 'r', encoding='utf-8') as md_file:
        markdown_text = md_file.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(markdown_text)

    # Write the HTML content to the output file
    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

    print(f"Markdown file '{input_file}' has been successfully converted to HTML and saved as '{output_file}'.")
