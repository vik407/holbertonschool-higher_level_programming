#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for elem in row:
            print("{:d}".format(elem), end="")
            if (row.index(elem) + 1) < len(row):
                print(" ", end="")
        print("\n", end="")
