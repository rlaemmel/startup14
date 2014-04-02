#
# (C) Ralf Laemmel, 2014
#
# Some commons to access Polls App API
#

import urllib2
import json

# Common URL prefix for API 
api = "http://rlaemmel.pythonanywhere.com/api/"

#
# HTTP GET
#
# http://stackoverflow.com/questions/645312/what-is-the-quickest-way-to-http-get-in-python
#

def get(url):
    string_response = urllib2.urlopen(api+url).read()
    dict_response = json.loads(string_response)
    return dict_response

#
# HTTP POST
#
# http://stackoverflow.com/questions/3290522/urllib2-and-json
#

def post(url, content):
    data = json.dumps(content)
    req = urllib2.Request(api+url, data, {'Content-Type': 'application/json'})
    f = urllib2.urlopen(req)
    string_response = f.read()
    f.close()
    dict_response = json.loads(string_response)
    return dict_response
