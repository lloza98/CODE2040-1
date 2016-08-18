# String searching. This script gets
# json data consisting of a 'needle' string to search
# for and a collection of strings. It them does a simple
# linear search for the string in the collection, then posts
# the index at which the string occurs.

import requests
import json
from registration import token, doubleCheck

# instance variables
get_url = 'http://challenge.code2040.org/api/haystack'
post_url = 'http://challenge.code2040.org/api/haystack/validate'

# Fetches the json data from the remote server
def get_exercise(get_url, token):
    return requests.post(get_url, data={'token': token})

# Get the text of the request object and turn it
# into a json dictionary
stringResponse = get_exercise(get_url, token).text
jsonResponse = json.loads(stringResponse)

# Extract the values from the dictionary
needle = jsonResponse['needle']
haystack = jsonResponse['haystack']

# A simple linear search
def search_haystack(needle, haystack):
    index = 0
    for each in haystack:
        if each == needle:
            return index
        index = index + 1
    return -1

# Post the information back to the remote server
index = search_haystack(needle, haystack)
def post_exercise(post_val, url, data_name):
    return requests.post(url, json={'token' : token, data_name : post_val})

post = post_exercise(index, post_url, 'needle')

# see to it that all is well
doubleCheck(post)
