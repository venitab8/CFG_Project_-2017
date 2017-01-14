"""
@author Venita Boodhoo
Website: SibGene
Status: In Progress
"""

import urllib2
from bs4 import BeautifulSoup
from util import *
from Result import Result
import re
import string

page = "http://www.sibgene.com/index.php/catalogsearch/result/?q="

def create_url(item):
	specific_url=page
	search_words=item.split()
	for i in range(len(search_words)):
		if i!=0:
			specific_url= specific_url + "+"+ search_words[i]
		else:
			specific_url= specific_url + search_words[i]
	return specific_url

def get_results(item):                
        page = urllib2.urlopen(create_url(item))
        soup = BeautifulSoup(page,"html.parser" )
        print create_url(item)
        table = soup.find('ol',attrs={'class':'products-list'})
        print soup.select("li")
        results=[]
##        print table.category-products
        
        for row in table:
                print row
                print ""
                '''
                #.encode('utf-8').strip() is used because not all of the characters
                # are recognized
                print row.find('a').get('href')
                new_result = Result(row.a.text.encode('utf-8').strip())
                url = re.sub('/catid/','.php?catid=',row.find('a').get('href'))
                #Omit last slash
                specific_url = re.sub('/prodid/','&prodid=',url)[:-1]
                new_result.url = 'http://www.labcommerce.com'+ specific_url.encode('utf-8').strip()
                new_result.condition = "used"
                new_soup = BeautifulSoup(urllib2.urlopen(new_result.url),"html.parser")
                #Omit surrounding text, get decimal only
                new_result.price = str(new_soup.find('td',class_='price').find_all(text=True)[0])\
                                   .encode('utf-8').strip()
                #Omit 1st char (a period)
                new_result.image_src = 'http://www.labcommerce.com'+new_soup.find('td',align='center')\
                                       .find('img').get('src')[1:].encode('utf-8').strip()
                results.append(new_result)
                '''
        return results

def main():
    print get_results("pump")

main()
