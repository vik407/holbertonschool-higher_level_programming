#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        result = fct(*args)
    except Exception as msg:
        print("Exception: {}".format(msg), file=stderr)
        result = None
    return result
