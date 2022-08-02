from pprint import pprint

r1 = {
    "IOS": "15.4",
    "IP": "10.255.0.1",
    "hostname": "london_r1",
    "location": "21 New Globe Walk",
    "model": "4451",
    "vendor": "Cisco",
}

lower_r1 = {}
for key, value in r1.items():
    lower_r1[key.lower()] = value

pprint(lower_r1, sort_dicts=False)

# dict comp
r1 = {
    "IOS": "15.4",
    "IP": "10.255.0.1",
    "hostname": "london_r1",
    "location": "21 New Globe Walk",
    "model": "4451",
    "vendor": "Cisco",
}

lower_r1 = {key.lower(): value for key, value in r1.items()}
pprint(lower_r1, sort_dicts=False)
pprint(r1.keys())
