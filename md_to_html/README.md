# URL Validator Library

The `md_to_html` library is a Python tool for validating and checking the accessibility of URLs. It provides a simple
way to determine whether a given URL is valid and can be accessed via HTTP requests.

## Usage

To use the `md_to_html` library, follow these steps:

1. Import the library in your Python script.

```python
import md_to_html
```

2. Use the `convert` function to convert a markdown file to html.

```python
import md_to_html

if __name__ == "__main__":
    input_file = input("Enter the input Markdown file name (e.g., input.md): ")
    output_file = input("Enter the output HTML file name (e.g., output.html): ")

    md_to_html.convert(input_file, output_file)

```

## Notes

- The `md_to_html` library relies on the [markdown](https://pypi.org/project/Markdown/) library convert md to html
  files.