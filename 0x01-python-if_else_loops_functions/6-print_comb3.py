#!/usr/bin/python3
for a in range(0, 9):
    for b in range(0, 10):
        res = int(str(a) + str(b))
        if res < 89:
            print("{:02d}, ".format(res), end='')
print("{:d}".format(89))
