#!/usr/bin/python3
"""Script that adds arguments to a Python list and saves to JSON file.

This script loads existing items from 'add_item.json', appends any
command-line arguments provided, and saves the updated list back to
the JSON file.

Usage:
    python3 7-add_item.py [item1] [item2] [item3] ...

Examples:
    python3 7-add_item.py first second third
    python3 7-add_item.py "hello world"
"""
import json
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__(
    '6-load_from_json_file.py').load_from_json_file

try:
    my_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    my_list = []

my_list.extend(argv[1:])
save_to_json_file(my_list, 'add_item.json')
