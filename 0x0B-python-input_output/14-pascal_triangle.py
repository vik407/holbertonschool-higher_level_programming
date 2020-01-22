#!/usr/bin/python3
"""14. Pascal's Triangle
"""


def pascal_triangle(n):
    """A function def pascal_triangle(n): that returns a list of lists of
    integers representing the Pascal’s triangle of n
    """
    list = []
    if n <= 0:
        return list

    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(i):
                row.append(sum(list[-1][j:j + 2]))
        list.append(row)
    return list
