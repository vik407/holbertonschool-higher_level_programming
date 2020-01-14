#!/usr/bin/python3
"""
matrix_divided - a function that divides all elements of a matrix.
Returns a new matrix
"""


def matrix_divided(matrix, div):
    """
    @matrix = a list of lists of integers or floats
    @div = must be a number (integer or float)
    """
    msg_1 = "matrix must be a matrix (list of lists) of integers/floats"
    msg_2 = "Each row of the matrix must have the same size"
    msg_3 = "div must be a number"
    msg_4 = "division by zero"
    equals = []
    if (matrix == []):
        raise TypeError(msg_1)
    if isinstance(matrix, (list)) is None or matrix is False:
        raise TypeError(msg_1)
    if isinstance(div, (int, float)) is False:
        raise TypeError(msg_3)
    if (div == 0):
        raise ZeroDivisionError(msg_4)
    if(len(set([len(_list) for _list in matrix])) > 1):
        raise TypeError(msg_2)
    for row in matrix:
        if isinstance(row, list) is False:
            raise TypeError(msg_1)
        for a in row:
            if isinstance(a, (int, float)) is False:
                raise TypeError(msg_1)
    equals = [[round(num / div, 2) for num in row] for row in matrix]
    return equals
