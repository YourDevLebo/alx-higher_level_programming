#!/usr/bin/python3

if __name__ == '__main__':
    """ Required packages """
    import requests
    from sys import argv
    res = requests.get(argv[1])
    """ condition to check if status is true or not """
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
