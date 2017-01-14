"""
@author Venita Boodhoo
Website: LabCommerce
Status: In Progress
Note: LabCommerce is also a reseller of previously-owned, 
       used and surplus/unused laboratory equipment
"""

import urllib2
from bs4 import BeautifulSoup
from util import *
from Result import Result

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

def get_results(item):                
        page = urllib2.urlopen(create_url(item))
        soup = BeautifulSoup(page,"html.parser" )

        table = soup.find_all('div',id="results")
        #print table
        print "-----------------"
        for row in table:
                print row.a.title
                new_result = Result(row.find('a').title)
                print new_result.title
                new_result.url = create_url(item)+row.find('a').get('href')
        
        results=[]
        print "----"
        for row in table:
                #print row
                new_result = Result(row.find('a').get('title'))
                #print new_result.title
                new_soup = BeautifulSoup(urllib2.urlopen(new_result.url),"html.parser")
                new_result.price = new_soup.find('a')
                number = get_price(new_result.title)
                new_result.condition = "used"
                new_result.image_src = "https://photos.labx.com/labx/"+number+"/"+number+"-0.jpg"
                results.append(new_result)
                results.append("\n")
        return results

def main():
    print get_results("pump")

main()
