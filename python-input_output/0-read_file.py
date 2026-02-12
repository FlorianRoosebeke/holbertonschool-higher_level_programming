#!/usr/bin/python3
"""Module for reading and printing file contents."""


def read_file(filename=""):
    """Read and print the contents of a file.

    Args:
        filename (str): The name of the file to read.

    Returns:
        None
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.readlines())
