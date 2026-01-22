#!/usr/bin/python3
"""Simple helpers to divide a matrix."""


def matrix_divided(matrix, div):
    """Return a new matrix with each element divided by ``div``.

    Args:
        matrix (list of lists): 2D array of ints/floats to divide.
        div (int or float): Number to divide each element by.

    Raises:
        TypeError: If ``div`` is not a number or any matrix element is not int/float.
        ZeroDivisionError: If ``div`` is zero.
        TypeError: If rows do not all share the same length.

    Returns:
        list of lists: New matrix where each value is rounded to 2 decimals.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for ligne in matrix:
        new_ligne = []
        for element in ligne:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix of integers/floats")
            new_ligne.append(round(element / div, 2))
        new_matrix.append(new_ligne)

    return new_matrix
