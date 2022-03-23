#!/usr/bin/python3

if __name__ == '__main__':
    from urllib.request import urlopen
    from urllib.request import Request
    import urllib.error
    from sys import argv
    """ body """
    url = argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
