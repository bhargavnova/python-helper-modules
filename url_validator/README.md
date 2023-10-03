# URL Validator Library

The `url_validator` library is a Python tool for validating and checking the accessibility of URLs. It provides a simple way to determine whether a given URL is valid and can be accessed via HTTP requests.

## Usage

To use the `url_validator` library, follow these steps:

1. Import the library in your Python script.

```python
import url_validator
```

2. Use the `validate` function to check a URL. The function returns a tuple with two boolean values: `is_valid` and `is_accessible`.

```python
url = "https://www.example.com"
is_valid, is_accessible = url_validator.validate(url)

if is_valid:
    print("The URL is valid.")
    
    if is_accessible:
        print("The URL is accessible.")
    else:
        print("The URL is not accessible.")
else:
    print("The URL is not valid.")
```

Replace `url` with the URL you want to validate.

## Features

The `url_validator` library offers the following features:

- URL Validation: Check the format and structure of a URL to ensure it's properly formed.
- Accessibility Check: Verify if the URL is reachable and returns a valid HTTP response.
- User-Friendly Output: Provides clear feedback on the validity and accessibility of the URL.
- The `url_validator` library relies on the [requests](https://docs.python-requests.org/en/latest/) library for making HTTP requests.