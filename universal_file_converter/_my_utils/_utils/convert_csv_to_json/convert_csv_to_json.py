import json
import csv

class ConvertCSVtoJSON(object):
    def __init__(self, csv_filename: str, json_filename: str):
        self.csv_file = csv_filename
        self.json_file = json_filename
    
    def read_csv(self) -> list:
        all_rows = []
        with open(self.csv_file, 'r', encoding='utf-8') as read_file:
            for row in csv.DictReader(read_file):
                all_rows.append(row)
        return all_rows
    
    def dump_to_json(self, content: list):
        with open(self.json_file, 'w', encoding='utf-8') as write_file:
            json.dump(content, write_file, indent=4)
    
    def convert_csv_to_json(self):
        self.dump_to_json(self.read_csv())

if __name__ == "__main__":
    pdf_converter = ConvertCSVtoJSON("input.csv", "output.json")
    pdf_converter.convert_csv_to_json()