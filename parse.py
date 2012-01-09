from HTMLParser import HTMLParser

class PPStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def stripTags(html):
    s = PPStripper()
    s.feed(html)
    return s.get_data()
