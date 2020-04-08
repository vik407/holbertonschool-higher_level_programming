#!/bin/bash
# A Bash script that takes in a URL, sends a GET request to the URL,
# and displays the body of the response
SERVER=$1
curl -s -L -X GET "$SERVER"
