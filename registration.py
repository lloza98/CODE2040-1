#
#
#

import requests

payload = { 'token' : '0756140fa1f238700cd260f5f813fab6', 'github' : 'https://github.com/jlikhuva/CODE2040.git'}

request = requests.post('http://challenge.code2040.org/api/register',  data=payload)
