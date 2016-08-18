#
#
#
#
#
#

import requests
import json
from needle_in_haystack import get_exercise

token = '0756140fa1f238700cd260f5f813fab6'
get_url = 'http://challenge.code2040.org/api/prefix'
post_url = 'http://challenge.code2040.org/api/prefix/validate'

def get_json_obj(token, get_url):
    stringResponse = get_exercise(get_url, token).text
    return json.loads(stringResponse)

jsonResponse = get_json_obj(token, get_url)

print jsonResponse

prefix = jsonResponse['prefix']
r_array  = jsonResponse['array']

'''
print prefix
print r_array
'''

def make_new_array(prefix, array):
    new_list = []
    for each in array:
        if not  each.startswith(prefix):
            new_list.append(each)
    return new_list


n_array = make_new_array(prefix, r_array)
#print n_array

data = {
    'token' : token,
    'array': n_array
    }

def post():
    return requests.post(post_url, json=data)

r = post()
print r.status_code
print r.text
