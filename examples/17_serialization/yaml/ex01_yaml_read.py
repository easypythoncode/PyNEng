import yaml
from pprint import pprint

with open("devices.yaml") as f:
    data = yaml.safe_load(f)
    pprint(data)
