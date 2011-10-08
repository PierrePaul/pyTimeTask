import sys, base64, urllib2

def startConnection(urlString):
	url = 'https://api.myintervals.com/'

	url = url + urlString
	request = urllib2.Request(url)

	base64string = base64.encodestring('%s:%s' % (user, password))[:-1]
	authheader =  "Basic %s" % base64string
	request.add_header("Authorization", authheader)
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
