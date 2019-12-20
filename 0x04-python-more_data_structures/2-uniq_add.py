#!/usr/bin/python3
def uniq_add(my_list=[]):
    _history = []
    add = 0
    for m in my_list:
        if m not in _history:
            _history.append(m)
            add += m
    return add
