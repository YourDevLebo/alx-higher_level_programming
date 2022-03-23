#!/usr/bin/python3

if __name__ == '__main__':
    """ Required package """
    import urllib.request
    """ Fetching URL as reponse """
    with urllib.request.urlopen(
         'https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        utf8 = html.decode('utf-8')
        print("Body response: \n\t- type: {}".format(type(html)))
        print("\t- content: {}\n\t- utf8 content: {}".format(
            html, utf8, end=""))
