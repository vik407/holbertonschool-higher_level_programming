#!/usr/bin/python3
def search_replace(my_list, search, replace):
    _my_list = []
    for m in my_list:
        if m == search:
            _my_list.append(replace)
        _my_list.append(m)
    return _my_list
