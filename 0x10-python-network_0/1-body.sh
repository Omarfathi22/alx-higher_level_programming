#!/bin/bash
# Script that takes in a URL, sends a GET request to the URL, and displays the body of the response

curl -s -X GET "$1" -o /tmp/body_response
if [[ $(head -n 1 /tmp/body_response | cut -d$' ' -f2) -eq 200 ]]; then
    cat /tmp/body_response
fi

