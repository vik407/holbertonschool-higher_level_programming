#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    big_number = my_list[0]
    for each_number in my_list:
        if each_number > big_number:
            big_number = each_number
    return big_number
