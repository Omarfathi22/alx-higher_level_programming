#!/bin/bash
# Script that sends a JSON POST request to a URL with contents from a file as the body, and displays the body of the response

curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
