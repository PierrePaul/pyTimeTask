import json, sys, datetime, time, dateutil.parser, string, urllib2
import utils, me
class Timer:
    requestedCommand = ''

    def commands(self):
        commands = [ 'current', 'current-id']
        return  commands

    def start(self, string):
        return urlString	

    def stop(self):
        return urlString

    def current(self, personId):
        urlString = 'timer/?personid='+personId
        return urlString

    def formatOutput(self, jsonObject):
        requestedCommand = self.getRequestedCommand()
        for uniqueTimer in jsonObject['timer']:
            if uniqueTimer['isrunning'] == 't':
                if requestedCommand == 'current':
                    now = datetime.datetime.utcnow()
                    started = dateutil.parser.parse(uniqueTimer['starttime'], ignoretz=True)
                    timeSpent = now - started
                    
                    timeSpent = str(timeSpent)
                    timeSpent = string.split(timeSpent, '.')
                    try:
                        print uniqueTimer['tasklocalid'] + ' : ' + utils.stripTags(uniqueTimer['task'])
                    except:
                        print uniqueTimer['tasklocalid'] + ' : ' + utils.stripTags(uniqueTimer['task']).encode('ascii','replace') 
                    #print uniqueTimer['tasklocalid'] + ' : ' + uniqueTimer['task']
                    print "Been running for " + timeSpent[0]
                    
                elif requestedCommand == 'current-id':
                    print uniqueTimer['tasklocalid']
                
    def takeCare(self):
        urlString  = ""
        requestedCommand = self.getRequestedCommand()
        
        if requestedCommand == "start":
            try:
                taskLocalId = sys.argv[3]
            except:
                searchStr = raw_input("Task id ?\n")
            
            urlString = self.start(str(taskLocalId))
            
        elif requestedCommand == "stop":
            try:
                taskLocalId = sys.argv[3]
            except:
                taskLocalId = raw_input("Task id ?\n")
            urlString = self.stop(taskLocalId)

        elif requestedCommand == 'pause':
            try:
                self.pause()
                
            
        elif requestedCommand == "current":
            personId = me.personId()
            urlString = self.current(personId)
            
        elif requestedCommand == 'current-id':
            personId = me.personId()
            urlString = self.current(personId)
            
        else:
            print "Invalid command"
            sys.exit(1)
        return urlString

    def getRequestedCommand(self):
        if self.requestedCommand == '':
            try:
                self.requestedCommand = sys.argv[2]	
            except Exception:
                print "Available commands : "
                print self.commands()
                self.requestedCommand = raw_input("Command ?\n")
            
        return self.requestedCommand
