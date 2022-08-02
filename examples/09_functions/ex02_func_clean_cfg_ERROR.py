from pprint import pprint

cfg_file = "config_r1.txt"


def clean_cfg(filename):
    cleaned_lines = []
    with open(filename) as f:
        # with open(cfg_file) as f:
        # with open("config_r1.txt") as f:
        for line in f:
            # if not line.startswith("!") and line.strip() != "":
            if "hostname" in line:
                cleaned_lines.append(line)
                return cleaned_lines


result = clean_cfg(cfg_file)
pprint(result)
result = clean_cfg("config_r2.txt")
pprint(result)
