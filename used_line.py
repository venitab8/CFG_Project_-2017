# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 16:04:08 2017

@author: thotran
"""
import util
from Result import Result
import urllib2
from bs4 import BeautifulSoup
#Code in Progress
MAIN_URL='http://www.used-line.com/search/s_index.cfm?search_term='
DELIMITER='+'
   
def exact_results(search_word):
    url=util.create_url(MAIN_URL,search_word,DELIMITER)
    page =urllib2.urlopen(url)
    soup=BeautifulSoup(page)
    product_grid=soup.find('ul', class_='Products_ul')
    total_equips=product_grid.find_all('li',class_='Products')
    equips=[]
    for equip in total_equips:
        title=equip.find('div', class_='title').find('span').find(text=True).strip()
        equipment=Result(title)
        equipment.url=equip.find('a').get('href')
        equipment.image_src=equip.find('div', class_='Image').find('img').get('src')
        price=equip.find('div', class_='price').find_all(text=True)
        equipment.price=''.join(price).strip()
        equips.append(equipment)
    return equips
    
print(exact_results('centrifuge'))