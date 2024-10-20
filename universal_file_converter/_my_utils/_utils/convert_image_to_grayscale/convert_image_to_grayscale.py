from PIL import Image


class ImageToGrayscaleConverter(object):
    def __init__(self, file_path, out_path):
        """
        Initialize the ImageToGrayscaleConverter with input and output file paths.

        :param file_path: Path to the input image file.
        :param out_path: Path to save the output grayscale image file.
        """
        self.file_path = file_path
        self.out_path = out_path

    def convert_image_to_grayscale(self):
        """
        Convert the image to grayscale.

        This method reads the image file specified in the file_path, converts
        it to grayscale, and saves it at the out_path location.
        """
        try:
            # Open the image file
            image = Image.open(self.file_path)
            # Convert the image to grayscale
            grayscale_image = image.convert("L")
            # Save the grayscale image
            grayscale_image.save(self.out_path)

            print(f"Successfully converted {self.file_path} to grayscale and saved at {self.out_path}.")
        except Exception as e:
            print(f"Error converting file: {e}")


if __name__ == "__main__":
    file_name = "input.jpg"
    out_path = "output.jpg"
    converter = ImageToGrayscaleConverter(file_name, out_path)
    converter.convert_image_to_grayscale()
