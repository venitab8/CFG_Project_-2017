'''
Created by Abigail Katcoff (complete)

'''

import urllib2
import util
from bs4 import BeautifulSoup
from Result import Result

MAIN_URL= "http://www.sci-bay.com/?s="

def create_url(search_term):
	specific_url=MAIN_URL
	search_words=search_term.split()
	for i in range(len(search_words)):
		if i!=0:
			specific_url= specific_url + "+"+ search_words[i]
		else:
			specific_url= specific_url + search_words[i]
	return specific_url

def extract_results(search_term, condition=None):
	#This website only contains used equipment
	if condition=='new':
		return []
	page=urllib2.urlopen(create_url(search_term))
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
