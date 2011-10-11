#! /usr/bin/env python
import sys, utils
import task, timer

utils.initConnection()

try:
	action = sys.argv[1]
except Exception:
	action = raw_input("Type of commands available : task, timer\n")

if str(action) == "task":
	try:
		urlString = task.takeCare()
		jsonObject = utils.startConnection(urlString)
		task.formatOutput(jsonObject)
	except Exception, e:
		print e
		sys.exit(1)

elif action == "timer":
	urlString = timer.takeCare()
	jsonObject = utils.startConnection(urlString)
	timer.formatOutput(jsonObject)	
	sys.exit(1)


