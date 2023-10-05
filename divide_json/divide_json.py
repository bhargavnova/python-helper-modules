import json_divider
import os


basePath = os.path.dirname(os.path.abspath(__file__))

filePath=basePath + '/' + 'large_data.json'
output_folder=basePath + '/' + 'output_folder'

# Divide a large JSON file into smaller chunks
# json_divider.divide(filePath, chunk_size=1, output_folder=output_folder)

# Customize the naming convention for output files
json_divider.divide(filePath, chunk_size=5, output_folder=output_folder, custom_names=['file1.json', 'file2.json'])