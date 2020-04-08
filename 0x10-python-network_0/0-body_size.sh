#!/bin/bash
# a Bash script that takes in a URL, sends a request to that URL, and displays
# the size of the body of the response
SERVER=$1
curl -sI "$SERVER" | grep Content-Length | cut -d' ' -f2
