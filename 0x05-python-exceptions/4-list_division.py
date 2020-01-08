#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = list()
    for i in range(list_length):
        equals = 0
        try:
            equals = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("{}".format("out of range"))
        except ZeroDivisionError:
            print("{}".format("division by 0"))
        except TypeError:
            print("{}".format("wrong type"))
        finally:
            result.append(equals)
    return result
