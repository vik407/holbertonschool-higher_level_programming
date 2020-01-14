#!/usr/bin/python3
"""
matrix_divided - a function that prints My name is <first name> <last name>
Returns <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    @first_name = str with firstname value
    @last_name = str with last_name value
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print("My name is {:s} {:s}".format(first_name, last_name))
