#!/bin/bash
# Find the way to the correct response
curl -s -L -H "Origin: HolbertonSchool" -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me
