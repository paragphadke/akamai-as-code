import requests

import json

import sys

import requests

import pprint

import socket

from akamai.edgegrid import EdgeGridAuth

from urllib.parse import urljoin

print ("Executing Purge API")



authClientSecret = "t862zDj/FqqobleVpro9ZgM0qmOt7huwulCU0Wehm4A="
authHost = "akab-ucu66uwooabguvd3-d2cvnsrdudjhwzfz.purge.akamaiapis.net"
authAccessToken = "akab-rdxhp6z5vks2tsja-owdi4w6qiz2ucozy"
authClientToken = "akab-bephclbuuarg65h6-pmo6lbb2cug3uuql"

contentType = "application/json"

requestBodyJson = {"objects": ["http://new.test.com/assets/js/jquery-min.js"]}

cachePurgeApi = "/ccu/v3/delete/url/staging"

baseurl = "https://akab-ucu66uwooabguvd3-d2cvnsrdudjhwzfz.purge.akamaiapis.net"

s = requests.Session()

s.auth = EdgeGridAuth(

client_token=authClientToken,

client_secret=authClientSecret,

access_token=authAccessToken

)

jLoad = json.dumps(requestBodyJson)

print ("jLoad=" + jLoad)

headers = { 'Content-Type' : 'application/json'}

 

#get the propertyId

apiendpoint = cachePurgeApi

print ('trying api endpoint....' + apiendpoint)

posturl = urljoin(baseurl,apiendpoint)

print("Before sending post="+ posturl)

response = s.post(posturl, data=jLoad, headers = headers)

print ("RESPONSE=" + response.text)