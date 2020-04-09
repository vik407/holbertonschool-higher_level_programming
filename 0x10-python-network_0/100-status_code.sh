#!/bin/bash
# 100 status code task from received server call
SERVER=$1
curl -s -L -I "$SERVER" -o /dev/null -w '%{http_code}'
