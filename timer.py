import json, HTMLParser, sys, utils

def commands():
	commands = ['start', 'stop', 'current']
	return commands

def start(string):

	return urlString	

def stop():

	return urlString

def current():

	return urlString


def formatOutput(jsonObject):
	for task in jsonObject['task']:
		#print json.dumps(task, indent=4)
		print task['localid'] + " : " + HTMLParser.HTMLParser().unescape(task['summary']) + "\n\n"
	
def takeCare():
	try:
		requestedCommand = sys.argv[2]
	except Exception:
		requestedCommand = raw_input("Command ?\n")

	if requestedCommand == "start":
		try:
			taskLocalId = sys.argv[3]
		except:		
			searchStr = raw_input("Task id ?\n")

		urlString = start(str(taskLocalId))

	elif requestedCommand == "stop" :
		try:
			taskLocalId = sys.argv[3]
		except:
			taskLocalId = raw_input("Task id ?\n")

		urlString = details(taskLocalId)

	elif requestedCommand == "current" :
		try:
			personId = me.current()
			taskId = current(personId)
			print "Current task Id : " + str(taskId)
		except:
			personId = 0

	else:
		print "Invalid command"
		sys.exit(1)
	return urlString	
