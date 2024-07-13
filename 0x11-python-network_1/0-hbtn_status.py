#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status"""


if __name__=="__main__":
    import urllib.request

    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        reply = response.read().decode('utf-8')
        print('Body response')
        print(f"\t- type: {type(reply)}")
        print(f"\t- content: {reply}")
        print(f"\t- utf8 content: {reply}")
