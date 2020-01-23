#!/usr/bin/python3
"""This is the main file for the base class
"""


class Base:
    """Base class for Holberton's 0x0C. Python - Almost a circle project
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
