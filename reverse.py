# A script to fetch a string from a remote
# server, reverse it, and send the result back


import requests
from registration import token, doubleCheck

# instance variables
get_url = 'http://challenge.code2040.org/api/reverse'
post_url = 'http://challenge.code2040.org/api/reverse/validate'

# fetch the data
objectToReverse = requests.post(get_url, data={'token' : token})

# Reverse the string
def reverse(string):
    return string[::-1]

# send the result back
reversedString = reverse(objectToReverse.text)
post = requests.post(post_url, data = {'token': token, 'string' : reversedString})

# check
doubleCheck(post)
