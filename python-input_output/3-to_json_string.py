#!/usr/bin/python3
"""Module for converting Python objects to JSON strings."""
import json


def to_json_string(my_obj):
    """Convert a Python object to a JSON string representation.

    Args:
        my_obj: A Python object (list, dict, etc.) to convert.

    Returns:
        str: JSON string representation of the object.
    """
    return json.dumps(my_obj)
