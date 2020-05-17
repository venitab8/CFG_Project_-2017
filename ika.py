# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 22:29:01 2017
Modified by Venita Boodhoo (04/2020)
@author: thotran
Status:Complete
Website with New products
"""
import util
from Result import Result
import urllib.request
from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

MAIN_URL='https://www.ika.com/owa/ika/catalog.search_autocomplete?term='
#r = requests.get(MAIN_URL, timeout = 4)
DELIMITER='+'
HOME_URL='https://www.ika.com/en'

	
def extract_results(search_word,condition=None):
	#url=util.create_url(MAIN_URL,search_word,DELIMITER)
	url = HOME_URL
	try:
		path_to_chromedriver = 'chromedriver.exe'
		option = webdriver.ChromeOptions()
		option.add_argument('headless')
		browser = webdriver.Chrome(executable_path = path_to_chromedriver,options=option)
		#url = "view-source:" + url
		browser.get(url)
		time.sleep(5)
		soup = BeautifulSoup(browser.page_source, 'html.parser')
		search_bar = soup.find('span',class_= "main-search--text")
		search_bar.string = search_word		 
		#search_bar.send_keys(Keys.RETURN)
		#print(soup,"soup")
		test = browser.find_element_by_tag_name('form')
		product_table=browser.find_element_by_class_name('main-search--results')
		text = WebDriverWait(browser, 10).until(lambda browser: product_table.text)
		print(text,"text")        
		#test.click()
		#product_table=soup.find('div',class_='main-search--results')
		print(product_table,"pt")
		#product_table=soup.find('ul',class_='results--list')
		result_links=product_table.find_all('li',class_="list--entry result--item")
	except Exception as e:
		print ("Error2 was: ", e) 
		return []
		
	equips=[]
	for link in result_links:
		product_url=HOME_URL+link.find('a').get('href')
		print(product_url)
		title = link.find('a').get('title')
		print(title)
		equipment=Result(title)
		equipment.set_url(product_url)
		product_page_content=BeautifulSoup(urllib.request.urlopen(product_url),"html.parser")
		equipment.set_image_src(HOME_URL+product_page_content.find('img').get('src'))
		equipment.set_price(util.get_price(product_page_content.find('span', class_='price--default is--nowrap').text))
		if util.is_valid_price(equipment.get_price()):
			equips.append(equipment)
		if len(equips)==10:
			return equips
	return equips

def main():
	print (extract_results('vial'))

if __name__=='__main__': main()
	
