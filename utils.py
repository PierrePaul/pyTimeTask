import sys, base64, urllib2, json, getpass, requests
from requests.auth import HTTPBasicAuth
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
    #formatOutput(urlRequest)
    request = urllib2.Request(urlRequest)

    authHeader = encodeHeader()

    request.add_header('Authorization', authHeader)
    request.add_header('Accept', 'application/json')

    try:
        handle = urllib2.urlopen(request)
    except IOError, e:                  # here we shouldn't fail if the username/password is right
        print "It looks like the username or password is wrong."
        print e
        sys.exit(1)

    jsonObject = json.load(handle)
    handle.close()
    return jsonObject

def getConnection(urlString):
    urlRequest = url + urlString
    try:
        request = requests.get(urlRequest, auth=(user,password))
    except IOError, e:
        print e
        sys.exit(1)

    return request.text

def postConnection(urlString, infos):
    urlRequest = url + urlString
    headers = {'content-type':'application/json'}

    try:
        request = requests.post(urlRequest, data=json.dumps(infos), auth=(user, password), headers=headers)
    except IOError, e:
        print "It looks like the username or password is wrong"
        print e
        sys.exit(1)

    return request.text

def putConnection(urlString, data):
    urlRequest = url + urlString
    request = requests.put(urlString, json.dumps(data))

    try:
        print "oups"
    except IOError, e:
        print "It looks like the username or password is wrong"
        print e
        sys.exit(1)

    jsonObject = json.load(handle)
    handle.close()
    return jsonObject

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

