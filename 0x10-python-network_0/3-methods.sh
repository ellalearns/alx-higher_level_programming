#!/bin/bash
# displays all the http methods a url's server will accept
curl -s -i -X OPTIONS $1 | grep -i allow
