#!/bin/bash
# Sends a DELETE request to the URL passed and displays the body of the response
SERVER=$1
curl -s -X DELETE "$SERVER"
