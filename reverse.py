#
#
#
#

import requests

token = '0756140fa1f238700cd260f5f813fab6'

r = requests.post('http://challenge.code2040.org/api/reverse', data={'token' : token})
'''
print r.status_code
print r.text
'''
def reverse(string):
    return string[::-1]


reversedString = reverse(r.text)

requests.post('http://challenge.code2040.org/api/reverse/validate', data = {'token': token, 'string' : reversedString})

