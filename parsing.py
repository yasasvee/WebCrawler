import urllib
from HTMLParser import HTMLParser
from lxml.html import parse
urltext = []
class myHTMLParser(HTMLParser):
	def handle_data(self, data):
		if data != '\n':
			urltext.append(data)
if __name__ == '__main__':
	fileParser = myHTMLParser()
	testUrl = "http://www.shopping.com/products?KW=<keword>"
	parsedURL = parse(testUrl)
	doc = parsedURL.getroot()
	links = doc.findall('.//a')
	linksSet = []
	for entry in links:
		linksSet.append(entry.get('href'))
	for entry in linksSet:
		print entry
	#pageHandle = urllib.urlopen(testUrl).read()
	#print pageHandle+"\n\n"
	#fileParser.feed(pageHandle)
	#fileParser.close()
	#print urltext
