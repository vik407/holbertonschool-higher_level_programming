#!/usr/bin/python3
"""This is the main file for the base class
"""
import json


class Base:
    """Base class for Holberton's 0x0C. Python - Almost a circle project
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if type(list_dictionaries) != list:
            raise TypeError("list_dictionaries must be a list")
        if any(type(s) != dict for s in list_dictionaries):
            raise TypeError("list_dictionaries must contain dictionaries")
        return json.dumps(list_dictionaries)
