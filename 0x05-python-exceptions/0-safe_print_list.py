#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    lenght = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            lenght += 1
        print("")
    except IndexError:
        print("")
        pass
    return (lenght)
