#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    _my_list = my_list.copy()
    if (0 <= idx < len(my_list)):
        _my_list[idx] = element
    return(_my_list)
