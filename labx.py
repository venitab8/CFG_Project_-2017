import urllib2
from bs4 import BeautifulSoup
testpage = "http://www.labx.com/v2/adsearch/search.cfm?sw=bio%20rad%20hd%20pump"
page = urllib2.urlopen(testpage)
soup = BeautifulSoup(page,"html.parser")
print soup
#&condition=Used,Refurbished,For%20Parts/Not%20Working,New%20or%20Used&adtype=998

