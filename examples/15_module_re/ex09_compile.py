from pprint import pprint
import re

with open("sh_cdp_neighbors_sw1.txt") as f:
    out = f.read()

regex = re.compile(
    r"Device ID: (?P<device>.+?)\n"
    r".+?"
    r" +IP address: (?P<ip>\S+)\n"
    r"Platform: (?P<platform>.+?),"
    r".+?"
    r"^Cisco IOS .+?, (?P<ios>.+?),",
    re.DOTALL | re.MULTILINE
)
result = {}
match_all = regex.finditer(out)

for m in match_all:
    groupdict = m.groupdict()
    device = groupdict.pop("device")
    result[device] = groupdict

pprint(result)
