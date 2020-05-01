"""
@author Venita Boodhoo
Website: daigger
Status: Complete
Comments: For new equipment only
"""
import urllib.request
import time
from bs4 import BeautifulSoup
from util import *
from Result import Result
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

MAIN_URL = "https://www.daigger.com/searchresults?qs="
HOME_URL = "https://www.daigger.com"                    
DELIMITER = "+"

def extract_results(item,condition=None):
        results=[]
        if condition != "new":
                return results
        headers={
        'Host': 'daigger-com.ecomm-nav.com',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'Referer': 'https://www.daigger.com/searchresults?qs=vacuum+pump',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'User-Agent': 'Chrome/80.0.3987.132, Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'cross-site',
        'Upgrade-Insecure-Requests':'1',
        'x-runtime':'148ms'}
        
        
        specific_url = create_url(MAIN_URL,item,DELIMITER)
        path_to_chromedriver = 'chromedriver.exe'
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        browser = webdriver.Chrome(executable_path = path_to_chromedriver,options=option)
        browser.get(specific_url)
        time.sleep(5)
        
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        table = soup.find('div',id = "ListingProducts")
   
        #Check for data
        try:
                  #If items are a list
                  rows=table.find_all('div',class_="ejs-productitem span3")
        except:
                  try:
                          
                          #Returns one item on a specific pg
                          title = soup.find('a',class_='product-title').get('title')
                          url = soup.find('a',class_='product-title').get('href')
                          img_src = soup.find('div',class_='box-photo').find('img').get('src')
                          new_result = Result(title)
                          new_result.set_url(url)
                          new_result.set_image_src(img_src)
                          browser.get(new_result.get_url())       
                          new_soup = BeautifulSoup(browser.page_source,"html.parser")
                          items = new_soup.find_all('tr',class_='ejs-addtocart-section')
                          for item in items:
                                #Supplier Number
                                supplier = item.find('span',class_='supplier-code')
                                if supplier != None:
                                        new_result.set_title(title + supplier.text)
                                new_result.set_price(item.find('strong',class_='price').text)
                                currency = item.find('span',itemprop='priceCurrency')
                                
                                if (currency == None or currency.text == "USD") and is_valid_price(new_result.get_price()):
                                        results.append(new_result)
                                        if len(results) == 9:
                                                break
                                new_result = Result(title)
                                new_result.set_url(url)
                                new_result.set_image_src(img_src)
                          
                          return results
                  #No results found
                  except:
                          return []
        
        #For multiple items  
        for row in rows:
                new_result = Result(row.find('a',class_='product-title').get('title'))
                new_result_title_temp = new_result.get_title()[:]
                new_result.set_url("https://" + row.find('a').get('href'))
                new_result.set_image_src(row.find('img').get('src'))
                browser.get(new_result.get_url())                
                new_soup = BeautifulSoup(browser.page_source,"html.parser")
                #Get all models of products from specific page
                items = new_soup.find_all('tr',class_='ejs-addtocart-section')
                for item in items:
                        #Supplier Number
                        supplier = item.find('span',class_='supplier-code')
                        if supplier != None:
                                new_result.set_title(new_result_title_temp + supplier.text)
                        new_result.set_price(item.find('strong',class_='price').text)
                        currency = item.find('span',itemprop='priceCurrency')
                        
                        if (currency == None or currency.text == "USD") and is_valid_price(new_result.get_price()):
                                results.append(new_result)
                                if len(results) == 10:
                                        break
                        new_result = Result(row.find('img').get('title'))
                        new_result.set_url(row.find('a').get('href'))
                        new_result.set_image_src(row.find('img').get('src'))
                if len(results) == 10:
                        break
        return results

def main():
    print (extract_results("Polypropylene Volumetric Flasks","new"))

if __name__ == "__main__": main()
