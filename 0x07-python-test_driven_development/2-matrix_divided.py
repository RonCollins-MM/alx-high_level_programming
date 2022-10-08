#!/usr/bin/python3
"""
Module that divides each element of a matrix.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by an equal divisor to the nearest 2
    decimal places.

    Args:
        matrix - The matrix
        div - The divisor

    Returns:
        A new matrix of the elements after division

    Raises:
        TypeError:
            If the matrix elements are not of type ``int`` or ``float``.
            If the rows of the matrix are not of the same size.
        ZeroDivisionError:
            If div == 0
    """

    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    len_rows = []
    for row in matrix:
        len_rows.append(len(row))

    # This.. THIS is why I love Python !!!!!
    if not all(elem == len_rows[0] for elem in len_rows):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # This is also why I love Python... such beauty in a single line :`)
    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]

    return new_matrix
