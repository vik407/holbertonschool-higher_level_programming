#!/usr/bin/python3
"""Write a function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """Function to find a peak"""
    if not list_of_integers:
        return None
    return _find(list_of_integers, 0, len(list_of_integers) - 1,
                 len(list_of_integers))


def _find(arr, low, high, n):
    """Helper func _find"""
    mid = low + (high - low)//2

    if (mid == 0 or arr[mid - 1] <= arr[mid]) and\
       (mid == n - 1 or arr[mid + 1] <= arr[mid]):
        return arr[mid]
    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return _find(arr, low, mid - 1, n)
    else:
        return _find(arr, mid + 1, high, n)
