#!/usr/bin/python3

if __name__ == '__main__':
    """ Required packages """
    import requests
    from sys import argv
    """ trail and error """
    try:
        q = argv[1]
    except:
        q = ''
        url = 'http://0.0.0.0:5000/search_user'
        payload = {'q': q}
        r = requests.post(url, payload)
    try:
        json = r.json()
        if len(json) == 0:
            print('No result')
        else:
            json_id = json.get('id')
            json_name = json.get('name')
            print('[{}] {}'.format(json_id, json_name))
    except:
            print('Not a valid JSON')
