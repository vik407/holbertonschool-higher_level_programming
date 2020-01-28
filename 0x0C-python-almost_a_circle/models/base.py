#!/usr/bin/python3
"""This is the main file for the base class
"""
import json
import csv
import os.path


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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file
        """
        if type(list_objs) != list and list_objs is not None:
            raise TypeError("list_objs must be a list")
        if list_objs is None or list_objs == []:
            output = []
        else:
            first = type(list_objs[0])
            if any(type(s) != first for s in list_objs):
                raise ValueError("all elements of list_objs must match")
            output = [c.to_dictionary() for c in list_objs]
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(output))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string:
        """
        if json_string is None or json_string == "":
            return []
        if type(json_string) != str:
            raise TypeError("json_string must be a string")
        loads = json.loads(json_string)
        for d in loads:
            if type(d) != dict:
                raise ValueError("json_string must contain dictionaries")
        return loads

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.
        """
        insta = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        insta.update(**dictionary)
        return insta

    @classmethod
    def load_from_file(cls):
        """returns a list of instances
        """
        filename = str(cls).split(".")[-1][:-2] + ".json"
        if not os.path.exists(filename):
            return []
        res = []
        with open(filename, "r") as file:
            dicts = cls.from_json_string(file.readline())
        for d in dicts:
            res.append(cls.create(**d))
        return res

    @classmethod
    def load_from_file_csv(cls):
        """Serializes and deserializes in CSV"""
        filename = cls.__name__ + ".csv"
        rectangle_head = ["id", "width", "height", "x", "y"]
        square_head = ["id", "size", "x", "y"]
        head = rectangle_head if cls.__name__ == "Rectangle" else square_head
        res = []
        if os.path.exists(filename):
            with open(filename, "r") as f:
                reader = csv.reader(f, delimiter=',')
                for i, row in enumerate(reader):
                    if i > 0:
                        new = cls(1, 1)
                        for j, e in enumerate(row):
                            if e:
                                setattr(new, head[j], int(e))
                        res.append(new)
        return res
