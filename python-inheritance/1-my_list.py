#!/usr/bin/python3
"""Module for MyList class."""


class MyList(list):
    """A list subclass that can print sorted list."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
