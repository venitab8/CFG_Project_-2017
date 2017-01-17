# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 18:06:56 2017

@author: thotran
"""
import util
from Result import Result
import urllib2
from bs4 import BeautifulSoup
#Code in Progress
MAIN_URL="http://www.marshallscientific.com/searchresults.asp?Search="
DELIMITER='+'


def exact_results(search_word):
    url=util.create_url(MAIN_URL,search_word,DELIMITER)
    page =urllib2.urlopen(url)
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

print exact_results('centrifuge')
    

        
    
    
    
    






    
    
    
    
    
    
    

