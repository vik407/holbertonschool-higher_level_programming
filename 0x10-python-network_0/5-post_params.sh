#!/bin/bash
# A Bash script that takes in a URL, sends a POST request to the passed URL,
# and displays the body of the response
SERVER=$1
curl -s -X POST -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD" "$SERVER"
