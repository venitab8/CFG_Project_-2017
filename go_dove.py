# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 00:49:07 2017

@author: thotran
"""
import urllib2
from bs4 import BeautifulSoup

main_url='http://www.go-dove.com/en/auction/search?cmd=results&fromsearch=true&words='

def search_url(search_word):
    if len(search_word)==0:
        return 'Please enter a keyword for searching'
    if ' ' in search_word:
        search=search_word.replace(' ', '+')
    else:
        search=search_word
    return main_url+search
    
    
def equipment_properties(search_word):
    web=search_url(search_word)
    page=urllib2.urlopen(web).read()
    soup=BeautifulSoup(page)
    #product_grid=soup.find('table',class_='results-table table table-striped')
    products=soup.find('tbody')
    for product in products.find_all('tr'):
        
    #for row in products.find('tr'):
        #return row
    #return products
    
    
print equipment_properties('centrifuge')