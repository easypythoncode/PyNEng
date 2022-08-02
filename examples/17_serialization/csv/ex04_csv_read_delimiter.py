import csv
from pprint import pprint

filter_keys = ["network", "netmask", "nexthop"]

with open("rib_table_delimiter.csv") as f:
    reader_data = csv.DictReader(f, delimiter=";")
    for row in reader_data:
        pprint(row, sort_dicts=False)
        # new_dict = {
        #    key: value for key, value in row.items()
        #    if key in filter_keys
        # }
        # pprint(new_dict)
