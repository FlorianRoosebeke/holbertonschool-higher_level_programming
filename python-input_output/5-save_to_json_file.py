#!/usr/bin/python3
"""Module for saving Python objects to JSON files."""
import json


def save_to_json_file(my_obj, filename):
    """Save a Python object to a JSON file.

    Args:
        my_obj: A Python object to save to JSON.
        filename (str): The name of the file to save to.

    Returns:
        None
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
