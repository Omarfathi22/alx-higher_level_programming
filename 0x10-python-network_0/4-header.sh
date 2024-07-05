#!/bin/bash
# Script that takes in a URL, sends a GET request with a specific header, and displays the body of the response
curl -sH "X-HolbertonSchool-User-Id: 98" "${1}"
