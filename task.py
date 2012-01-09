import json, parse, sys, utils
requestedCommand = '';

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
        try:
            print task['localid'] + " : " + parse.stripTags(task['summary']) + "\n\n"
        except:
            print task['localid'] + " : " + parse.stripTags(task['summary']).encode('ascii', 'replace') + "\n\n"
    
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
    global requestedCommand
    if requestedCommand == '':
        try:
            requestedCommand = sys.argv[2]
        except Exception:
            print "Available commands : "
            print commands()
            requestedCommand = raw_input("Command ?\n")

    return requestedCommand
