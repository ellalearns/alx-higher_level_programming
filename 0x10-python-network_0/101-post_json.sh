#!/bin/bash
# sends curl post json request with data from file and displays response body
curl -s -X POST -H "Content-Type: application/json" $1 -d $2 -L
