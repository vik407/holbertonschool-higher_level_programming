#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

from requests import post
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    try:
        request = post("http://0.0.0.0:5000/search_user",
                       data={'q': q}).json()
        if "id" in request and "name" in request:
            print("[{}] {}".format(request["id"], request["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
