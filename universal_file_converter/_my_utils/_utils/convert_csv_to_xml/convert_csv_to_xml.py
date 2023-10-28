import pandas as pd

class ConvertCSVtoXML(object):
    def __init__(self, csv_filename: str, xml_filename: str):
        self.csv_file = csv_filename
        self.xml_file = xml_filename
    
    def read_csv(self) -> dict:
        return pd.read_csv(self.csv_file)
    
    def to_xml(self, data_frame: object) -> object:
        return data_frame.to_xml()

    def dump_to_xml(self, xml_data_frame: object):
        with open(self.xml_file, 'w', encoding='utf-8') as write_file:
            write_file.write(xml_data_frame)
    
    def convert_csv_to_xml(self):
        csv_data = self.read_csv()
        self.dump_to_xml(self.to_xml(csv_data))

if __name__ == "__main__":
    csv_converter = ConvertCSVtoXML("input.csv", "output.xml")
    csv_converter.convert_csv_to_xml()