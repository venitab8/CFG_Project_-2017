'''
Created by Abigail Katcoff (complete)
Modified by Venita Boodhoo (04/2020)
New and Used Equipment
'''
import util
import urllib.request
from bs4 import BeautifulSoup
from Result import Result

MAIN_URL='http://www.ebay.com/sch/i.html?_nkw='
DELIMITER= '+'

USED= '&LH_ItemCondition=4'
NEW= '&LH_ItemCondition=3'

def extract_results(search_term, condition=None):
	url=''
	if condition=='new':
		url = util.create_url(MAIN_URL, search_term, DELIMITER) + '&rt=nc' + NEW
	else:
		url = util.create_url(MAIN_URL, search_term, DELIMITER) + '&rt=nc' + USED
	page=urllib.request.urlopen(url)
	soup = BeautifulSoup(page,"html.parser")
	table=soup.find('div',class_='srp-river-results clearfix')
	try:
		rows=table.findAll('div', class_='s-item__wrapper clearfix')
	except:
		return []
	results=[]
	for row in rows: 
		new_result=Result(row.find('img', class_='s-item__image-img').get('alt'))
		new_result.set_url(row.find('a').get('href'))
		new_result.set_image_src(row.find('img', class_='s-item__image-img').get('src'))
		new_result.set_price(util.get_price(row.find('span', class_="s-item__price").text))
		if util.is_valid_price(new_result.get_price()):
			results.append(new_result)
	return results

def main():
	print (extract_results("vacuum pump","new"))

if __name__ == "__main__": main()
