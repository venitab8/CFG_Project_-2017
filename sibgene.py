"""
@author Venita Boodhoo
Website: SibGene
Status: Complete
"""

import urllib2
from bs4 import BeautifulSoup
from util import *
from Result import Result
import re
import string

page = "http://sibgene.com/index.php/catalogsearch/result/?q="

def create_url(item):
	specific_url=page
	search_words=item.split()
	for i in range(len(search_words)):
		if i!=0:
			specific_url= specific_url + "+"+ search_words[i]
		else:
			specific_url= specific_url + search_words[i]
	return specific_url

def get_results(item,requested_condition=None):
        page = urllib2.urlopen(create_url(item))
        soup = BeautifulSoup(page,"html.parser" )
        results=[]
        table = soup.find_all('li',class_='item')
        
        for row in table:
                new_result = Result(row.find('a').get('title'))
                new_result.url = row.find('a').get('href')
                new_result.price = str(row.find('span',class_='price').find_all(text=True)[0])\
                                   .encode('utf-8')[1:]
                new_result.image_src = row.find('img').get('src')
                
                specific_page = urllib2.urlopen(new_result.url)
                new_soup = BeautifulSoup(specific_page,"html.parser")
                condition = new_soup.find('div',class_='product-collateral').find('div',class_='std').text
                conditions = ['new','New','used','Used']
                bad_condition_types = ['bad','poor','not working','broken','not functional']
                for word in conditions:
                        if word in condition:
                                new_result.condition = word.lower()
                                if (requested_condition == None and word.lower() == 'used') or \
                                        (requested_condition != None and requested_condition.lower()== word.lower()):
                                        #Only add working good equipment
                                        for type_word in bad_condition_types:
                                                if type_word not in condition:
                                                        results.append(new_result)
        return results

def main():
    print get_results("bio pump")
