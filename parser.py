from HTMLPArser import HTMLParser
import urllib

sampleUrl = "http://www.google.co.in"

handle = urllib.urlopen(sampleUrl)
html_data = handle.read()
print html_data
