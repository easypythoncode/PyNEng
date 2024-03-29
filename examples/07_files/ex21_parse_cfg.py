from pprint import pprint

result = {}

with open("configs/config_r1.txt") as f:
    for line in f:
        if line.startswith("interface"):
            intf = line.split()[-1]
            result[intf] = None
        elif line.startswith(" ip address"):
            ip = line.split()[-2]
            print(f"{intf=} {ip=}")
            result[intf] = ip

pprint(result)
