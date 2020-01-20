#!/usr/bin/python3
""" Write a class MyList that inherits from list:
"""


class MyList(list):
    """Class definition"""
    def print_sorted(self):
        """Public instance method: def print_sorted(self):
        that prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
