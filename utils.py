import sys, base64, urllib2, json, getpass
from HTMLParser import HTMLParser

def initConnection():
    global user
    global password
    global url
    user = '2nnztrtz0ue'
    password = getpass.getpass("Password : ")
    url = 'https://api.myintervals.com/'

def startConnection(urlString):
    urlRequest = url + urlString
    request = urllib2.Request(urlRequest)

    authHeader = encodeHeader()

    request.add_header("Authorization", authHeader)
    request.add_header("Accept", "application/json")

    try:
        handle = urllib2.urlopen(request)
    except IOError, e:                  # here we shouldn't fail if the username/password is right
        print "It looks like the username or password is wrong."
        print e
        sys.exit(1)

    jsonObject = json.load(handle)
    handle.close()
    return jsonObject

def postConnection(urlString, data):
    urlRequest = url + urlString
    request = urllib2.Request(urlRequest)

    data = json.load(data)
    authHeader = encodeHeader()

    print json.dumps(data, indent=4)
    
    request.add_data(json.dumps(data))
    request.add_header("Authorization", authHeader)
    request.add_header("Accept", "application/json")

    try:
        handle = urllib2.urlopen(request)
    except IOError, e:
        print "It looks like the username or password is wrong"
        print e
        sys.exit(1)

    jsonObject = json.load(handle)
    handle.close()
    
def encodeHeader():
    base64string = base64.encodestring('%s:%s' % (user, password))[:-1]
    authheader =  "Basic %s" % base64string
    return authheader

def stripTags(html):
    s = PPStripper()
    s.feed(html)
    return s.get_data()

def formatOutput(jsonObject):
    print json.dumps(jsonObject, indent=4)
    
class PPStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

