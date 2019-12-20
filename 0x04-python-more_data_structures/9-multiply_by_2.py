#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    _a_dictionary = {}
    for key in a_dictionary:
        _a_dictionary[key] = a_dictionary[key] * 2
    return a_dictionary
