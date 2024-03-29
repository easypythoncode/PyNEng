import json

london = {
    "sw1": {
        "IOS": "3.6.XE",
        "IP": "10.255.0.101",
        "hostname": "london_sw1",
        "location": "21 New Globe Walk",
        "model": "3850",
        "vendor": "Cisco",
    },
    "r1": {
        "IOS": "15.4",
        "IP": "10.255.0.1",
        "hostname": "london_r1",
        "location": "21 New Globe Walk",
        "model": "4451",
        "vendor": "Cisco",
    },
    "r2": {
        "IOS": "15.4",
        "IP": "10.255.0.2",
        "hostname": "london_r2",
        "location": "21 New Globe Walk",
        "model": "4451",
        "vendor": "Cisco",
    },
}
with open("london.json", "w") as f:
    json.dump(london, f, indent=2, sort_keys=True)
