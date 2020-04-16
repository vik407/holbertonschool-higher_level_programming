#!/usr/bin/python3
""" Python script that takes in a URL, sends a request and get X-Request-Id var
"""

from urllib import request
from sys import argv

if __name__ == "__main__":
    with request.urlopen(argv[1]) as res:
        print(res.getheader("X-Request-Id"))
