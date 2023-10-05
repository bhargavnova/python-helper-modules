## image_converter
A Python module that can be used to convert one image format to another.

### Import the module

```python
import image_converter
```

### Convert file format

```python
   Example
@image_converter.convert_image("/path/to/input_image.webp", "/path/to/output_image.png", "png")
```
### For unmatching format name

```one chosen file extension must match the extension mentioned in path to save image, else it will show an error message
   ERROR: chosen file format and saving file path extension do not match.
```