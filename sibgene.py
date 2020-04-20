"""
@author Venita Boodhoo
Website: SibGene
Status: Complete
Comment: This website contains used and new equipment
"""

import urllib.request
from bs4 import BeautifulSoup
import util
import time
from Result import Result
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

MAIN_URL = "https://sibgene.com/catalogsearch/result/?q="
DELIMITER = "+"

def extract_results(item,requested_condition=None):
        path_to_chromedriver = 'chromedriver.exe'
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        browser = webdriver.Chrome(executable_path = path_to_chromedriver,options=option)
        url = util.create_url(MAIN_URL,item,DELIMITER)
        browser.get(url)
        time.sleep(5)
        soup = BeautifulSoup(browser.page_source,'html.parser')
        results=[]
        #Check for data
        try:
                table = soup.find('div',class_='search results')
        except:
                return results
        #Get 1st 10 results only
        rows = table.find_all('li',class_='item product product-item')

        for i in range(len(rows)):
                row=rows[i]
                new_result = Result(row.find('a',class_='product-item-link').text.strip())
                new_result.set_url(row.find('a').get('href'))
                new_result.set_price(util.get_price(str(row.find('span',class_='price').find(text=True))\
                                   .encode('utf-8')[1:]))
                new_result.set_image_src(row.find('img').get('src'))
                browser.get(new_result.get_url())       
                new_soup = BeautifulSoup(browser.page_source,"html.parser")
                condition = new_soup.find('div',class_='product attribute description').find('div',class_='value').text
                conditions = ['new','New','used','Used']
                bad_condition_types = ['bad','poor','not working','broken','not functional']
                #Check for matching conditions
                for word in conditions:
                        if word in condition:
                                if (requested_condition == None and word.lower() == 'used') or \
                                        (requested_condition != None and requested_condition.lower()== word.lower()):
                                        #Only add working good equipment
                                        for type_word in bad_condition_types:
                                                if type_word not in condition and util.is_valid_price(new_result.get_price()):
                                                        results.append(new_result)
                                                        break
                                                if len(results) == 10:
                                                        return results
        return results

def main():
    print (extract_results("pump", "used"))
    
if __name__ == "__main__": main()
