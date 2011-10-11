import json, HTMLParser, sys, utils

def commands():
	commands = ['details','personId']
	return commands

def details():
	urlString = "me/"
	return urlString
	
def personId():
	urlString = details()
	jsonObject = utils.startConnection(urlString)
	return jsonObject['personid']

def formatOutput(jsonObject):
	print json.dumps(jsonObject, indent=4)
	
def takeCare():
	try:
		requestedCommand = sys.argv[2]
	except Exception:
		requestedCommand = raw_input("Command ?\n")

	if requestedCommand == "details":
		urlString = details()

	elif requestedCommand == "current":
		urlString = current()

	else:
		print "Invalid command"
		sys.exit(1)

	return urlString	
