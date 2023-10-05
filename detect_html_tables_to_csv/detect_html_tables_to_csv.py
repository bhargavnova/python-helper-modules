import csv
from pathlib import Path
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import argparse


parser = argparse.ArgumentParser()
parser.add_argument(
    "--prefix",
    default="table",
    help="The Prefix of the tables that are to be saved",
)
parser.add_argument(
    "--url",
    default="http://localhost:5500/detect_html_tables_to_csv/assets/home.html",
    help="The target url for scraping tables",
)
args = parser.parse_args()
html_url = args.url
csv_file_prefix = args.prefix
output_file_dir = f"{Path(__file__).parent.absolute()}/tables/"


def scrape_and_export_tables(html_url):
    """For scraping HTML tables in a url and exporting them to a csv file"""
    try:
        try:
            response = requests.get(html_url)
            response.raise_for_status()  # Check for HTTP request errors
        except Exception as err:
            print(f"Error while fetching data from the URL")
            raise err
        soup = BeautifulSoup(
            response.text, "html.parser"
        )  # Parse the HTML content with BeautifulSoup & find all the tables in the HTML
        tables = soup.find_all("table")
        if not tables:
            raise ValueError("No tables found in the HTML")
        # Export each table to a separate CSV file
        for i, table in enumerate(tables):
            curr_dt = datetime.utcnow().strftime("%Y-%m-%d")
            csv_filename = f"{output_file_dir}{csv_file_prefix}-{curr_dt}-{i + 1}.csv"
            with open(csv_filename, "w", newline="") as csv_file:
                csv_writer = csv.writer(csv_file)
                # Loop through the rows and cells of the table
                for row in table.find_all("tr"):
                    row_data = [
                        cell.get_text(strip=True) for cell in row.find_all(["th", "td"])
                    ]
                    csv_writer.writerow(row_data)
            print(f"Table {i + 1} exported to '{csv_filename}'.")
    except requests.exceptions.RequestException as e:
        print(f"Error in HTTP request: {e}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")


if __name__ == "__main__":
    scrape_and_export_tables(html_url)
