# This script JSON data made up of a string prefix and a collection
# of random strings. The program implements routines that create a 
# new collection made up of strings that do not start with the given
# string prefix

import requests
import json
from needle_in_haystack import get_exercise, post_exercise
from registration import token, doubleCheck

# instance variables
get_url = 'http://challenge.code2040.org/api/prefix'
post_url = 'http://challenge.code2040.org/api/prefix/validate'

# create the json object using the data send by the remote server
def get_json_obj(token, get_url):
    stringResponse = get_exercise(get_url, token).text
    return json.loads(stringResponse)

# Get the prefix and the string collection
jsonResponse = get_json_obj(token, get_url)
prefix = jsonResponse['prefix']
r_array  = jsonResponse['array']

# create a new collection made up of strings that do
# not start with prefix
def make_new_array(prefix, array):
    new_list = []
    for each in array:
        if not  each.startswith(prefix):
            new_list.append(each)
    return new_list

n_array = make_new_array(prefix, r_array)

post = post_exercise(n_array, post_url, 'array')
doubleCheck(post)
