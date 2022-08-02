from pprint import pprint
import re

result = []

regex = r"^(\S+) *([A-Z][a-z]+ \S+) +\d+.+ (\S+ \S+)"
with open("sh_cdp_n_sw1.txt") as f:
    for line in f:
        match_line = re.search(regex, line)
        if match_line:
            print(match_line.groups())
            neighbor, l_intf, n_intf = match_line.groups()

pprint(result)
