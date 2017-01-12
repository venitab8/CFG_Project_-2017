#LabCommerce
#Status: In Progress

import re
import string
import urllib2
from bs4 import BeautifulSoup
testpage = "http://www.labcommerce.com/searchresults.php?txtsearch=air+pump&image.x=0&image.y=0"
page = urllib2.urlopen(testpage)
soup = BeautifulSoup(page,"html.parser")

table = soup.find('tbody', class_='ResultsNewTable')
#For used condition add the below comment to url string:
#&condition=Used,Refurbished,For%20Parts/Not%20Working,New%20or%20Used&adtype=998

##Description

#Title
A = []
#Link
B = []
#Price
C = []

#Description
D = []
#Seller Info
E = []
#Image
F = []

for row in table.find_all('tr'):
  A.append(row.find('a').get('title'))
  B.append(row.find('a').get('href'))
  C.append(row.find_all('td')[4].contents[0])
  new_soup = BeautifulSoup(urllib2.urlopen(B[-1]),"html.parser")
  #D.append(new_soup.find('span'),class_='AdDetailsTitle')
  E.append(new_soup.find('div', class_='sellerInformation'))
  allow = string.digits
  number = re.sub('[^%s]' %allow,'',A[-1])
  F.append("https://photos.labx.com/labx/"+number+"/"+number+"-0.jpg")

#print D

