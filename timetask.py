#! /usr/bin/env python
import sys, utils

utils.initConnection()

try:
    action = sys.argv[1]

except Exception:
    action = raw_input("Type of commands available : task, timer\n")

try:
    actionClassName = action[0].capitalize() + action[1:]
    action = "features."+str(action)
    actionClass = __import__(action, fromlist=[actionClassName])
    actionDef = getattr(actionClass, actionClassName)
    actionObject = actionDef()

except Exception, e:
    print "Invalid command"

try:
    urlString = actionObject.takeCare()
    jsonObject = utils.startConnection(urlString)
    actionObject.formatOutput(jsonObject)
except Exception, e:
    print e
    sys.exit(1)



