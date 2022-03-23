#!/usr/bin/python3

if __name__ == '__main__':
    """ Required packages """
    from urllib.request import urlopen
    from sys import argv
    """ Body: must return x_request-Id """
    with urlopen(argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
