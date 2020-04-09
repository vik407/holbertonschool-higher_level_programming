#!/bin/bash
# Using POST send a json to validate
SERVER=$1
FILE=$2
curl -s -X POST -H "Content-Type: application/json" -d @"$FILE" "$SERVER"
