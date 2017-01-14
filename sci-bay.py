'''
Created by Abigail Katcoff (complete)

'''

import urllib2
import util
from bs4 import BeautifulSoup
from Result import Result

MAIN_URL= "http://www.sci-bay.com/?s="
DELIMITER= '+'

def extract_results(search_term, condition=None):
	#This website only contains used equipment
	if condition=='new':
		return []
	url=util.create_url(MAIN_URL, search_term, DELIMITER)
	page=urllib2.urlopen(url)
	soup = BeautifulSoup(page)
	table=soup.find('div', class_='content-area')
	rows= table.findAll("article")

	results=[]
	for row in rows:
		new_result=Result(row.find('h1', class_="entry-title").find("a").find(text=True))
		result_url=row.find('a').get('href')

		#scrape from the result's page
		result_soup=BeautifulSoup(urllib2.urlopen(result_url))
		new_result.url=result_url
		new_result.price=util.get_price(result_soup.find('span', class_="amount").find(text=True))
		new_result.image_src=result_soup.find('div', class_='images').find('img').get('src')
		new_result.condition='used'
		if util.is_valid_price(new_result.price):
			results.append(new_result)
	return results

def main():
    results= extract_results("Beckman")
    try:
    	print results
    except:
	    for result in results:
	    	print result.title, result.url 
	    	print result.price, result.image_src + "\n"

if __name__ == "__main__": main()
