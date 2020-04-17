#!/usr/bin/python3
"""Python script that takes 2 valuments in order to solve this challenge
Number of contributions per user and commit
"""

from requests import get
from sys import argv

if __name__ == "__main__":
    json = get("https://api.github.com/repos/{}/{}/commits".
               format(argv[2], argv[1])).json()
    contrib = 0
    for val in json:
        contrib += 1
        name = val.get("commit").get("author").get("name")
        sha = val.get("sha")
        print("{}: {}".format(sha, name))
        if contrib == 10:
            break
