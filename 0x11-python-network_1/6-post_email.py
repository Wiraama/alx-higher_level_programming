#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the
"""
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
import sys
import requests
if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    res = requests.post(url, data=payload)

    print(res.text)
