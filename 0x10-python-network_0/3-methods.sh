#!/bin/bash
# displays all the http methods a url's server will accept
curl -s -X HEAD $1 -D headers.txt
