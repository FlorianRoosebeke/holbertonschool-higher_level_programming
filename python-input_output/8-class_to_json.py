#!/usr/bin/python3
"""Module for converting class instances to dictionaries."""


def class_to_json(obj):
    """Convert a class instance to a dictionary representation.

    Args:
        obj: A class instance to convert.

    Returns:
        dict: Dictionary representation of the object's attributes.
    """
    dict_obj = vars(obj)
    return dict_obj
