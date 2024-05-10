#!/bin/bash
# curl request that returns a message containaing a required string and displays body of response
curl -s "0.0.0.0:5000/catch_me" -L
