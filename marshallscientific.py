# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 18:06:56 2017

@author: thotran
"""
from Result import Result
import urllib2
from bs4 import BeautifulSoup
#Code in Progress
main_url="http://www.marshallscientific.com/searchresults.asp?Search="
   
def search_url(search_word):
    if len(search_word)==0:
        return 'Please use a keyword for searching'
    if ' ' in search_word:
        search=search_word.replace(' ', '+')
    else:
        search=search_word
    return main_url+search+'&Submit='

def equipments(search_word):
    web=search_url(search_word)
    page =urllib2.urlopen(web)
    soup=BeautifulSoup(page)
    product_grid=soup.find('div', class_='v-product-grid')
    total_equips=product_grid.find_all('div',class_='v-product')
    equips=[]
    for equip in total_equips:
        title=equip.find('a', class_='v-product__title productnamecolor colors_productname').find(text=True).strip()
        equipment=Result(title)
        equipment.url=equip.find('a',class_='v-product__img').get('href')
        equipment.image_src='http:'+equip.find('img').get('src')
        price=equip.find('div', class_='product_productprice').find_all(text=True)
        equipment.price=''.join(price).strip('Our Price:').strip()
        equips.append(equipment)
    return equips

print equipments('centrifuge')
    

        
    
    
    
    






    
    
    
    
    
    
    

