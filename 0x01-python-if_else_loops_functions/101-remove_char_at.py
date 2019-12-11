#!/usr/bin/python3
def remove_char_at(str, n):
    res = ''
    for a in str:
        if n:
            res += a
        n -= 1
    return (res)
