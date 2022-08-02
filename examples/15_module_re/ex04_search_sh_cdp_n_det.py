import re
from pprint import pprint

result = {
    "SW2": {"ip": "10.1.1.2", "platform": "..."},
    "R1": {"ip": "10.1.1.2", "platform": "..."},
}
result = {}

with open("sh_cdp_neighbors_sw1.txt") as f:
    for line in f:
        if line.startswith("Device ID"):
            device = re.search(r"Device ID: (.+)", line).group(1)
            result[device] = {}
        elif "IP address" in line:
            ip = line.split()[-1]
            result[device]["ip"] = ip
        elif line.startswith("Platform"):
            platform = re.search(r"Platform: (.+?),", line).group(1)
            result[device]["platform"] = platform
        elif line.startswith("Cisco "):
            ios = re.search(r"Cisco .+?, (.+),", line).group(1)
            result[device]["ios"] = ios

pprint(result)
