#!/bin/bash
# script that takes in a URL as an argument, sends a GET request to the URL,
# and displays the body of the response
SERVER=$1
curl -s -X GET -H "X-HolbertonSchool-User-Id: 98" "$SERVER"
