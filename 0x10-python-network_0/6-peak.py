#!/usr/bin/python3
"""Write a function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """Finds a peak in a list of integers"""
    if not list_of_integers:
        return None
    mid = int(len(list_of_integers) / 2)
    start = 0
    end = len(list_of_integers) - 1
    while mid > start and mid < end:
        if list_of_integers[mid - 1] > list_of_integers[mid]:
            end = mid
            mid = int(mid/2)
            continue
        if list_of_integers[mid + 1] > list_of_integers[mid]:
            start = mid
            mid = int((end + mid)/2)
            continue
        else:
            break
    return list_of_integers[mid]
