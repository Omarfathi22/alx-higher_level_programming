#!/bin/bash
# This script takes in a URL (including protocol), sends a request to that URL, and displays the size of the body of the response
# Get the byte size of the HTTP response header for a given URL.
curl -s "$1" | wc -c
