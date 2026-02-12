#!/usr/bin/python3
"""Module for loading Python objects from JSON files."""
import json


def load_from_json_file(filename):
    """Load a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        object: Python object loaded from the JSON file.
    """
    with open(filename, 'r') as f:
        return json.load(f)
