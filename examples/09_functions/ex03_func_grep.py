from pprint import pprint


def grep_cfg(filename, pattern="service"):
    lines = []
    with open(filename) as f:
        for line in f:
            if pattern in line:
                lines.append(line)
    return lines


# Позиционные аргументы
result = grep_cfg("config_r1.txt", "ip address")
pprint(result)
result = grep_cfg("config_r1.txt", "interface")
pprint(result)
