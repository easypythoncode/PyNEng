from pprint import pprint
import re

with open("sh_cdp_neighbors_sw1.txt") as f:
    out = f.read()
"""
------\nDevice ID: SW2\nEntry address(es):\n  IP address: 10.1.1.2\nPlatform: cisco WS-C2960-8TC-L,  Capabilities: Switch IGMP,\nInterface: GigabitEthernet1/0/16,  Port ID (outgoing port): GigabitEthernet0/1\nHoldtime : 164 sec\n\nVersion :\nCisco IOS Software, C2960 Software (C2960-LANBASEK9-M), Version 12.2(55)SE9, RELEASE SOFTWARE (fc1)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2014 by Cisco Systems, Inc.\nCompiled Mon 03-Mar-14 22:53 by prod_rel_team\n\nadvertisement version: 2\nVTP Management Domain: ''\nNative VLAN: 1\nDuplex: full\nManagement address(es):\n  IP address: 10.1.1.2\n\n-------------------------
"""
regex = (
    r"Device ID: (?P<device>.+)\n"
    r".+\n"
    r" +IP address: (?P<ip>\S+)\n"
    r"Platform: (?P<platform>.+?),"
    r"(.*\n)+?"
    r"Cisco IOS .+?, (?P<ios>.+),"
)
result = {}
match_all = re.finditer(regex, out)
for m in match_all:
    groupdict = m.groupdict()
    device = groupdict.pop("device")
    result[device] = groupdict

pprint(result)
