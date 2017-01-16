# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 12:32:55 2017

@author: thotran
"""
from Result import Result
import urllib2
from bs4 import BeautifulSoup
#Code in Progress
main_url='https://www.dotmed.com/listings/search/equipment.html?key='
auction_url='https://www.dotmed.com/auction/'
   
def search_url(search_word):
    if len(search_word)==0:
        return 'Please use a keyword for searching'
    if ' ' in search_word:
        search=search_word.replace(' ', '+')
    else:
        search=search_word
    return main_url+search
    
def equipments(search_word):
    web=search_url(search_word)
    page =urllib2.urlopen(web)
    soup=BeautifulSoup(page)
    product_grid=soup.find('div', id='totalListings')
    #auction items
    equips=[]
    auction_equips=product_grid.find_all('div',class_='auction_table')
    for auction_equip in auction_equips:
        equips.append(Result('Auction Equipment'))
    
    sale_equips=product_grid.find_all('div', class_='listings_table_d') 
    # tries to fix this later
    for equip in sale_equips[1::]:
        if equip.find('dl', class_='datePosted').find('p')==None:
            equips.append(Result('No price'))
            continue
        title=''.join(equip.find('dt', class_='listing_head').find_all(text=True)).strip()
        equipment=Result(title)
        equipment.url='http:'+equip.find('dt', class_='listing_head').find('a').get('href')
        equipment.image_src=equip.find('dd',class_='img').find('img').get('src')
        price=equip.find('dl', class_='datePosted').find('p').find_all(text=True)
        equipment.price=str(''.join(price).strip('Asking Price: ').strip())
        equips.append(equipment)
    return equips
   
print equipments('bio centrifuge')
#print search_url('Applied Biosystems 9700')