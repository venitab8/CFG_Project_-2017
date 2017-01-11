# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 18:06:56 2017

@author: thotran
"""

import urllib
from bs4 import BeautifulSoup
#Learning Beautiful Area
'''
web= "http://www.marshallscientific.com/Hettich-EBA-21-Centrifuge-w-1118-01-Rotor-p/heba21.htm"
page =urllib.urlopen(web).read()
soup=BeautifulSoup(page)
#print soup.prettify()
#print soup.a
links= soup.find_all('a')
#for link in links:
    #print link.get('href')

tables=soup.find_all('table')[0:100]
#print tables
table=soup.find('table', class_="colors_pricebox")
rows=table.find_all('tr')
price=[]
for row in rows:
    if row.find('span', itemprop="price")!=None:
        price.append(row.find('span', itemprop="price").find(text=True))
        break
#print price
#print division.find_all('span', itemprop='price')
    
    
#print price
#print price

#for row in 
    
#print tables

'''
#Code in Progress
main_url="http://www.marshallscientific.com/searchresults.asp?Search="
    
def search_url(search_word):
    if ' ' in search_word:
        search=search_word.replace(' ', '+')
    else:
        search=search_word
    return main_url+search+'&Submit='
    
#print search_url('Eppendorf 5415C Centrifuge')

def equipment_properties(search_word):
    web=search_url(search_word)
    page =urllib.urlopen(web).read()
    soup=BeautifulSoup(page)
    product_grid=soup.find('div', class_='v-product-grid')
    products=product_grid.find_all('div',class_='v-product')
    #prices=[]
    #urls=[]
    #photos=[]
    equips=[]
    for equip in products:
        price_div=equip.find('div', class_='product_productprice')
        price=price_div.find_all(text=True)
        #print price_div.find(text=True)
        #prices.append(price_b.find_all(text=True)[1])
        
        #equip_details=equip.find('div', class_="v-product__details")
        url=equip.find('a').get('href')
        photo=equip.find('img').get('src')
        #for detail in equip_details:
        #urls.append(detail.find('a').get('href'))
        equips.append((price,url,photo))
         
         
         
    return equips
        

    
    
    
    
print equipment_properties('centrifuge')
        
    
    
    
    






    
    
    
    
    
    
    

