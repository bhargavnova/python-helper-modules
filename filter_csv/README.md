# filter_csv

This module provides functions to filter data in a CSV file and save the filtered data in various formats.

## Usage

### Example code demonstrating how to use the module

```python
# Import the module
import module_name

# Filter CSV data
filtered_data = module_name.filter_csv('data.csv', 'column_name', '==', 'value', output='json')

# Save filtered data
module_name.save_filtered_data('filtered_data.csv', filtered_data, input='json')
```

## Installation

To use this module, make sure you have the required packages installed. You can install them using the following command:

```bash
pip install -r requirements.txt
```

## Functions

### `filter_csv(path, column, operator, value, output="dataframe")`

Filters a CSV file based on the provided column, operator, and value.

- `path` (str): Path to the CSV file.
- `column` (str): Name of the column to filter.
- `operator` (str): Comparison operator (e.g., '==', '!=', '<', '<=', '>', '>=').
- `value` (str): Value to compare against.
- `output` (str, optional): Output format ('dataframe', 'dict', 'json', 'list'). Default is 'dataframe'.

### `save_filtered_data(path, filtered_data, input="dataframe")`

Saves the filtered data to a CSV file.

- `path` (str): Path to save the CSV file.
- `filtered_data` (various types): Filtered data (input format depends on `input` parameter).
- `input` (str, optional): Input format ('dataframe', 'dict', 'json', 'list'). Default is 'dataframe'.

## Example

```python
# Import the module
import module_name

# Filter CSV data
filtered_data = module_name.filter_csv('data.csv', 'column_name', '==', 'value', output='json')

# Save filtered data
module_name.save_filtered_data('filtered_data.csv', filtered_data, input='json')
```
