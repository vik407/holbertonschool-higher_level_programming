#!/usr/bin/python3
def safe_print_division(a, b):
    equals = None
    try:
        equals = a / b
    except:
        pass
    finally:
        if equals is not None:
            print("Inside result: {:.1f}".format(equals))
        else:
            print("Inside result: None")
    return equals
