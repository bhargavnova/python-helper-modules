# CSV CRUD Manage

## Objective

The `csv_crud_manage` module provides a convenient Python interface for performing basic CRUD (Create, Read, Update, Delete) operations on CSV (Comma Separated Values) files. It allows users to efficiently manage data in CSV files using Python.

## Features

- **Create:** Add new records to a CSV file.
- **Read:** View the content of a CSV file.
- **Update:** Modify existing records in the CSV file.
- **Delete:** Remove specific records from the CSV file.

## Example Usage

```python
import csv_crud_manage

# Create a new record
csv_crud_manage.create_record('data.csv', {'Name': 'John Doe', 'Email': 'john@example.com', 'Age': 30})

# Read the CSV file
data = csv_crud_manage.read_csv('data.csv')
print(data)

# Update a record
csv_crud_manage.update_record('data.csv', 1, {'Name': 'Jane Doe', 'Email': 'jane@example.com', 'Age': 35})

# Delete a record
csv_crud_manage.delete_record('data.csv', 2)
```

## Installation

To install the required dependencies, you can use `pip` and the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```