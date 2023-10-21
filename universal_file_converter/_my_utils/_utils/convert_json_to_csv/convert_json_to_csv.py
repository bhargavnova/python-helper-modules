import json
import pandas as pd

class ConvertJSONtoCSV(object):
    def __init__(self, json_filename: str, csv_filename: str):
        self.json_file = json_filename
        self.csv_file = csv_filename
    
    def read_json(self) -> dict:
        with open(self.json_file, 'r', encoding='utf-8') as read_file:
            return json.loads(read_file.read())
    
    def flatten_json(self, json_content: dict) -> object:
        return pd.json_normalize(json_content)
    
    def dump_to_csv(self, data_frame: object):
        data_frame.to_csv(self.csv_file, index=False, encoding='utf-8')
    
    def convert_json_to_csv(self):
        json_data = self.read_json()
        self.dump_to_csv(self.flatten_json(json_data))

if __name__ == "__main__":
    pdf_converter = ConvertJSONtoCSV("input.json", "output.csv")
    pdf_converter.convert_json_to_csv()