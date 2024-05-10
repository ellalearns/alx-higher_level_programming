#!/bin/bash
# sends curl request and displays only the status code of response
curl -s -w "%{http_code}" -o /dev/null $1
