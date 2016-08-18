#
#
#
#
#

import requests
import json
import datetime

from needle_in_haystack import  post_exercise
from prefix import get_json_obj

token = '0756140fa1f238700cd260f5f813fab6'
get_url = 'http://challenge.code2040.org/api/dating'
post_url = 'http://challenge.code2040.org/api/dating/validate'

jsonResponse = get_json_obj(token, get_url)
dateStamp = jsonResponse['datestamp']
intervalToAdd = jsonResponse['interval']

timeDelta = datetime.timedelta(seconds=intervalToAdd)

'''
dateFmt = 2016-09-11T14:21:43Z
'''
fmt = "%Y-%m-%dT%H:%M:%SZ"
datetimeObj = datetime.datetime.strptime(dateStamp, fmt)

'''
print timeDelta
print datetimeObj
'''
newDateTime = datetimeObj + timeDelta
print newDateTime

def toISO(datetimeObj):
    return datetimeObj.isoformat()

print toISO(newDateTime) 

post = post_exercise(toISO(newDateTime) + "Z", post_url, 'datestamp')
print post.status_code
print post.text
