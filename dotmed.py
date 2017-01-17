# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 12:32:55 2017

@author: thotran
"""
import util
from Result import Result
import urllib2
from bs4 import BeautifulSoup
#Code in Progress  
MAIN_URL='https://www.dotmed.com/listings/search/equipment.html?key='
DELIMITER='+'
    
def extract_results(search_word):
    url=util.create_url(MAIN_URL,search_word,DELIMITER)
    page =urllib2.urlopen(url)
    soup=BeautifulSoup(page)
    product_grid=soup.find('div', id='totalListings')
    equips=[]
    #auction items
    auction_equips=product_grid.find_all('div',class_='auction_table')
    for auction_equip in auction_equips:
        equips.append(Result('Auction Equipment'))
    #sale items
    sale_equips=product_grid.find_all('div', class_='listings_table_d') 
    # tries to fix unicode encode error later
    for equip in sale_equips:
        if equip.find('dl', class_='datePosted').find('p')==None:
            equips.append(Result('No price'))
            continue
        title=''.join(equip.find('dt', class_='listing_head').find_all(text=True)).strip()
        equipment=Result(title)
        equipment.url='http:'+equip.find('dt', class_='listing_head').find('a').get('href')
        equipment.image_src=equip.find('dd',class_='img').find('img').get('src')
        price=equip.find('dl', class_='datePosted').find('p').find(text=True)
        equipment.price=util.get_price(price)
        if util.is_valid_price(equipment.price):
            equips.append(equipment)
    return equips
    
def main():
    print extract_results('bio centrifuge')
if __name__=='__main__': main()