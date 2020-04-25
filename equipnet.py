'''
Created by Abigail Katcoff (complete)
Modified by Venita Boodhoo (04/2020)
This website sells used equipment
'''
import util
import urllib.request
from bs4 import BeautifulSoup
from Result import Result

MAIN_URL= "http://www.equipnet.com/search/?q="
DELIMITER="%20"

def extract_results(search_term, condition=None):
	if condition=='new':
		return []
	url=util.create_url(MAIN_URL, search_term, DELIMITER)
	page=urllib.request.urlopen(url)
	soup = BeautifulSoup(page,"html.parser")
	table=soup.find('div', class_='search-results-container')
	try:
		rows= table.findAll("div", class_="card-body")
	except:
		return []
	results=[]
	for row in rows:
		new_result=Result(row.find('h6', class_="title listing-title-padding").text)
		new_result.set_price(util.get_price(row.find('span', class_="price price-amount")))
		new_result.set_url(row.find('a').get('href'))
		new_result.set_image_src(row.find('img').get('src'))
		if util.is_valid_price(new_result.get_price()):
			results.append(new_result)
	return results

def main():
	print (extract_results("vacuum pump","used"))

if __name__ == "__main__": main()
