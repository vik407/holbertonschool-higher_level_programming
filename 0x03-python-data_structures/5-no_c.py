#!/usr/bin/python3
def no_c(my_string):
    _my_string = ""
    for each_c in my_string:
        if each_c in ['c', 'C']:
            continue
        else:
            _my_string += each_c
    return _my_string
