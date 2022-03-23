#!/usr/bin/python3

if __name__ == '__main__':
    """ Required packages """
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    from sys import argv
    """ params """
    url = argv[1]
    email = {'email': argv[2]}

    data = urlencode(email).encode('utf-8')
    req = Request(url, data)
    """ Body """
    with urlopen(req) as response:
        print(response.read().decoded('utf-8'))
