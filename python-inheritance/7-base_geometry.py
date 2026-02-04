#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """A base geometry class with validation methods."""

    def area(self):
        """Raise an exception - not implemented yet."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
