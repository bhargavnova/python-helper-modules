import pandas as pd

def merge(file_list, output_file):
  df_list = []
  for file in file_list:
      df = pd.read_csv(file)
      df_list.append(df)
  df = pd.concat(df_list, axis=0, ignore_index=True)

  df.to_csv(output_file or 'output.csv', index=False)