#!/bin/bash
# sends a curl post request and displays the response
curl -s -X POST $1 -H "Content-Type: multipart/form-data" -F "email=test@gmail.com" -F "subject=I will always be here for PLD" -L
