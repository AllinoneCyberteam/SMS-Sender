""" Steps to be done :
1. Create an account in FAST2SMS
2. Get your API in the DEV API section.
3. Copy that API in the authorization field.
4. Run the program and your are ready to go.
5. If you have not installed the requests library. Install it Using "pip install requests".
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 22:26:56 2019

@author: Akash
"""

import requests
 
url = "https://www.fast2sms.com/dev/bulk"

msg=input("Enter the message you want to send: ")                         
num=input("Enter the phone numbers you want to send, separated by a comma :")  # xxxxxxxxxx,xxxxxxxxxx
 
payload = "sender_id=FSTSMS&message={}&language=english&route=p&numbers={}".format(msg,num)
headers = {
 'authorization': "YOUR_API_KEY", #Copy your API Key here
 'Content-Type': "application/x-www-form-urlencoded",
 'Cache-Control': "no-cache",
 }
 
response = requests.request("POST", url, data=payload, headers=headers)
 
print(response.text)

