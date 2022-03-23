#!/usr/bin/python3

if __name__ == '__main__':
    """ Required packages """
    import requests
    from sys import argv
    """ display email """
    data_mail = {'email': argv[2]}
    response = requests.post(argv[1], data=data_mail)
    print(response.text)
