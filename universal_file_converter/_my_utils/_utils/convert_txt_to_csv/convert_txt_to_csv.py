import csv


class ConvertTXTtoCSV(object):
    def __init__(self, txt_filepath, csv_filepath) -> None:
        self.txt_filepath = txt_filepath
        self.csv_filepath = csv_filepath

    def convert_txt_to_csv(self, separator: str = ',') -> None:
        with open(self.txt_filepath, 'r', newline='', encoding='utf-8') as txt_file:
            with open(self.csv_filepath, 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.writer(csv_file)

                for line in txt_file:
                    row = line.strip().split(sep=separator)
                    writer.writerow(row)


if __name__ == "__main__":
    converter = ConvertTXTtoCSV("input.txt", "output.csv")
    converter.convert_txt_to_csv()
