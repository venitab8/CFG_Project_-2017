"""
@author Venita Boodhoo
Website: daigger
Status: In Progress (need to retrieve info for all items on specific pg, price to do)
Comments: For new equipment only
May return just a result on one page
"""

import urllib2
from bs4 import BeautifulSoup
from util import *
from Result import Result

MAIN_URL = "http://www.daigger.com/products-search?qs="
HOME_URL = "http://www.daigger.com"                    
DELIMITER = "+"

def extract_results(item,condition=None):
        results=[]
        if condition != "new":
                return results
        specific_url = create_url(MAIN_URL,item,DELIMITER)
        page = urllib2.urlopen(specific_url)
        soup = BeautifulSoup(page,"html.parser" )

        table = soup.find('div',id ="ListingProducts")

        try:
                  rows=table.find('div',class_="boxshad productbox")
        except:
                  return []
                
        for row in table.find_all('div',class_="boxshad productbox"):
                new_result = Result(row.find('a').get('title'))
                new_result.url = HOME_URL + row.find('a').get('href')
                new_result.image_src = row.find('img').get('src')
                specific_page = urllib2.urlopen(new_result.url)
                new_soup = BeautifulSoup(specific_page,"html.parser")
                new_result.price = new_soup.find('strong',class_="price").text
                if is_valid_price(new_result.price):
                        results.append(new_result)
        return results

def main():
    print extract_results("balance scale","new")

if __name__ == "__main__": main()
