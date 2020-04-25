# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 12:32:55 2017
Modified by Venita Boodhoo 04/2020
@author: thotran

#Sells used and new equipment
"""
import util
import re
import time
from Result import Result
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import urllib.request
from bs4 import BeautifulSoup 
HOME_URL='http://www.dotmed.com'
MAIN_URL='https://www.dotmed.com/listings/search/equipment.html?key='
DELIMITER='+'
	

def extract_results(search_word, condition=None):
	url=util.create_url(MAIN_URL,search_word,DELIMITER)
	url= url + '&cond=used' if condition!='new' else url + '&cond=new'
	path_to_chromedriver = 'chromedriver.exe'
	option = webdriver.ChromeOptions()
	option.add_argument('headless')
	browser = webdriver.Chrome(executable_path = path_to_chromedriver,options=option)
	browser.get(url)
	time.sleep(5)
	soup=BeautifulSoup(browser.page_source,"html.parser")

	equips=[]
	try:
		sale_equips=soup.find_all('div', {'id': re.compile('listing_*')}) 
	except:
		return equips

	for equip in sale_equips:
		title=equip.find('h4').find('a').text.strip()
		equipment=Result(title)
		equipment.set_url(HOME_URL+equip.find('div', class_='row').find('a').get('href'))
		equipment.set_image_src(equip.find('img').get('src'))
		equipment.set_price(util.get_price(equip.find('span',class_='price')))
		if util.is_valid_price(equipment.get_price()):
			equips.append(equipment)
		if len(equips)==10:
			return equips
	return equips
	
def main():
	print (extract_results('vacuum pump','used'))
if __name__=='__main__': main()
