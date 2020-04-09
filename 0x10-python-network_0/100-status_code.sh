#!/bin/bash
# 100 status code task from received server call
curl -s -L -I "$1" -o /dev/null -w '%{http_code}'
