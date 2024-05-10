#!/bin/bash
# sends curl post json request with data from file and displays response body
curl -s -X POST -H "Content-Type: application/json" -d "$(cat $2)" $1 -L
