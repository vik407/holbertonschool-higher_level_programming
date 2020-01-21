#!/usr/bin/python3
"""4. Append to a file
"""


def append_write(filename="", text=""):
    """Write a function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added:
    """
    with open(filename, 'a') as file:
        file_write = file.write(text)
    return file_write
