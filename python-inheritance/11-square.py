#!/usr/bin/python3
"""Module for BaseGeometry, Rectangle and Square classes."""


class BaseGeometry:
    """A base geometry class with validation methods."""

    def area(self):
        """Raise an exception - not implemented yet."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a Rectangle with width and height validation."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a Square with size validation."""
        self.integer_validator("size", size)
        self._Rectangle__width = size
        self._Rectangle__height = size

    def area(self):
        """Return the area of the square."""
        return super().area()

    def __str__(self):
        """Return string representation of the square."""
        return "[Square] {}/{}".format(self._Rectangle__width,
                                       self._Rectangle__height)
