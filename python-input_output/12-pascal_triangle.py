#!/usr/bin/python3
"""
Module used to generate Pascal's triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's
    triangle of n rows

    Args:
        n (int): The number of rows in Pascal's triangle

    Returns:
        list: A list of lists of integers representing Pascal's
              triangle. Returns an empty list if n <= 0
    """

    if n <= 0:
        return []

    triangle = []

    for row in range(n):
        if row == 0:
            line = [1]
        else:
            line = [1]
            for column in range(1, row):
                line.append(triangle[row - 1][column - 1] +
                            triangle[row - 1][column])
            line.append(1)
        triangle.append(line)
    return triangle
