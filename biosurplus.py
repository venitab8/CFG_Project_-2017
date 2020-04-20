'''
Created by Abigail Katcoff
Modified by Venita Boodhoo (04/2020)
This website sells pre-owned equipment
'''
import urllib.request
import util
import time
import re
from bs4 import BeautifulSoup
from Result import Result
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

MAIN_URL= "http://www.biosurplus.com/?ajax_search_nonce=b2ba2354a5&s="
DELIMITER= '+'

def extract_results(search_term, condition=None):
	if condition=='new':
		return []
	headers={
	'Host': 'www.biosurplus.com',
	'Connection': 'keep-alive',
	'Accept': 'text/html',
	'Referer': 'http://www.biosurplus.com/?ajax_search_nonce=b2ba2354a5&s==Beckman+Coulter&post_type=product',
	'Accept-Encoding': 'gzip, deflate, sdch',
	'Accept-Language': 'en-US,en;q=0.8',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
	url=util.create_url(MAIN_URL, search_term, DELIMITER)+ "&post_type=product"
	path_to_chromedriver = 'chromedriver.exe'
	option = webdriver.ChromeOptions()
	option.add_argument('headless')
	browser = webdriver.Chrome(executable_path = path_to_chromedriver,options=option)
	browser.get(url)
	time.sleep(5)

	soup = BeautifulSoup(browser.page_source,"html.parser")
	table=soup.find('div', class_='content-area')
	try:
		#check if the table
		rows= table.findAll("li", {"class": re.compile('post-*')})
	except:
		return []
	results=[]
	for row in rows:
				new_result=Result(row.find('h2', class_="woocommerce-loop-product__title").text)
				new_result.set_price(util.get_price(row.find(text= re.compile("Price*"))))
				#Handle different paths
				try:
					img_src = row.find('div',class_="image_frame").find('div',class_="product-loop-image bsi-thumb").get("style")			 
				except:
					img_src = row.find('div',{"style": re.compile('background*')}).get('style')				 
				img_src = img_src.replace(') ', '( ')
				img_src = img_src.split('(')[1]
				img_src = img_src.split(')')[0]
				new_result.set_image_src(img_src)
				new_result.set_url(row.find('a').get('href'))
				if util.is_valid_price(new_result.get_price()):
						results.append(new_result)
						if len(results)==10:
								return results
	return results


def main():
	print (extract_results("Beckman Coulter"))

if __name__ == "__main__": main()
