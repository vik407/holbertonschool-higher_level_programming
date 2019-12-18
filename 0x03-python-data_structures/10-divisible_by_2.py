#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    _my_list = []
    for each_number in my_list:
        if not each_number % 2:
                _my_list.append(True)
        else:
                _my_list.append(False)
    return _my_list
