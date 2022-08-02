import csv
from pprint import pprint

with open("rib_table.csv") as f:
    reader_data = csv.DictReader(f)
    for row in reader_data:
        # pprint(row, sort_dicts=False)
        print([row["network"], row["netmask"], row["nexthop"]])
