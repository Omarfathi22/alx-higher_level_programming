#!/usr/bin/python3
"""
Module 1-hbtn_header
Takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        print(headers.get('X-Request-Id'))
