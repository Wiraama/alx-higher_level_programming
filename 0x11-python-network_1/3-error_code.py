#!/usr/bin/python3
"""
takes in a URL
sends a request to the URL and displays the body of the response (decoded in utf-8).
"""

import sys
import urllib.request

if __name__ == '__main__':
    if sys.argv != 2:
        print('Usage: ./script <URL>')
        sys.exit(1)
    url = sys.argv[1]

    # decoding whats in url
    data = urllib.parse.urlencode({'url': url}).encode('utf-8')
    # sending request
    req = urllib.request.Request(data=data)

    try:
        with urllib.request.urlopen(url) as responce:
            content = reponce.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as error:
        print(error.reason)
