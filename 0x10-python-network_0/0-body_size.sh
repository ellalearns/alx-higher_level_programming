#!/bin/bash
# uses curl to send request to a url and display size of the response body
curl -s -w "%{size_download}" -o /dev/null $1
