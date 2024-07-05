#!/bin/bash
# Script that takes in a URL, sends a GET request to the URL, and displays the body of the response for a 200 status code
# Get the response body for a given URL for 200 status code responses.
curl -sL "$1"
