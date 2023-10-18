"""
A Python module that column wise adds two CSV's

Assuming the column names are the same
"""

import os
import csv


def merge_csv(csv_path_1,csv_path_2):

    if os.path.exists(csv_path_1) and os.path.exists(csv_path_2):

            with open(csv_path_1, 'r', newline='') as f1, open(csv_path_2, 'r', newline='') as f2:
                reader1 = csv.reader(f1)
                reader2 = csv.reader(f2)
                headers1 = next(reader1)
                headers2 = next(reader2)

                # Check if the headers fields match, even if they are in different orders
                if set(headers1) == set(headers2):
                    # Create a list to store the merged data
                    merged_data = [headers1]

                    # Create a dictionary to map header names to their respective indices in file2
                    header_index_map = {header: index for index, header in enumerate(headers2)}


                    # Read and merge the data from file2
                    for row in reader1:
                        merged_data.append(row)

                    # Read and merge the data from file1
                    for row in reader2:
                        merged_row = [''] * len(headers1)
                        for index, header in enumerate(headers1):
                            if header in header_index_map:
                                merged_row[index] = row[header_index_map[header]]
                        merged_data.append(merged_row)



                    # Write the merged data to the output file
                    with open("Output.csv", 'w', newline='') as output_csv:
                        writer = csv.writer(output_csv)
                        writer.writerows(merged_data)
                    print("CSV files merged successfully.")
                else:
                    print("Header names do not match. Cannot merge CSV files.")


    elif not os.path.exists(csv_path_1):

        print(f"{csv_path_1} doesn't exist !")
    else:
        print(f"{csv_path_2} doesn't exist !")
    

