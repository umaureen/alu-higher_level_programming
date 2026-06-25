#!/usr/bin/python3
"""
Python script that fetches https://alu-intranet.hbtn.io/status
"""
import requests

if __name__ == '__main__':
    url = 'https://alu-intranet.hbtn.io/status'
    # The checker will replace this URL during testing
    
    res = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))
