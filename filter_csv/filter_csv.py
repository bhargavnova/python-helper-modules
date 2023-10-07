import pandas as pd


def filter_csv(path, column, operator, value, output="dataframe"):
    if operator not in ["==", "!=", "<", "<=", ">", ">="]:
        raise Exception("Invalid Operator!!!")
        return

    data = pd.read_csv(path)
    filtered_data = data.query(f"{column} {operator} {value}")

    if output == "dict":
        return filtered_data.to_dict('list')
    elif output == "json":
        return filtered_data.to_json()
    elif output == "list":
        return [list(filtered_data.columns)] + filtered_data.values.tolist()

    return filtered_data


def save_filtered_data(path, filtered_data, input="dataframe"):
    if input == "dict":
        df = pd.DataFrame.from_dict(filtered_data)
        df.to_csv(path)
    elif input == "json":
        df = pd.DataFrame(filtered_data)
        df.to_csv(path)
    elif input == "list":
        df = pd.DataFrame(data=filtered_data[1:], columns=filtered_data[0])
        df.to_csv(path)
    else:
        filtered_data.to_csv(path)
