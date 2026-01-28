#!/usr/bin/python3
"""Module 3-square
Defines class Square with area method."""


class Square:
    """Square class that defines a square by its size and can compute area."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the square (default 0).
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size
