import json_divider

# Divide a large JSON file into smaller chunks
json_divider.divide('large_data.json', chunk_size=1000, output_folder='output_folder')

# Customize the naming convention for output files
json_divider.divide('large_data.json', chunk_size=500, output_folder='output_folder', custom_names=['part1.json', 'part2.json'])