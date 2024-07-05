#!/bin/bash
# Get the byte size of the HTTP response body for a given URL.

size=$(curl -sI "$1" | grep -i Content-Length | awk '{print $2}')

if [ -z "$size" ]; then
    :
else
    echo "$size"
fi

