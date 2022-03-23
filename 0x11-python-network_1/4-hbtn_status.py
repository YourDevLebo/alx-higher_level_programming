#!/usr/bin/python3

if __name__ == '__main__':
    """ Required packages """
    import requests
    """ requesting from url """
    req_data = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:\n\t- type: {}\n\t- content: {}"
            .format(type(req_data.text), req_data.text))
