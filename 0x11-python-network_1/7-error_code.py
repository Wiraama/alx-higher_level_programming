#!/usr/bin/python3
"""takes url sends request to url and display body """

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: <script> url")
        sys.exit(1)

    res = requests.get(sys.argv[1])

    if res.status_code >= 400:
        print(f'Error code:{res.status_code}')
    else:
        print(res.text)
