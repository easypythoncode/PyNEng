import csv

data = [['hostname', 'vendor', 'model', 'location'],
        ['sw1', 'Cisco', 3750, 'London, Best str'],
        ['sw2', 'Cisco', 3850, 'Liverpool, Better str'],
        ['sw3', 'Cisco IOS', 3650, 'Liverpool, Better str'],
        ['sw4', 'Cisco IOS', 3650, 'London, Best str']]

with open("sw_data_write.csv", "w") as f:
    wr = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=";")
    for row in data:
        wr.writerow(row)
