#!/usr/bin/python3
"""
print_square - a function that prints a square with the character #.
Returns a square in the form of characters #
"""


def print_square(size):
    """
    @size = is the size length of the square
    """
    if not isinstance(size, int):
        raise ValueError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return
    for row in range(int(size)):
        for col in range(int(size)):
            print("{:s}".format("#"), end="")
        print()
