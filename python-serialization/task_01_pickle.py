#!/usr/bin/python3
"""Module for basic serialization with JSON."""

import json
import pickle


class CustomObject:
    """A custom object class with name, age, and student status."""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject with name, age, and student status."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print a formatted string reprentation of the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object to a file using pickle."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file using pickle."""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
