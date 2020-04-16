#!/usr/bin/python3
""" Python script that takes in a URL, sends a request and get X-Request-Id var
"""
from urllib import request
from sys import argv


with request.urlopen(argv[1]) as req:
    print(req.headers.get('X-Request-Id'))
