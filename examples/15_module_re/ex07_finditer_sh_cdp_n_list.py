from pprint import pprint
import re

with open("sh_cdp_neighbors_sw1.txt") as f:
    out = f.read()
regex = (
    r"Device ID: (?P<device>.+)\n"
    r".+\n"
    r" +IP address: (?P<ip>\S+)\n"
    r"Platform: (?P<platform>.+?),"
    r"(?:.*\n)+?"
    r"Cisco IOS .+?, (?P<ios>.+),"
)
result = []
match_all = re.finditer(regex, out)
for m in match_all:
    result.append(m.groups())
pprint(result, width=120)
