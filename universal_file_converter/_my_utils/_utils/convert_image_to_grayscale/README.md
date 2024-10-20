# Image to Grayscale Converter

This is a Python script that converts any image file (e.g., JPEG, PNG) to grayscale. It uses the `Pillow` library to handle image processing.

## Features

-   Converts images to grayscale.
-   Supports various image formats (JPEG, PNG, BMP, etc.).
-   Easy to use with simple input and output paths.

## Requirements

Make sure you have the following installed:

-   Python 3.x
-   `Pillow` library for image processing

### Install the `Pillow` library

Before running the script, install the required library by executing the following command:

```bash
pip install Pillow
```

## Usage

1. Place your image in the same directory as the script (or specify the full path to your image).
2. Update the file_name and out_path variables in the script with the input image path and desired output image path.

    Example

    ```python
    file_name = "input_image.jpg"    # Path to the input image
    out_path = "output_image.jpg"    # Path to save the grayscale image
    ```

3. Run the script:

    ```bash
    python image_to_grayscale.py
    ```

    Output

    ```bash
    The script will save the grayscale version of your image at the specified output path.
    ```

## Author

-   [NayLin](https://github.com/naylin-dev)
