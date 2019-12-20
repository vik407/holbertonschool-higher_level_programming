#!/usr/bin/python3
def uniq_add(my_list=[]):
    _my_list = []
    _history = []
    _m = 0
    for m in my_list:
        if m not in _history:
            _history.append(m)
            _m += m
    return _m
