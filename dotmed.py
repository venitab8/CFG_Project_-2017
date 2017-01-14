# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 12:32:55 2017

@author: thotran
"""
from Result import*
import urllib2
from bs4 import BeautifulSoup
#Code in Progress
main_url='https://www.dotmed.com/listings/search/equipment.html?key='
   
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
    page =urllib2.urlopen(web).read()
    soup=BeautifulSoup(page)
    product_grid=soup.find('div', class_='v-product-grid')
    products=product_grid.find_all('div',class_='v-product')
    equips=[]
    for equip in products:
        price_div=equip.find('div', class_='product_productprice')
        for e in price_div.find_all(text=True):
            if e==' ':
                continue
            else:
                price=e
        url=equip.find('a').get('href')
        photo=equip.find('img').get('src')
        title=equip.find_all('a')[1].get('title')
        equipment=Result(title)
        equipment.url=url
        equipment.image_src=photo
        equipment.price=price
        equips.append(equipment)
    return equips