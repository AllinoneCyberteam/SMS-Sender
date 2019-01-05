
import requests
 
url = "https://www.fast2sms.com/dev/bulk"

msg=input("Enter the message you want to send: ")
num=input("Enter the phone numbers you want to send, separated by a comma :")
 
payload = "sender_id=FSTSMS&message={}&language=english&route=p&numbers={}".format(msg,num)
headers = {
 'authorization': "WVDprqN9LbCUE7B5TF1XSmMiZ3aOQYgjcsGowhedP2n86JltRIEaOpmglJ1A5cenuDK7jUTZ6qBWRxYQ",
 'Content-Type': "application/x-www-form-urlencoded",
 'Cache-Control': "no-cache",
 }
 
response = requests.request("POST", url, data=payload, headers=headers)
 
print(response.text)

