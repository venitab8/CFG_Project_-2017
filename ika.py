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
MAIN_URL="http://www.ika.com/owa/ika/catalog.search?iString="
DELIMITER='+'
home_url='http://www.ika.com'
def extract_results(search_word, condition=None):
    url=util.create_url(MAIN_URL,search_word,DELIMITER)
    page =urllib2.urlopen(url)
    soup=BeautifulSoup(page,"html.parser")
    product_table=soup.find('table', class_='table_content')
    try:
        result_links=product_table.find_all('a')
    except:
        return []
    equips=[]
    for link in result_links:
        product_url=home_url+link.get('href')
        product_page_content=BeautifulSoup(urllib2.urlopen(product_url),"html.parser")
        title=''.join(product_page_content.find('div', class_='product_left').find('h1').find_all(text=True)).strip()
        equipment=Result(title)
        equipment.url=product_url
        equipment.image_src=home_url+product_page_content.find('img',{"id": "big_product_img"}).get('src')
        equipment.price=util.get_price(product_page_content.find('div', class_='pr_price2').find(text=True))
        
        if util.is_valid_price(equipment.price):
            equips.append(equipment)
    return equips

def main():
    print extract_results('centrifuge')

if __name__=='__main__': main()
    