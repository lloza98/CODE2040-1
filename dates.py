# A script for doing simple
# date arithmetic

import requests
import json
import datetime

from needle_in_haystack import  post_exercise
from prefix import get_json_obj
from registration import token, doubleCheck

# instance variables
get_url = 'http://challenge.code2040.org/api/dating'
post_url = 'http://challenge.code2040.org/api/dating/validate'

# Fetch JSON data and extract the needed values
jsonResponse = get_json_obj(token, get_url)
dateStamp = jsonResponse['datestamp']
intervalToAdd = jsonResponse['interval']

# transform the number of seconds we need to add to a timedelta
timeDelta = datetime.timedelta(seconds=intervalToAdd)

# parse the date and change it from ISO 8601 to a datetime
# object 
'''
dateFmt = 2016-09-11T14:21:43Z
'''
fmt = "%Y-%m-%dT%H:%M:%SZ"
datetimeObj = datetime.datetime.strptime(dateStamp, fmt)

# Add the timedelta to the datetime object
newDateTime = datetimeObj + timeDelta

# Change the result back to ISO 8601
def toISO(datetimeObj):
    return datetimeObj.isoformat()

# send it back to the server, adding the "z" to match the required format
post = post_exercise(toISO(newDateTime) + "Z", post_url, 'datestamp')

doubleCheck(post)
