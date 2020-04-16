#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status
"""
from urllib import request


with request.urlopen("https://intranet.hbtn.io/status") as req:
    out = req.read()
    print("Body response:")
    print("\t- type: {}".format(type(out)))
    print("\t- content: {}".format(out))
    print("\t- utf8 content: {}".format(out.decode('utf-8')))
