#!/usr/bin/python3
"""Module for converting JSON strings to Python objects."""
import json


def from_json_string(my_str):
    """Convert a JSON string to a Python object.

    Args:
        my_str (str): A JSON formatted string.

    Returns:
        object: Python object (list, dict, etc.) representation of the JSON.
    """
    return json.loads(my_str)
