#!/usr/bin/python3
for c in range(97, 123):
    if c not in [113, 101]:
        print("{:c}".format(c), end='')
