#!/usr/bin/python3

"""Python script that takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header
"""

from requests import get
from sys import argv

if __name__ == "__main__":
    res = get(argv[1])
    print(res.headers.get('x-request-id'))
