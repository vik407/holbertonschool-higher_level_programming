#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    keys = list(a_dictionary.keys())
    big_key = keys[0]
    for num in keys:
        if a_dictionary[num] > a_dictionary[big_key]:
            big_key = num
        else:
            big_key
    return big_key
