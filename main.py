from s3_operations import read_bucket
from utils import *
from validate import *
from log import *
import sys
import re

########################################################
# bucket_name="ghrc-cog"
# prefix="NALMA/"

# _type="NALMA"
# expr1=r"_(\d{8})_" #extract date
# expr2=r"(\d+)\.tif$" #extract band

# outfile_path="testing.json"
########################################################

if len(sys.argv) < 7:
    print("Error. Need at least 7 input parameters.")
    input_format()
    sys.exit()

_ , bucket_name, prefix, expr1, expr2, expr3, outfile_path = sys.argv

expr1 = re.compile(expr1)
expr2 = re.compile(expr2)
expr3 = re.compile(expr3)
########################################################


files = read_bucket(bucket_name, prefix)
print("Data read from the Bukcet.")

data = []
for path in files:
    filename = extract_filename(path['Key'])
    _type, date, band = extract_date_band(filename, expr1, expr2, expr3)
    data.append({
        "type":_type,
        "date":date,
        "band":band,
        "path":path['Key']
    })
print("Dict of data complete.")

json_outfile(data, outfile_path)
print("Json has been created.")
