#!/usr/bin/python3
for n in range(0, 99):
    if n < 98:
        print("{:02d}, ".format(n), end='')
    else:
        print("99")
