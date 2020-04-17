#!/usr/bin/python3
"""Python script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""

from requests import get
from sys import argv

if __name__ == "__main__":
    req = get("https://api.github.com/user",
              auth=(argv[1], argv[2])).json()
    try:
        print(req["id"])
    except:
        print(None)
