# Script for registering for the 
# 2016 CODE2040 technical challenge

import requests

#Instance variables
token = '0756140fa1f238700cd260f5f813fab6'
github = 'https://github.com/jlikhuva/CODE2040.git'

#JSON dictionary
payload = {
    'token' : token,
    'github' : github
}

#post
request = requests.post('http://challenge.code2040.org/api/register',  data=payload)

#check to see that all is okay
if request.status == 200:
    print "200 [OK]"
else:
    print request.text
