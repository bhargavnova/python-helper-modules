# Wikipedia Search

## Description
The `wikipedia_search` project provides a Python script for searching Wikipedia articles and generating URLs for the search results. It includes error handling for cases where no search results are found or the search process fails.

## Installation
1. Clone this repository to your local machine.
2. Ensure you have Python 3.12 installed.

## Usage
To use the `wikipedia_search` script, follow these steps:

1. Import the `wikipedia_search` function from the script.
2. Call the function with your search query and an optional language parameter.
3. The wikipedia_search function will return a dictionary containing Wikipedia article titles as keys and their corresponding URLs as values.

## Examples
Here's an example of how to use the wikipedia_search script:

```python
from wikipedia_search import wikipedia_search

query = "Python (programming language)"
language = "en"

results = wikipedia_search(query, language)
print(results)
```

## Running Tests
We have included a set of tests in the tests folder. To run these tests using pytest, follow these steps:

1. Make sure you have pytest installed. If not, you can install it using pip:
```shell
pip install pytest
```
2. Navigate to the project's root directory in your terminal.
3. Run the following command to execute the tests:

```shell
pytest .\tests\tests_wikipedia_search.py
```
This will run the test suite and provide feedback on the functionality and correctness of the wikipedia_search script.

<br/>

## Contributing Guidelines 🤝
We welcome contributions from the open-source community. If you'd like to contribute to this project, please follow our Contribution Guidelines:

To contribute, follow these steps:

1. Fork this repository.
2. Create a new folder with the name of your module.
3. Inside this folder, include your Python helper module with **appropriate documentation including README.md file**.
4. Create a Pull Request with a clear description of your contribution.
### Important New Update
1. The folder name must be the same as the script name inside the folder. (`lower letter`, with `_` separation instead of space.)
2. there should be only a single script, you can include code for the standalone script in the `if __name__ = "__main__":` block.
3. The folder must contain `README.md` file and a `requirements.txt` file if needed.
Refer `extract_images_from_pdf` in the repo, for a better understanding!! :)
> Remember, no contribution is too small! Every line of code makes a difference. Let's build something amazing together! Happy coding!!

### Example Module 📦

**Description**: Briefly describe what this module does.

**Usage**:

```python
# Example code demonstrating how to use the module

# Import the module
import module_name

# Call a function from the module
module_name.function_name(argument)
```
<br/>

## License
This project is licensed under the MIT License.