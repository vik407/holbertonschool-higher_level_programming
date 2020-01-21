#!/usr/bin/python3
"""3. Write to a file
"""


def write_file(filename="", text=""):
    """Write a function that writes a string to a text file (UTF8)
    and returns the number of characters written.
    """
    with open(filename, 'w') as file:
        file_write = file.write(text)
    return file_write
