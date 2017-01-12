import urllib2
'''
Created by Abigail Katcoff (complete)

'''

import gzip
import StringIO
from bs4 import BeautifulSoup
from Result import Result

MAIN_URL= "http://www.biosurplus.com/store/search/?per_page=24&product_search_q="

def create_url(search_term):
	specific_url=MAIN_URL
	search_words=search_term.split()
	for i in range(len(search_words)):
		if i!=0:
			specific_url= specific_url + "+"+ search_words[i]
		else:
			specific_url= specific_url + search_words[i]
	return specific_url

def extract_results(search_term):
	headers={
	'Host': 'www.biosurplus.com',
	'Connection': 'keep-alive',
	'Accept': 'text/html',
	'Referer': 'http://www.biosurplus.com/store/search/?per_page=24&product_search_q=Beckman+Coulter+Biomek+Workstation',
	'Accept-Encoding': 'gzip, deflate, sdch',
	'Accept-Language': 'en-US,en;q=0.8',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
	req =urllib2.Request(create_url(search_term), headers=headers)
	page=urllib2.urlopen(req)
	stringified_data = StringIO.StringIO(page.read())
	unzipped_page = gzip.GzipFile(fileobj=stringified_data)
	soup = BeautifulSoup(unzipped_page)
	table=soup.find('div', class_='product_browse')
	rows= table.findAll("div", class_="fps_featured_product")
	results=[]
	for row in rows:
		new_result=Result(row.find('h2', class_="fps_fp_heading").find("a").find(text=True))
		new_result.price=row.find('p', class_='product_price').find(text=True)
		new_result.image_src=row.find('div', class_="fps_fp_image_inner").find('img').get('src')
		new_result.url="www.biosurplus.com" +  row.find('a').get('href')
		results.append(new_result)
	return results


def main():
    print extract_results("Beckman Coulter Biomek Workstation")

if __name__ == "__main__": main()
