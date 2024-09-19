#!/usr/bin/python3
""" takes letter and sends a Post to url with letter as parameter """

import sys
import requests

if __name__ == "__main__":
    # get letter from command line
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    payload = {'q': q}

    res = requests.post('http://0.0.0.0:5000/search_user', data=payload)

    try:
        json_res = res.json()

        if json_res:
            print(f"[{json_res['id']}] {json_res['name']}")
        else:
            print("No results")
    except ValueError:
        print("Not a valid JSON")
