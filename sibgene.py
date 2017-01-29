"""
@author Venita Boodhoo
Website: SibGene
Status: Complete
"""

import urllib2
from bs4 import BeautifulSoup
from util import *
from Result import Result

MAIN_URL = "http://sibgene.com/index.php/catalogsearch/result/?q="
DELIMITER = "+"

def extract_results(item,requested_condition=None):
        page = urllib2.urlopen(create_url(MAIN_URL,item,DELIMITER))
        soup = BeautifulSoup(page,"html.parser" )
        results=[]
        #Check for data
        try:
                table = soup.find_all('li',class_='item')
        except:
                return results
        #Get 1st 10 results only
        for i in range(min(len(table), 10)):
                row=table[i]
                new_result = Result(row.find('a').get('title'))
                new_result.url = row.find('a').get('href')
                new_result.price = get_price(str(row.find('span',class_='price').find_all(text=True)[0])\
                                   .encode('utf-8')[1:])
                new_result.image_src = row.find('img').get('src')
                
                specific_page = urllib2.urlopen(new_result.url)
                new_soup = BeautifulSoup(specific_page,"html.parser")
                condition = new_soup.find('div',class_='product-collateral').find('div',class_='std').text
                conditions = ['new','New','used','Used']
                bad_condition_types = ['bad','poor','not working','broken','not functional']
                #Check for matching conditions
                for word in conditions:
                        if word in condition:
                                if (requested_condition == None and word.lower() == 'used') or \
                                        (requested_condition != None and requested_condition.lower()== word.lower()):
                                        #Only add working good equipment
                                        for type_word in bad_condition_types:
                                                if type_word not in condition and is_valid_price(new_result.price):
                                                        results.append(new_result)
        return results

def main():
    print extract_results("bio pump")
    
if __name__ == "__main__": main()
