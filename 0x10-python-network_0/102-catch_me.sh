#!/bin/bash
# curl request that returns a message containaing a required string and displays body of response
curl -s -X PUT "0.0.0.0:5000/catch_me" -H "Origin: HolbertonSchool" -d "user_id=98" -L
