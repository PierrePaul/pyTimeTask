import json, HTMLParser, sys, datetime, time, dateutil.parser, string
import utils, me

def commands():
	commands = ['start', 'stop', 'current']
	return commands

def start(string):

	return urlString	

def stop():

	return urlString

def current(personId):
	urlString = 'timer/?personid='+personId
	return urlString


def formatOutput(jsonObject):
	#print json.dumps(jsonObject, indent=4)
	for uniqueTimer in jsonObject['timer']:
		if uniqueTimer['isrunning'] == 't':
			now = datetime.datetime.utcnow()
			started = dateutil.parser.parse(uniqueTimer['starttime'], ignoretz=True)
			timeSpent = now - started
			
			timeSpent = str(timeSpent)
			timeSpent = string.split(timeSpent, '.')
			print uniqueTimer['tasklocalid'] + ' : ' + HTMLParser.HTMLParser().unescape(uniqueTimer['task'])
			print "Been running for " + timeSpent[0]
	
def takeCare():
	urlString = ""
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

	elif requestedCommand == "stop":
		try:
			taskLocalId = sys.argv[3]
		except:
			taskLocalId = raw_input("Task id ?\n")

		urlString = details(taskLocalId)

	elif requestedCommand == "current":
		personId = me.personId()
		urlString = current(personId)

	else:
		print "Invalid command"
		sys.exit(1)
	return urlString	
