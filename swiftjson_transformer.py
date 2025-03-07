import pandas as pd
import json
import dask.dataframe as dd


def same_length(flattened: dict):
    max_len = max((len(v) for v in flattened.values() if isinstance(v, list)), default=0)
    for key in flattened.keys():
        if isinstance(flattened[key], list) and len(flattened[key]) < max_len:
            flattened[key].extend([None] * (max_len - len(flattened[key])))
    return flattened

def process_value(keys, value, flattened):
    if isinstance(value, dict):
        for key in value.keys():
            process_value(keys + [key], value[key], flattened)
    elif isinstance(value, list):
        for v in value:
            process_value(keys, v, flattened)
    else:
        jkey = '__'.join(keys)
        if jkey in flattened:
            if isinstance(flattened[jkey], list):
                flattened[jkey].append(value)
            else:
                flattened[jkey] = [flattened[jkey], value]
        else:
            flattened[jkey] = value

def flatten_json(json_data):
    flattened_result = {}
    json_list = json_data if isinstance(json_data, list) else [json_data]
    for j in json_list:
        for key in j.keys():
            process_value([key], j[key], flattened_result)
    return flattened_result

INPUT_FILE_PATH = "input_file.json"  # Modify as needed

try:
    with open(INPUT_FILE_PATH, "r") as f:
        y = json.load(f)
except (FileNotFoundError, PermissionError, OSError):
    print("Error opening file")
    exit(1)

flat = flatten_json(y)
df = pd.DataFrame.from_dict(same_length(flat), orient='columns')

# Adjust partitioning as needed based on dataset size
ddf = dd.from_pandas(df, npartitions=8)

OUTPUT_FILE_PATH = "your_output_file.csv"  # Modify as needed
ddf.to_csv(OUTPUT_FILE_PATH, index=False, encoding='utf-8', single_file=True)
