#!/usr/bin/python3
"""2. Read n lines
"""


def read_lines(filename="", nb_lines=0):
    """Write a function that reads n lines of a text file (UTF8) and prints
    it to stdout:
    """
    len_file = len(open(filename).readlines())
    with open(filename, 'r') as file:
        if nb_lines > 0 and nb_lines < len_file:
            while nb_lines:
                print(file.readline(), end="")
                nb_lines -= 1
        else:
            file_content = file.read()
            print(file_content, end="")
