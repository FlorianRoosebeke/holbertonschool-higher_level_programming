#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div."""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for ligne in matrix:
        new_ligne = []
        for element in ligne:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix of integers/floats")
            new_ligne.append(round(element / div, 2))
        new_matrix.append(new_ligne)

    return new_matrix
