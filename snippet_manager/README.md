# Code Snippet Manager

## Objective

The `code_snippet_manager` module allows users to efficiently manage and store code snippets using Python. It provides basic CRUD (Create, Read, Update, Delete) operations, enabling users to add, view, edit, and delete code snippets as needed.

## Features

- **Create:** Add new code snippets with specified titles, descriptions, and code content.
- **Read:** View all currently stored code snippets with their details.
- **Update:** Modify the title, description, or code content of an existing code snippet.
- **Delete:** Remove a specific code snippet based on its ID.

## Example Usage

```python
import code_snippet_manager

# Add a new code snippet
code_snippet_manager.add_snippet("Hello", "Hello World code", "print('Hello World')")

# List all code snippets
code_snippet_manager.list_snippets()

# Edit a code snippet
code_snippet_manager.edit_snippet(1, 'Bye', 'Bye World code', 'print("Bye World")')

# Delete a code snippet
code_snippet_manager.delete_snippet(1)
```

## Installation

To install the required dependencies, you can use `pip` and the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```
