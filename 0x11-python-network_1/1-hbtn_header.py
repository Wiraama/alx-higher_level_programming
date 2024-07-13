#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response
"""
import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: ./script <URL>')
        sys.exit(1)

    url = sys.argv[1]

    with urllib.request.urlopen(url) as responce:
        head = responce.getheaders()
        x_request_id = dict(head).get('X-Request-Id')

        if x_request_id:
            print(x_request_id)
