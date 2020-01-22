#!/usr/bin/python3
"""8. Create object from a JSON file
"""
import json


def load_from_json_file(filename):
    """Write a function that creates an Object from a “JSON file”:
    """
    with open(filename, 'r') as file:
        file_read = json.load(file)
    return file_read
