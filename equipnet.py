'''
Created by Abigail Katcoff (complete)

'''

import urllib2
from bs4 import BeautifulSoup
from Result import Result

MAIN_URL= "http://www.equipnet.com/search/?q="

def create_url(search_term):
	specific_url=MAIN_URL
	search_words=search_term.split()
	for i in range(len(search_words)):
		if i!=0:
			specific_url= specific_url + "%20"+ search_words[i]
		else:
			specific_url= specific_url + search_words[i]
	return specific_url

def extract_results(search_term):
	page=urllib2.urlopen(create_url(search_term))
	soup = BeautifulSoup(page)
	table=soup.find('div', id='tbl-listings')
	rows= table.findAll("div", class_="search-row")

	results=[]
	for row in rows:
		new_result=Result(row.find('h3', class_="listing-title").find("a").find(text=True))
		new_result.price=row.find('span', class_="listing-price").find(text=True)
		new_result.url=row.find('a').get('href')
		new_result.image_src=row.find('img', class_="search-thumbnail").get('src')
		results.append(new_result)
	return results

def main():
    print extract_results("Beckman Coulter Biomek Workstation")

if __name__ == "__main__": main()
