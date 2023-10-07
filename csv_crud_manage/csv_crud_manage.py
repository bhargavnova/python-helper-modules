"""
A Python module that allows users to perform basic 
CRUD (Create, Read, Update, Delete) operations on CSV (Comma Separated Values) files. 
This module will provide a convenient interface for managing data in CSV files using Python.
"""


import os
import pandas as pd

def create_record(file_path, data):
    """
    Create a new record in the CSV file.

    Args:
        file_path (str): Path to the CSV file.
        data (dict): Dictionary containing record data.
    """
    if not os.path.isfile(file_path):
        csv_data = pd.DataFrame(columns=data.keys())
    else:
        csv_data = pd.read_csv(file_path)

    csv_data = csv_data.append(data, ignore_index=True)
    csv_data.to_csv(file_path, index=False)

def read_csv(file_path):
    """
    Read the content of the CSV file.

    Args:
        file_path (str): Path to the CSV file.
    """
    if os.path.isfile(file_path):
        csv_data = pd.read_csv(file_path)
        return csv_data.to_dict('records')
    else:
        print(f"The file '{file_path}' does not exist.")
        return None

def update_record(file_path, index, data):
    """
    Update an existing record in the CSV file.

    Args:
        file_path (str): Path to the CSV file.
        index (int): Index of the record to be updated.
        data (dict): Dictionary containing updated record data.
    """
    if os.path.isfile(file_path):
        csv_data = pd.read_csv(file_path)
        if index >= len(csv_data):
            print(f"Index {index} is out of range.")
        else:
            csv_data.iloc[index] = data
            csv_data.to_csv(file_path, index=False)
    else:
        print(f"The file '{file_path}' does not exist.")

def delete_record(file_path, index):
    """
    Delete a record from the CSV file.

    Args:
        file_path (str): Path to the CSV file.
        index (int): Index of the record to be deleted.
    """
    if os.path.isfile(file_path):
        csv_data = pd.read_csv(file_path)
        if index >= len(csv_data):
            print(f"Index {index} is out of range.")
        else:
            csv_data = csv_data.drop(index, axis=0).reset_index(drop=True)
            csv_data.to_csv(file_path, index=False)
    else:
        print(f"The file '{file_path}' does not exist.")
