#!/usr/bin/python3
"""13. Student to disk and reload
"""


class Student:
    """Write a class Student that defines a student
    """
    def __init__(self, first_name, last_name, age):
        """Set public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student
        """
        if attrs is not None and all(isinstance(item, str) for item in attrs):
            json_obj = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    json_obj[key] = value
            return json_obj
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
        """
        for key, value in json.items():
            self.__dict__[key] = value
