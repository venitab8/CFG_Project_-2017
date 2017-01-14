"""
@author Venita Boodhoo
Website: EurekaSpot
Status: Complete
Comment: Search only single words, NOT multiple words because
         their web search engine includes the "20" between
         words when it should be recognized as a space
         
         e.g. bio%20pump should search bio pump but their
         code makes it search "bio20pump" which unfortunately
         I cannot change :(

         Same thing with "+"
***Assumes all items are used on this website***???
"""

import urllib2
from bs4 import BeautifulSoup
from util import *
from Result import Result
import re
import string

page = "http://www.eurekaspot.com/estore/searchtmp2.cfm?quiksrch_keywords="

def create_url(item):
	specific_url=page
	search_words=item.split()
	for i in range(len(search_words)):
		if i!=0:
			specific_url= specific_url + "20%"+ search_words[i]
		else:
			specific_url= specific_url + search_words[i]
	return specific_url

def get_results(item,condition=None):
        page = urllib2.urlopen(create_url(item))
        soup = BeautifulSoup(page,"html.parser" )
        results=[]
        table = soup.find_all('td',class_='productname')
        for row in table:
                new_result = Result(row.find('a').text)
                specific_url = "http://www.eurekaspot.com"+row.find('a').get('href')
                new_result.url = re.sub('%2E','.',specific_url)
                new_result.image_src = "http://www.eurekaspot.com"+\
                                       soup.find_all('td',class_='image')[0].find('img').get('src')
                specific_page = urllib2.urlopen(new_result.url)
                new_soup = BeautifulSoup(specific_page,"html.parser")
                new_result.price = new_soup.find('span',class_='sellprice').text
                new_result.condition = "used"
                results.append(new_result)
                
        return results

def main():
    print get_results("pump")

main()
