import requests
import datetime
import time
import yagmail
import smtplib
import re
    
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0',
    'X-CSRFToken': 'b1pHtQ5crJLAT3smFP0epJXfY6vPmZUD',
    'Cookie': 'mid=YZIUAwALAAHIMaHw27iWm4uRNhXm; ig_did=267B8A84-7E4C-4AE8-8310-89537C6AE002; ig_nrcb=1; datr=ZWq4YgmzX9ZT1JWqg_JKOBhe; dpr=1.25; shbid="12194\05448282355544\0541699368636:01f7c66711afffb851018f96e728deca3575751a0c5325d0d7a0ae8c7df453849f159282"; shbts="1667832636\05448282355544\0541699368636:01f7d6dc489179654930f48f6e1bddd838831245ecd9a4320c9b73f128765bb21fb31322"; rur="EAG\05448282355544\0541699528482:01f7290a1947859b0750850000bcafbb9a501128ff5f8732265077b8dfeb30dafd938e78"; csrftoken=b1pHtQ5crJLAT3smFP0epJXfY6vPmZUD',
}
data = {
    "enc_password": "#PWD_INSTAGRAM_BROWSER:10:1666003782:AaJQAOvwCmxrRBoLgsRmdBAhmbryCB+vi4973MVF9d575edq0vUfARENK0QiqdtfIyuhzgGzSetL1yhBUvkIDUhugrkPpsXeeAgQM9IDGVRcAxivpqpgQJI7X5UrXHC2d9CRH5uvvkTdq4VM",
    "username": "speedmilo40@gmail.com",
    "queryParams": "{\"oneTapUsers\":\"[\\\"48282355544\\\"]\"}",
    "optIntoOneTap": "false",
    "stopDeletionNonce": "",
    "trustedDeviceRecords": "{}"
}
session = requests.session()
resp = session.post('https://www.instagram.com/accounts/login/ajax/', data=data, headers=headers)
print(resp.text)
