#!/usr/bin/python3

if __name__ == '__main__':
    """ Required packages """
    import requests
    import sys
    """ Python script that takes your GitHub credentials """
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get('https://api.github.com/user', 
            auth=(username, password))
    data = response.json()
    print(data.get('id'))
