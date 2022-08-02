from pprint import pprint


def clean_cfg(filename):
    cleaned_lines = []
    with open(filename) as f:
        for line in f:
            if not line.startswith("!") and line.strip() != "":
                cleaned_lines.append(line)
    return cleaned_lines


result = clean_cfg("config_r1.txt")
pprint(result)
result = clean_cfg("config_r2.txt")
pprint(result)
