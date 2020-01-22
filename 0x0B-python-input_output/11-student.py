#!/usr/bin/python3
"""11. Student to JSON
"""


class Student:
    """Write a class Student that defines a student
    """
    def __init__(self, first_name, last_name, age):
        """Set public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student
        """
        return self.__dict__
