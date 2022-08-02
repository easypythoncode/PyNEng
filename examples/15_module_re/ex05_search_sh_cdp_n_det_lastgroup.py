import re
from pprint import pprint

regex = (
    r"Device ID: (?P<device>.+)"
    r"|IP address: (?P<ip>\S+)"
    r"|Platform: (?P<platform>.+?),"
    r"|Cisco .+?, (?P<ios>.+),"
    r"|Duplex: (?P<duplex>\S+)"
    r"|Interface: (?P<local_intf>\S+), .+: (?P<remote_intf>\S+)"
)
result = {}

with open("sh_cdp_neighbors_sw1.txt") as f:
    for line in f:
        m = re.search(regex, line)
        if m:
            group = m.lastgroup
            group_value = m.group(group)
            if group == "device":
                device = group_value
                result[device] = {}
            elif group == "remote_intf":
                result[device][group] = group_value
                result[device]["local_inf"] = m.group("local_intf")
            else:
                result[device][group] = group_value

pprint(result)
