"""
@author Venita Boodhoo
Website: us.vmr
Status: Get all items and price
Comments: For new equipment only
"""

import urllib2
#import html5lib
from bs4 import BeautifulSoup
from util import *
from Result import Result
'''
MAIN_URL = "https://us.vwr.com/store/search/searchResultList.jsp;jsessionid=8ZklCtAydmfcnhnY5QszDh7b.estore4a?_dyncharset=UTF-8&"+\
           "_dynSessConf=-257157651131681844&keyword="
           '''
MAIN_URL = "https://us.vwr.com/store/search/searchResultList.jsp?&keyword="
HOME_URL = "https://us.vwr.com"                    
DELIMITER = "+"

def extract_results(item,condition=None):
        results=[]
        if condition != "new":
                return results
        specific_url = create_url(MAIN_URL,item,DELIMITER)
        #print specific_url
        page = urllib2.urlopen(specific_url)
        
        soup = BeautifulSoup(page,"html.parser" )
        #print soup
        table = soup.find('div',id ="items")
        #print table
        try:
                  rows=table.find_all('div',class_="search_item")
        except:
                  #print "?"
                  return []
                
        for row in table.find_all('div',class_="search_item"):
                supplier = row.find('div',class_="search_supplier").text.replace('Supplier:','')
                title = row.find('span',style=True).text
                #Add supplier to name if not in title
                if not any(supplier_word in title.split() for supplier_word in supplier.split()) and \
                   all(title.find(supplier_word)==-1 for supplier_word in supplier.split()):
                        title = supplier + " " + title
                title = ' '.join(title.split())
                #print title
                new_result = Result(title)
                new_result.url = HOME_URL+row.find('a').get('href')
                new_result.image_src = row.find('img').get('src')

                #Price is a hidden value on page?, parse specific url with soup
                specific_page = urllib2.urlopen(new_result.url)
                new_soup = BeautifulSoup(specific_page,"html.parser" )

                #Find where description and price tags are located in column
                description_index = None
                VWR_index = None
                price_index = None
                tags = new_soup.find_all('th',class_="productHeader")
                for i in range(len(tags)):
                        if tags[i].text == "Description":
                                description_index = i
                        if tags[i].text == "Price":
                                price_index = i
                        if tags[i].text == "VWR Catalog Number":
                                VMR_index = i
                        #Want first set of indices since there may be duplicate productHeaders
                        if description_index != None and price_index != None and VMR_index != None:
                                break

                #Get various models of item and append description to title
                models = new_soup.find_all('td',class_="productGrid")
                titles_for_model = models[description_index].text.strip()
                #Image and url should be the same
                for model_title in titles_for_model:
                        # Will override previous title
                        new_result.title = title + " " + model_title
                        x = models[VMR_index-1].text
                        p = ''.join(str("L"+x+"EA").split())
                        #print new_soup.find_all('td',id=p)
                        print ":("
                        #results.append(new_result)
                #print models[price_index-1].find_next('td').text.strip()
                #print "........"
        #print "oh?"
        return results

def main():
    print extract_results("double buret","new")

if __name__ == "__main__": main()
