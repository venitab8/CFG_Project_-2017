"""
@author Venita Boodhoo
Website: LabCommerce
Status: Complete
Note: LabCommerce is also a reseller of previously-owned, 
       used and surplus/unused laboratory equipment
"""

import urllib2
from bs4 import BeautifulSoup
from util import *
from Result import Result
import re
import string

main_url = 'http://www.labcommerce.com'
page = "http://www.labcommerce.com/searchresults.php?txtsearch="

def create_url(item):
	specific_url=page
	search_words=item.split()
	for i in range(len(search_words)):
		if i!=0:
			specific_url= specific_url + "+"+ search_words[i]
		else:
			specific_url= specific_url + search_words[i]
	specific_url = specific_url + "&image.x=0&image.y=0"
	return specific_url

def get_results(item,condition=None):
        results=[]
        if condition != 'new':
                page = urllib2.urlopen(create_url(item))
                soup = BeautifulSoup(page,"html.parser" )

                table = soup.find_all('div',class_="search_result")
                
                
                for row in table:
                        #.encode('utf-8') is used because to convert text to str since
                        #not all of the characters are recognized
                        new_result = Result(row.a.text.encode('utf-8').strip())
                        url = re.sub('/catid/','.php?catid=',row.find('a').get('href'))
                        #Omit last slash
                        specific_url = re.sub('/prodid/','&prodid=',url)[:-1]
                        new_result.url = main_url+ specific_url.encode('utf-8').strip()
                        new_result.condition = "used"
                        new_soup = BeautifulSoup(urllib2.urlopen(new_result.url),"html.parser")
                        #Omit surrounding text, get decimal only
                        new_result.price = str(new_soup.find('td',class_='price').find_all(text=True)[0])\
                                           .encode('utf-8').strip()[1:]
                        #Omit 1st char (a period)
                        new_result.image_src = main_url+new_soup.find('td',align='center')\
                                               .find('img').get('src')[1:].encode('utf-8').strip()
                        
                        bad_condition_types = ['bad','poor','not working','broken','not functional']
                        condition_type_text = new_soup.find(text='Condition:')
                        if condition_type_text != None:
                                condition_type = condition_type_text.find_next(text=True)
                                for word in bad_condition_types:
                                        if word not in condition_type:
                                                results.append(new_result)
        
        return results

def main():
    print get_results("pump")

main()
