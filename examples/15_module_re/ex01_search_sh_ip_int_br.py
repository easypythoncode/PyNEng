from pprint import pprint
import re

result = []
regex = r"(\S+) +(\S+) +\S+ +\S+ +(up|down) +(up|down)"
with open("sh_ip_int_br.txt") as f:
    for line in f:
        match_line = re.search(regex, line)
        if match_line:
            result.append(match_line.groups())

pprint(result)
