#!/bin/bash
# send a curl get request with a custom header attached
curl -s -X GET -H "X-School-User-Id: 98" -L $1
