import json, HTMLParser, sys, utils

def commands():
    commands = ['search', 'commands', 'details']
    return commands

def search(string):
    urlString = "task/search=" + str(string)
    return urlString

def details(taskId):
    urlString = "task/?localid=" + str(int(taskId))
    return urlString

def formatOutput(jsonObject):
    for task in jsonObject['task']:
        #print json.dumps(task, indent=4)
        print task['localid'] + " : " + HTMLParser.HTMLParser().unescape(task['summary']) + "\n\n"
    
def takeCare():
    requestedCommand = getRequestedCommand()
    if requestedCommand == "search":
        try:
            searchStr = sys.argv[3]
        except:     
            searchStr = raw_input("Searching for ?\n")

        urlString = search(str(searchStr))

    elif requestedCommand == "details" :
        try:
            taskLocalId = sys.argv[3]
        except:
            taskLocalId = raw_input("Task id ?\n")

        urlString = details(taskLocalId)

    else:
        print "Invalid command"
        sys.exit(1)
    return urlString    

def getRequestedCommand():
    try:
        requestedCommand = sys.argv[2]
    except Exception:
        print "Available commands : "
        print commands()
        requestedCommand = raw_input("Command ?\n")
    return requestedCommand
