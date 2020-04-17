#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status
"""

from requests import get

if __name__ == "__main__":
    res = get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))
