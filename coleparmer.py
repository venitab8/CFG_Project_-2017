# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 22:29:01 2017

@author: thotran
"""

import util
from Result import Result
import urllib2
from bs4 import BeautifulSoup
#Code in Progress
MAIN_URL="https://www.coleparmer.com/c/balances-and-scales?searchterm="
DELIMITER='+'
home_url='https://www.coleparmer.com'

def extract_results(search_word, condition=None):
    url=util.create_url(MAIN_URL,search_word,DELIMITER)
    page =urllib2.urlopen(url)
    soup=BeautifulSoup(page,"html.parser")
    '''
    try:
        total_categories=product_grid.find_all('div',class_='featured-category-box')
        #print total_categories
    except:
        return []
    '''
    equips=[]
    cat_grid=soup.find('div', class_='cm')
    cats=cat_grid.find('div',class_='featured-cat-title').find_all('a')
    for cat in cats:
        cat_url=home_url+cat.get('href')
        cat_page_content=BeautifulSoup(urllib2.urlopen(cat_url),"html.parser")
        view_all_products_buttons=cat_page_content.find_all('div', class_='cart-button view-all-button')
        for button in view_all_products_buttons:
            equip_url=home_url+button.find('a').get('href')
            equip_page_content=BeautifulSoup(urllib2.urlopen(equip_url),'html.parser')
            product_table=equip_page_content.find('table',class_='EbProductBottom eb-product-grid-tbl')
            rows=product_table.find('tbody').find_all('tr')
            for row in rows:
                title=row.find('div',{'id':'gaProductName'})
                equipment=Result(title)
                equipment.image=row.find('img', class_='lazy').get('src')
                equipment.price=util.get_price(row.find('span', class_='price-range').find(text=True))
        if util.is_valid_price(equipment.price):
            equips.append(equipment)
    return equips

def main():
    print extract_results('centrifuge')

if __name__=='__main__': main()
    