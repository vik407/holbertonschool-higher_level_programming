#!/bin/bash
# Find the way to the correct response
# You are not coming from HolbertonSchool response
# You are not user_id=98 response
curl -s -L -H "Origin: HolbertonSchool" -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me
