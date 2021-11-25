import requests
#import sys

#param = sys.argv[1]

class API_Client():
    def __init__(self, header, key, param, url):
        self.header = header
        self.key = key
        self.param = param
        self.url = url

    def connect(self):

        headers = {
        self.header: self.key,
        'Accepts': 'application/json'
        }

        params = {
            'info': self.param
        }

        json = requests.get(self.url, params=params, headers=headers).json()

        return json