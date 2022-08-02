from pprint import pprint
import re

result = []
regex = r"(\S+) +(\S+) +\S+ +\S+ +(up|down) +(up|down)"
with open("sh_ip_int_br.txt") as f:
    out = f.read()
    match_all = re.finditer(regex, out)
    for m in match_all:
        result.append(m.groups())

pprint(result)
