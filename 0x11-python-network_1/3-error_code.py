#!/usr/bin/python3
"""
Module 3-error_code
Takes in a URL, sends a request to the URL and displays the body of the response
(decoded in utf-8).
"""
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]
    
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
            print(content.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")

