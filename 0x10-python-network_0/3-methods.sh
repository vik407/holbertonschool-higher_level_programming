#!/bin/bash
# Get the methods that the server permits
SERVER=$1
curl -sI -X OPTIONS "$SERVER" | grep Allow | cut -d' ' -f1 --complement
