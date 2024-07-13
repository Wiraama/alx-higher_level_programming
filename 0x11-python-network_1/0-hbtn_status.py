#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status"""


if __name__=="__main__":
    import urllib.request

    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        reply = response.read()
        print('Body response:')
        print("\t- type: {}".format(type(reply)))
        print("\t- content: {}".format(reply))
        print("\t- utf8 content: {}".format(reply.decode('utf-8')))
