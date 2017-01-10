# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 18:06:56 2017

@author: thotran
"""

import urllib2
web= "http://www.biosurplus.com"
page =urllib2.urlopen(web)
from bs4 import BeautifulSoup
soup=BeautifulSoup(page)
print soup.prettify()