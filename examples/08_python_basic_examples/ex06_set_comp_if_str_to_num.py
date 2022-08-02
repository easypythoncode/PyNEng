from pprint import pprint

items = ["10", "20", "30", "mode", "1", "11", "100", "trunk", "10", "20"]
vlans = set()

for vl in items:
    if vl.isdigit():
        vlans.add(int(vl))

pprint(vlans)

# set comp
items = ["10", "20", "30", "mode", "1", "11", "100", "trunk", "10", "20"]
vlans = {int(vl) for vl in items if vl.isdigit()}
pprint(vlans)
