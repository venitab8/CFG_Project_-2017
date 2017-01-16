import util
import urllib2
from bs4 import BeautifulSoup
from Result import Result

MAIN_URL='https://www.google.com/search?output=search&tbm=shop'
DELIMITER= '+'

def extract_results(search_term, condition=None):
	url=util.create_url(MAIN_URL, search_term, DELIMITER)
	url = url + '&tbs=vw:l,mr:1,new:1' if condition=='new' else url
	page=urllib2.urlopen(url)
	soup = BeautifulSoup(page)
	table=soup.find('div', class_='sh-pr__product-results')
	rows=table.findAll('div', class_='psli')

	results=[]
	for row in rows:
		#ensure that if we're looking for used results to include used results only
		if condition!='new' and row.find('span', class_='price').find(text=True).strip()!='used':
			continue
		new_result=Result(row.find('a', class_=pstl).find(text=True))
		new_result.url='https://www.google.com'+row.find('a', class_=pstl).get('href')
		new_result.price=util.get_price(row.find('span', class_='price').b.find(text=True))
		new_result.image_src=row.find('img').get('src')
		if util.is_valid_price(new_result.price):
			results.append(new_result)
	return results


def main():
    print extract_results("Beckman Coulter Biomek Workstation")

if __name__ == "__main__": main()