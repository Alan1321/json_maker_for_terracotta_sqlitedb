import re
import json

def extract_filename(file_path):
    result = re.search(r'[^/]+$', file_path)
    extracted_string=""
    if result:
        extracted_string = result.group()
    else:
        print("utils.py extract_filename >>> No match found.")
    return extracted_string

def extract_date_band(filename, expr1, expr2, expr3):
    result = re.search(expr1, filename)
    _type=""
    if result:
        date = result.group(1)
    else:
        print("utils.py extract_date_band >>> No match found. -- first")


    result = re.search(expr2, filename)
    date=""
    if result:
        date = result.group(1)
    else:
        print("utils.py extract_date_band >>> No match found. -- second")

    result = re.search(expr3, filename)
    band=""
    if result:
        band = result.group(1)
    else:
        print("utils.py extract_date_band >>> No match found. --third")
    return _type, date, band

def json_outfile(data, output_file_path="output.json"):
    # Export the list of dictionaries to a JSON file
    with open(output_file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)  # indent=4 for pretty formatting (optional)

