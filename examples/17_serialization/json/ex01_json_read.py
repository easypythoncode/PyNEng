import json
from pprint import pprint

with open("sw_templates.json") as f:
    data = json.load(f)
    pprint(data)
