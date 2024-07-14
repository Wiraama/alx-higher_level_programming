#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
"""

import urllib.request
import urllib.parse
import sys


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('usage: ./script <URL>  <email>')
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    #decode information in email
    data = urllib.parse.urlencode({'email':email}).encode('utf-8')

    #requesting data
    req = urllib.request.Request(url, data=data)

    try:
        with urllib.request.urlopen(req) as res:
            content = res.read().decode('utf-8')
            print(content)
    except urllib.error.URLError as error:
        print(error.reason)
