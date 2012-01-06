import json, HTMLParser, sys, datetime, time, dateutil.parser, string, urllib2
import utils, me

def commands():
    commands = [ 'current', 'current-id']
    return  commands

def start(string):

    return urlString	

def stop():

    return urlString

def current(personId):
    urlString = 'timer/?personid='+personId
    return urlString

def formatOutput(jsonObject):
    #print json.dumps(jsonObject, indent=4)
    requestedCommand = getRequestedCommand()
    for uniqueTimer in jsonObject['timer']:
        if uniqueTimer['isrunning'] == 't':
            if requestedCommand == 'current':
                now = datetime.datetime.utcnow()
                started = dateutil.parser.parse(uniqueTimer['starttime'], ignoretz=True)
                timeSpent = now - started
                
                timeSpent = str(timeSpent)
                timeSpent = string.split(timeSpent, '.')
                try:
                    print uniqueTimer['tasklocalid'] + ' : ' + HTMLParser.HTMLParser().unescape(uniqueTimer['task'])
                except:
                    print uniqueTimer['tasklocalid'] + ' : ' + HTMLParser.HTMLParser().unescape(uniqueTimer['task']).encode('ascii','replace') 
                #print uniqueTimer['tasklocalid'] + ' : ' + uniqueTimer['task']
                print "Been running for " + timeSpent[0]
                
            elif requestedCommand == 'current-id':
                print uniqueTimer['tasklocalid']
            
def takeCare():
    urlString  = ""
    requestedCommand = getRequestedCommand()
    
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
        
    elif requestedCommand == 'current-id':
        personId = me.personId()
        urlString = current(personId)
        
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
