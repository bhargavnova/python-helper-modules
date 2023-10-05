import json
import pandas as pd

def flatten_json(json_data, prefix=''):
    flattened_data = {}
    for key, value in json_data.items():
        if isinstance(value, dict):
            flattened_data.update(flatten_json(value, prefix + key + '_'))
        elif isinstance(value, list):
            for i, item in enumerate(value):
                if isinstance(item, dict):
                    flattened_data.update(flatten_json(item, prefix + key + str(i) + '_'))
                else:
                    flattened_data[prefix + key + str(i)] = item
        else:
            flattened_data[prefix + key] = value
    return flattened_data

def convert(input_json_file, output_csv_file, field_mapping=None):
    try:
        with open(input_json_file, 'r') as json_file:
            data = json.load(json_file)

        if field_mapping:
            data = {field_mapping.get(k, k): v for k, v in data.items()}

        if isinstance(data, list):
            flattened_data_list = []
            for item in data:
                flattened_item = flatten_json(item)
                flattened_data_list.append(flattened_item)
            df = pd.DataFrame(flattened_data_list)
        else:
            flattened_data = flatten_json(data)
            df = pd.DataFrame([flattened_data])

        df.to_csv(output_csv_file, index=False)

        print(f"Conversion successful. CSV saved as {output_csv_file}")

    except FileNotFoundError:
        print("Input JSON file not found.")
    except json.JSONDecodeError:
        print("Invalid JSON format in the input file.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    input_json_file = 'input.json'
    output_csv_file = 'output.csv'
    
    # Convert JSON to CSV
    convert(input_json_file, output_csv_file)
    
    # Convert JSON with custom mapping
    mapping = {'Name': 'full_name', 'Email': 'contact.email', 'Phone': 'contact.phone'}
    convert(input_json_file, output_csv_file, field_mapping=mapping)
