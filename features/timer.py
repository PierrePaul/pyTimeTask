import json, sys, datetime, time, dateutil.parser, string, urllib2, requests
import utils, me, task

class Timer:
    requestedCommand = ''

    def commands(self):
        commands = [ 'current', 'current-id', 'pause']
        return  commands

    def start(self, personId, localTaskId):
        taskObject = task.Task()
        taskItem = json.loads(utils.getConnection(taskObject.details(localTaskId)))
        taskId = taskItem['task'][0]['id']

        time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
        infos = {'personid':personId, 'starttime':time, 'taskid':taskId}
        jsonObject = utils.postConnection('timer/', infos)
        urlString = self.current(personId)
        return urlString    

    def pause(self, personId):
        # calculate the amount of time lapsed between the starttime and now, and sum that value with the value in the time field (i.e. time = time + (now - starttime)). Then nullify the starttime field.
        taskObject = task.Task()
        taskLocalId = json.loads(utils.getConnection(self.current(personId)))
        timer = taskLocalId['timer'][0]
        
        startTime = timer['starttime'] 
        timer['starttime'] = None
        total = float(timer['time']) + (datetime.datetime.utcnow() - startTime)
        timer['time'] = total

        return None

    def stop(self):

        return urlString

    def current(self, personId):
        urlString = 'timer/?personid='+personId
        return urlString

    def formatOutput(self, jsonObject):
        requestedCommand = self.getRequestedCommand()
        for uniqueTimer in jsonObject['timer']:
            if uniqueTimer['isrunning'] == 't':
                if requestedCommand == 'current' or requestedCommand == 'start':
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
                taskLocalId = raw_input("Task id ?\n")
            
            personId = me.personId()
            urlString = self.start(personId, str(taskLocalId))
            
        elif requestedCommand == "stop":
            try:
                taskLocalId = sys.argv[3]
            except:
                taskLocalId = raw_input("Task id ?\n")
            urlString = self.stop(taskLocalId)

        elif requestedCommand == 'pause':
            personId = me.personId()
            self.pause(personId)
                
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
