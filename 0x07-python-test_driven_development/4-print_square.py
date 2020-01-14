#!/usr/bin/python3
"""
print_square - a function that prints a square with the character #.
Returns a square in the form of characters #
"""


def print_square(size):
    """
    @size = is the size length of the square
    """
    if isinstance(size, (int)) is None or size is False:
        raise TypeError("size must be an integer")
    if isinstance(size, (float)) is None and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        for col in range(size):
            print("{:s}".format("#"), end="")
        print()
