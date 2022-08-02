from pprint import pprint
import re

result = []

regex = r"(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)"
with open("dhcp_snooping.txt") as f:
    for line in f:
        match_line = re.search(regex, line)
        if match_line:
            # print(match_line.group())
            # mac, ip, _, _, vlan, intf = line.split()
            mac, ip, vlan, intf = match_line.groups()
            # print(mac, ip, vlan, intf)
            result.append(match_line.groups())
pprint(result)
