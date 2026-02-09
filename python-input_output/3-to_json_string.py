#!/usr/bin/python3
import json


def to_json_string(my_obj):
    with open(my_obj, "r") as f:
        data = json.load(f)
    print(json.dumps(data, indent=4))
    f.close()
