#!/usr/bin/python3
"""
Defines a Rectangle class with all required features.
"""


class Rectangle:
    """
    Rectangle with width, height, area, perimeter, and utility methods.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance with optional width and height.
        Increments the instance counter.
        Args:
            width (int): The width of the rectangle (default 0).
            height (int): The height of the rectangle (default 0).
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieve the width of the rectangle.
        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle with validation.
        Args:
            value (int): The new width of the rectangle.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieve the height of the rectangle.
        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle with validation.
        Args:
            value (int): The new height of the rectangle.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Compute and return the area of the rectangle.
        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Compute and return the perimeter of the rectangle.
        Returns:
            int: The perimeter of the rectangle, or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        Return the string representation of the rectangle using
        the print_symbol.
        Returns:
            str: The rectangle as a string of print_symbol characters.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("\n".join([str(self.print_symbol) * self.__width
                           for _ in range(self.__height)]))

    def __repr__(self):
        """
        Return the official string representation of the rectangle.
        Returns:
            str: A string that can recreate the instance with eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Print a message when a Rectangle instance is deleted and
        decrement the instance counter.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the rectangle with the biggest area, or rect_1 if equal.
        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.
        Raises:
            TypeError: If rect_1 or rect_2 is not a Rectangle instance.
        Returns:
            Rectangle: The rectangle with the largest area, or rect_1 if equal.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """
        Create a new Rectangle instance with width and height equal to size.
        Args:
            size (int): The size of the square sides (default 0).
        Returns:
            Rectangle: A new Rectangle instance with width == height == size.
        """
        return cls(size, size)
