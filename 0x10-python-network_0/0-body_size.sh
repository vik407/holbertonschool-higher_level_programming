#!/bin/bash
# a Bash script that show the Content-Lenght
curl -sI "$1" | grep Content-Length | cut -d' ' -f2
