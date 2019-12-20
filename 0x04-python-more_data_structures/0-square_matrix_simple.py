#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    _matrix = []
    for row in matrix:
        _row = []
        for col in row:
            _row.append(col ** 2)
        _matrix.append(_row)
    return _matrix
