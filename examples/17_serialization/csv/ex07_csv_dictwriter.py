import csv

data = [
    {"hostname": "sw1", "location": "London", "model": "3750", "vendor": "Cisco"},
    {"hostname": "sw2", "location": "Liverpool", "model": "3850", "vendor": "Cisco"},
    {"hostname": "sw3", "location": "Liverpool", "model": "3650", "vendor": "Cisco"},
    {"hostname": "sw4", "location": "London", "model": "3650", "vendor": "Cisco"},
]

with open("csv_write_dictwriter.csv", "w") as f:
    # headers = list(data[0].keys())
    wr = csv.DictWriter(
        f, fieldnames=["hostname", "model", "vendor", "location"],
        quoting=csv.QUOTE_ALL
    )
    wr.writeheader()
    for row in data:
        wr.writerow(row)
