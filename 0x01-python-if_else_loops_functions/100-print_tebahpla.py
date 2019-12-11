#!/usr/bin/python3
for a in range(122, 96, -1):
    offset = 0
    if a % 2:
        offset = 32
    print("{:s}".format(chr(a - offset)), end='')
