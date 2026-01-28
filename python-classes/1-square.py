#!/usr/bin/python3
"""Module 1-square
Defines class Square with private size attribute."""


class Square:
    """Square class that defines a square by its size."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
