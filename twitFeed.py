import urllib2

from BeautifulSoup import BeautifulStoneSoup

var = raw_input("Enter your Twitter id: ")

print "Tweets of", var

er = "http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20twitter.user.timeline%20where%20id%3D'"

fg = "'&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"

 

zx = er+var+fg

 

page = urllib2.urlopen(zx)

soup = BeautifulStoneSoup(page)

tweet = soup.findAll('text')

for twt in tweet:



    print twt.string
