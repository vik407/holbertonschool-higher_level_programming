#!/usr/bin/python3
"""
add_integer - a function that adds 2 integers.
Returns an integer: the addition of a and b
"""


def add_integer(a, b=98):
    """
    @a = integers or floats
    @b = integers or floats (initialized in 98)
    """

    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    return(int(a) + int(b))
