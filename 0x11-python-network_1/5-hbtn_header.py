#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays the value of the variable
X-Request-Id in the response header
"""
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: ./script <URL>')
        sys.exit(1)

    url = sys.argv[1]

    try:
        response = requests.get(url)
        x_response_id = response.headers.get('X-Request-Id')

        if x_response_id:
            print(x_response_id)

    except requests.RequestException as error:
        print('error encountered'.format(error))
