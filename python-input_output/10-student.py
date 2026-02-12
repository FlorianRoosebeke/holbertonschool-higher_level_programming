#!/usr/bin/python3
"""Module defining a Student class with selective JSON serialization."""


class Student:
    """A class to represent a student with selective attribute serialization.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get student attributes as a dictionary with optional filtering.

        Args:
            attrs (list, optional): A list of attribute names to include.
                                    If None or not a list of strings, all
                                    attributes are included.

        Returns:
            dict: Dictionary of selected or all student attributes.
        """
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):

            obj_dict = vars(self)
            dict_sort = {}

            for keys in attrs:
                if keys in obj_dict:
                    dict_sort[keys] = obj_dict[keys]
            return dict_sort

        else:
            return vars(self)
