#! /usr/bin/env python2.7
import urllib2, sys, re, base64, pdb, json

url = 'https://api.myintervals.com/task/'
user = '2nnztrtz0ue'
password = 'test'

taskId = input("Task id?\n")
url = url + '?localid=' + str(taskId)

print url

request = urllib2.Request(url)

base64string = base64.encodestring('%s:%s' % (user, password))[:-1]
authheader =  "Basic %s" % base64string
request.add_header("Authorization", authheader)
request.add_header("Accept", "application/json")

try:
	handle = urllib2.urlopen(request)
except IOError, e:                  # here we shouldn't fail if the username/password is right
	print "It looks like the username or password is wrong."
	print e
	sys.exit(1)

jsonObject = json.load(handle)

print json.dumps(jsonObject, indent=4)
handle.close()
