# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 00:49:07 2017

@author: thotran
"""
from Result import Result
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
    page=urllib2.urlopen(web)
    #product_grid=soup.find('table',class_='results-table table table-striped')
    products=soup.find('tbody')
    for product in products.find_all('tr'):
        
    #for row in products.find('tr'):
        #return row
    #return products
        
        
def equipments(search_word):
    web=search_url(search_word)
    page =urllib2.urlopen(web)
    soup=BeautifulSoup(page)
    product_grid=soup.find('div', class_='pagebody')
    total_equips=product_grid.find_all('div',class_='el')
    equips=[]
    for equip in total_equips:
        # tries to fix this later
        items_details=equip.find('div', class_='item_details').find_all(text=True)
        #print items_details
        title=' '.join(items_details).strip()
        equipment=Result(title)
        equipment.url=equip.find('div',class_='image').find('a',class_='item_number').get('href')
        equipment.image_src=equip.find('div',class_='image').find('img').get('src')
        equipment.price=equip.find('div', class_='price').find('span').find(text=True).strip()
        equips.append(equipment)
    return equips
    
    
print equipment_properties('centrifuge')