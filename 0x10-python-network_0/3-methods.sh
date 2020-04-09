#!/bin/bash
# Get the methods that the server permits
curl -sI -X OPTIONS "$1" | grep Allow | cut -d' ' -f1 --complement
