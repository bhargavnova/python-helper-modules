import pandas as pd


def merge(file_list: list[str], seperator: str = ';', how: str = 'outer') -> pd.DataFrame:
    """
        Merge a list of csv files into a single DataFrame.
        Parameters:
            file_list (list of csv_files): List of csv files (str) to be merged.
            seperator (str): seperator to use to read and save csv (default is ':').
            how (str): Type of merge to be performed (default is 'outer').
                     You can choose from 'inner', 'outer', 'left', or 'right'.
        Returns:
            pd.DataFrame: Merged DataFrame.
        """
    # check if how is valid:
    if how not in ['inner', 'outer', 'left', 'right']:
        raise ValueError(f"The Join '{how}' is not valid, you can choose from 'inner', 'outer', 'left', or 'right'.")

    # check if file_list is not empty:
    if len(file_list) < 2:
        raise ValueError(r"file_list do not have enough files to merge")

    # Generate the list of dataframe from file list.
    df_list = [pd.read_csv(file, sep=seperator) for file in file_list]

    # concat all dataframe from df_list using the join method 'how' (default is 'outer')
    df_concat = pd.concat(df_list, axis=0, ignore_index=True, join=how)

    return df_concat


if __name__ == '__main__':

    csv_files_to_merge = ['merge_csv_files/example-csv/data.csv', 'merge_csv_files/example-csv/data2.csv']
    output_csv = 'merge_csv_files/example-csv/merged_data.csv'
    sep = ';'

    # merge csv files
    df = merge(file_list=csv_files_to_merge, seperator=sep)
    print(df)

    # Save the dataframe with merged data in the output_csv.
    df.to_csv(output_csv, index=False, sep=sep)
