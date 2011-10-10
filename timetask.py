#! /usr/bin/env python2.7
import sys, getpass, utils
import task, timer

user = '2nnztrtz0ue'
password = getpass.getpass("Password : ")

try:
	action = sys.argv[1]
except Exception:
	action = raw_input("Type of commands available : task\n")

if str(action) == "task":
	try:
		urlString = task.takeCare()
		jsonObject = utils.startConnection(urlString, user, password)
		task.formatOutput(jsonObject)
	except Exception, e:
		print e
		sys.exit(1)
elif action == "timer":
	urlString = timer.takeCare()
	
	sys.exit(1)
 

