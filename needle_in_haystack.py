#
#
#
#
#

import requests
import json

token = '0756140fa1f238700cd260f5f813fab6'
get_url = 'http://challenge.code2040.org/api/haystack'
post_url = 'http://challenge.code2040.org/api/haystack/validate'

def get_exercise(get_url, token):
    return requests.post(get_url, data={'token': token})

stringResponse = get_exercise(get_url, token).text
jsonResponse = json.loads(stringResponse)
needle = jsonResponse['needle']
haystack = jsonResponse['haystack']

def search_haystack(needle, haystack):
    index = 0
    for each in haystack:
        if each == needle:
            return index
        index = index + 1
        
index = search_haystack(needle, haystack)

def post_exercise(post_val, url, data_name):
    return requests.post(url, json={'token' : token, data_name : post_val})

post_exercise(index, post_url, 'needle')