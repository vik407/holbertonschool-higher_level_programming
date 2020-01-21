#!/usr/bin/python3
"""1. Number of lines
"""


def number_of_lines(filename=""):
    """Write a function that returns the number of lines of a text file
    """
    line_number = 0
    with open(filename, 'r') as file:
        for line in file:
            line_number += 1

    return(line_number)
