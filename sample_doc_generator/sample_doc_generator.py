from faker import Faker
import csv
import xml.etree.ElementTree as ET
import json


def generate_text_document(
    filename: str, words: int = 500, output_path: str = ""
) -> None:
    """generate_text_document
    ---
    This function generates a text file with random fake text.

    Parameters:
    ---
    filename: str
        Name of the file that will be saved

    Optional

    words: int
        max number of words that will be used inside the file.
    output_path: str
        path where the file will be saved.

    Return
    ---
    None

    """
    fake = Faker()
    paragraph = fake.text(max_nb_chars=words)
    file_path = output_path + filename

    with open(file_path, "w") as f:
        f.write(paragraph)


def generate_csv(filename: str, output_path: str = "", rows: int = 10) -> None:
    """generate_csv
    ---
    This function generates a csv file with random names, cities and addresses.

    Parameters:
    ---
    filename: str
        Name of the file that will be saved

    Optional

    rows: int
        numbers of rows inside the csv file.
    output_path: str
        path where the file will be saved.

    Return
    ---
    None

    """
    fake = Faker()

    header = ["name", "city", "address"]
    names = [fake.name() for x in range(rows)]
    city = [fake.city() for x in range(rows)]
    address = [fake.address() for x in range(rows)]

    file_path = output_path + filename

    with open(file_path, "w", encoding="UTF8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i in range(rows):
            writer.writerow([names[i], city[i], address[i]])


def generate_json(filename: str, output_path: str = "", items: int = 10) -> None:
    """generate_json
    ---
    This function generates a csv file with random names, cities and addresses.

    Parameters:
    ---
    filename: str
        Name of the file that will be saved.

    Optional

    items: int
        numbers of items inside the json file.
    output_path: str
        path where the file will be saved.

    Return
    ---
    None

    """
    fake = Faker()
    file_path = output_path + filename

    keys = [f"id_{x}" for x in range(items)]
    values = [[fake.name(), fake.city(), fake.address()] for x in range(items)]
    data = {k: v for k, v in zip(keys, values)}

    json_object = json.dumps(data, indent=4)

    with open(file_path, "w") as f:
        f.write(json_object)


def generate_xml(filename: str, output_path: str = "", items: int = 10) -> None:
    """generate_json
    ---
    This function generates a xml file with random names, cities and addresses.

    Parameters:
    ---
    filename: str
        Name of the file that will be saved.

    Optional

    items: int
        numbers of items inside the json file.
    output_path: str
        path where the file will be saved.

    Return
    ---
    None

    """
    fake = Faker()
    file_path = output_path + filename

    root = ET.Element("root")
    for i in range(items):
        item = ET.SubElement(root, "item")
        name = ET.SubElement(item, "name")
        city = ET.SubElement(item, "city")
        address = ET.SubElement(item, "address")
        name.text = fake.name()
        city.text = fake.city()
        address.text = fake.address()

    tree = ET.ElementTree(root)
    ET.indent(tree, space=" ", level=0)
    tree.write(file_path)
