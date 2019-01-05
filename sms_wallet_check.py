# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 22:26:56 2019

@author: akash
"""

import requests

url = "https://www.fast2sms.com/dev/wallet"

headers = {
    'authorization': "WVDprqN9LbCUE7B5TF1XSmMiZ3aOQYgjcsGowhedP2n86JltRIEaOpmglJ1A5cenuDK7jUTZ6qBWRxYQ",
    }

response = requests.request("POST", url, headers=headers)

print(response.text)