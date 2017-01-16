"""
@author Venita Boodhoo
Website: LabX
Status: Complete
Note: Have not sorted broken equipment yet
"""

import urllib2
from bs4 import BeautifulSoup
from util import *
from Result import Result

page = "http://www.labx.com/v2/adsearch/search.cfm?sw="

def create_url(item):
	specific_url=page
	search_words=item.split()
	for i in range(len(search_words)):
		if i!=0:
			specific_url= specific_url + "%20"+ search_words[i]
		else:
			specific_url= specific_url + search_words[i]
	return specific_url


def get_results(item,condition=None):
        if condition == "new":
                specific_url = create_url(item) + "&condition=New,New%20or%20Used&adtype=998"
        else:
                specific_url = create_url(item) + "&condition=Used,Refurbished,For%20Parts/Not%20Working,New%20or%20Used&adtype=998"
                
        page = urllib2.urlopen(specific_url)
        soup = BeautifulSoup(page,"html.parser" )

        table = soup.find('tbody', class_='ResultsNewTable')
        results=[]

        for row in table.find_all('tr'):
                  new_result = Result(row.find('a').get('title'))
                  new_result.url = row.find('a').get('href')
                  new_result.price = row.find_all('td')[4].contents[0]
                  new_soup = BeautifulSoup(urllib2.urlopen(new_result.url),"html.parser")
                  #D.append(new_soup.find('span'),class_='AdDetailsTitle')
                  #E.append(new_soup.find('div', class_='sellerInformation'))
                  number = get_price(new_result.title)
                  new_result.condition = condition
                  new_result.image_src = "https://photos.labx.com/labx/"+number+"/"+number+"-0.jpg"
                  results.append(new_result)
        return results

def main():
    print get_results("Bio rad pump","used")


