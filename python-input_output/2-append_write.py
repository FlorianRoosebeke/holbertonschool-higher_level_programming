#!/usr/bin/python3
"""Module for appending text to a file."""


def append_write(filename="", text=""):
    """Append text to the end of a file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text content to append.

    Returns:
        int: The number of characters appended.
    """
    with open(filename, "a+") as f:
        f.write(text)
        f.close()
