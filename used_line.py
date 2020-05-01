# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 16:04:08 2017
Modified by Venita Boodhoo (05/2020)
@author: thotran

Assume most results used on used-line are used, Use this function only to search for used
"""
import util
import re
import time
from Result import Result
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

MAIN_URL='https://www.used-line.com/search/s_index.cfm?search_term='
DELIMITER='+'
HOME_URL='https://www.used-line.com'
   

def extract_results(search_word, condition=None):
	if condition=='new':
		return []
	url=util.create_url(MAIN_URL,search_word,DELIMITER)
	path_to_chromedriver = 'chromedriver.exe'
	option = webdriver.ChromeOptions()
	option.add_argument('headless')
	browser = webdriver.Chrome(executable_path = path_to_chromedriver,options=option)
	browser.get(url)
	time.sleep(5)
	soup = BeautifulSoup(browser.page_source,"html.parser")
	product_grid=soup.find('ul',class_='product_list p_list')
	try:
		total_equips=product_grid.find_all('li',{"class": re.compile('p_list_item*')})
	except:
		return []
	equips=[]
	for equip in total_equips:
		title=equip.find('div', class_='title').find('a').text
		print(title,"t")
		equipment=Result(title)
		equipment.set_url(HOME_URL+equip.find('a').get('href'))
		equipment.set_image_src(HOME_URL+equip.find('div', class_='thumb').find('img').get('src'))
		price_text=equip.find('li', class_='price').text
		equipment.set_price(util.get_price(price_text))
		if util.is_valid_price(equipment.get_price()):
			equips.append(equipment)
		if len(equips)==10:
			return equips
	return equips

def main():
	print(extract_results('centrifuge'))

if __name__=='__main__': main()
