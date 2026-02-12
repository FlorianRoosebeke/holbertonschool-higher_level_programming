#!/usr/bin/python3
"""Module for writing text to a file."""


def write_file(filename="", text=""):
    """Write text to a file.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text content to write.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w+") as f:
        f.write(text)
        f.close()
