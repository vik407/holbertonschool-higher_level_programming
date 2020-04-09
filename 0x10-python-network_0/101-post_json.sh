#!/bin/bash
# Using POST send a json to validate
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
