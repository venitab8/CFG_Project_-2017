"""
@author Venita Boodhoo
Website: NewLifeScientific
Status: Complete
Note: Assumes all items are used
"""

import urllib2
from bs4 import BeautifulSoup
from util import *
from Result import Result
import re
import string

main_url = "http://newlifescientific.com"
page = "http://newlifescientific.com/search?q="

def create_url(item):
	specific_url=page
	search_words=item.split()
	for i in range(len(search_words)):
		if i!=0:
			specific_url= specific_url + "+"+ search_words[i]
		else:
			specific_url= specific_url + search_words[i]
	return specific_url

def get_results(item,condition=None):
        results = []
        if condition != 'new':
                page = urllib2.urlopen(create_url(item))
                soup = BeautifulSoup(page,"html.parser" )
                table = soup.find_all('li',class_='item')
                
                for row in table:
                        new_result = Result(row.find('a').get('title'))
                        new_result.url = main_url+row.find('a').get('href')
                        new_result.price = row.find('span',class_='price').text
                        new_result.image_src = row.find('img').get('src')
                        
                        specific_page = urllib2.urlopen(new_result.url)
                        new_soup = BeautifulSoup(specific_page,"html.parser")
                        item_condition = new_soup.find('div',class_='box-collateral-content').find('div',class_='std').text

                        bad_condition_types = ['bad','poor','not working','broken','not functional']
                        if condition != "new" or condition != "New":
                                #Only add working good equipment
                                for type_word in bad_condition_types:
                                        if type_word not in item_condition:
                                                new_result.condition = "used"
                                                results.append(new_result)
                
        return results

def main():
    print get_results("balance scale")

