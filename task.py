import json, parse, sys, utils
class Task:
    requestedCommand = '';

    def commands(self):
        commands = ['search', 'commands', 'details']
        return commands

    def search(self, string):
        urlString = "task/search=" + str(string)
        return urlString

    def details(self, taskId):
        urlString = "task/?localid=" + str(int(taskId))
        return urlString

    def formatOutput(self, jsonObject):
        for task in jsonObject['task']:
            #print json.dumps(task, indent=4)
            try:
                print task['localid'] + " : " + parse.stripTags(task['summary']) + "\n\n"
            except:
                print task['localid'] + " : " + parse.stripTags(task['summary']).encode('ascii', 'replace') + "\n\n"
        
    def takeCare(self):
        requestedCommand = self.getRequestedCommand()
        if requestedCommand == "search":
            try:
                searchStr = sys.argv[3]
            except:
                searchStr = raw_input("Searching for ?\n")

            urlString = self.search(str(searchStr))

        elif requestedCommand == "details" :
            try:
                taskLocalId = sys.argv[3]
            except:
                taskLocalId = raw_input("Task id ?\n")

            urlString = self.details(taskLocalId)

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
