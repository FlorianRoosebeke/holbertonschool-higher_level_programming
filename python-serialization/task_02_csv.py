#!/usr/bin/python3
"""Module for basic serialization with JSON."""

import json
import csv


def convert_csv_to_json(CSV_filename):
    """Convert CSV file to JSON format."""
    list = []
    
    try:
        with open(CSV_filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                list.append(row)

        with open("data.json", "w") as f:
            json.dump(list, f, indent=4)
        return True
    except FileNotFoundError:
        return False
