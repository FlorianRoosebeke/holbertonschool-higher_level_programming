#!/usr/bin/python3
"""Module for inherits_from function."""


def inherits_from(obj, a_class):
    """Return True if obj is instance of inherited class from a_class."""
    return isinstance(obj, a_class) and not type(obj) is a_class
