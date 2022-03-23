#!/usr/bin/python3

if __name__ == '__main__':
    """ Required packages """
    import requests
    from sys import argv
    """ displays the value of x-request-Id """
    req_data = requests.get(argv[1])
    print(req_data.headers.get('X-Request-Id'))
