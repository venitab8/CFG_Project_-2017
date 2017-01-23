"""
@author Venita Boodhoo
Website: LabX
Status: Complete
"""

import urllib2
from bs4 import BeautifulSoup
from util import *
from Result import Result

MAIN_URL = "http://www.labx.com/v2/adsearch/search.cfm?sw="
DELIMITER = "%20"

def extract_results(item,condition=None):
        if condition == "new":
                specific_url = create_url(MAIN_URL,item,DELIMITER) + "&condition=New,New%20or%20Used&adtype=998"
        else:
                specific_url = create_url(MAIN_URL,item,DELIMITER) + "&condition=Used,Refurbished,For%20Parts/Not%20Working,New%20or%20Used&adtype=998"
                
        page = urllib2.urlopen(specific_url)
        soup = BeautifulSoup(page,"html.parser" )

        table = soup.find('tbody', class_='ResultsNewTable')
        results=[]

        for row in table.find_all('tr'):
                  new_result = Result(row.find('a').get('title'))
                  new_result.url = row.find('a').get('href')
                  new_result.price = get_price(row.find_all('td')[4].contents[0])
                  new_soup = BeautifulSoup(urllib2.urlopen(new_result.url),"html.parser")
                  number = get_price(new_result.title)
                  new_result.image_src = "https://photos.labx.com/labx/"+number+"/"+number+"-0.jpg"
                  if is_valid_price(new_result.price):
                    new_result.description = new_soup.find('div',class_='AdInformationBlock')
                    results.append(new_result)
        return results

def main():
    print extract_results("Bio rad pump")

if __name__ == "__main__": main()
