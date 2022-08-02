from pprint import pprint
import re

regex = r"(\S+) +(\S+) +\S+ +\S+ +(up|down) +(up|down)"
with open("sh_ip_int_br.txt") as f:
    out = f.read()
    result = re.findall(regex, out)

pprint(result)
