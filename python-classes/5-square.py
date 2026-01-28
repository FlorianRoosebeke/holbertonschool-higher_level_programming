#!/usr/bin/python3
"""Module 5-square
Defines class Square with size and position properties, and print method."""


class Square:
    """Square class that defines a square by its size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The size of the square (default 0).
            position (tuple): The position (default (0, 0)).
        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if (not isinstance(position, tuple) or len(position) != 2 or
                not all(isinstance(x, int) and x >= 0 for x in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Print the square with the character # at position."""
        if self.size == 0:
            print()
            return
        print("\n" * self.__position[1], end='')
        for i in range(self.size):
            print(" " * self.__position[0] + "#" * self.__size)

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The new position.
        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(x, int) and x >= 0 for x in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
