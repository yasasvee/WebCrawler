from HTMLParser import HTMLParser
import urllib

sampleUrl = "http://www.google.co.in"
urllist = []
class MyHTMLParser(HTMLParser):
	def handle_data(self, data):
		if data!='\n':
			urllist.append(data)
handle = urllib.urlopen(sampleUrl)
html_data = handle.read()
parser = MyHTMLParser()
parser.feed(html_data)
parser.close()
for url in urllist:
	print url
