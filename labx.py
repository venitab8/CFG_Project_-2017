"""
@author Venita Boodhoo
Website: LabX
Status: Complete
Comment: For both new and used equipment
"""

import urllib.request
import util 
import time
from bs4 import BeautifulSoup
from Result import Result
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

MAIN_URL = "https://www.labx.com/search?sw="
HOME_URL = "https://www.labx.com" 
DELIMITER = "+"

def extract_results(item,condition=None):
        #Url is extended based on condition
        if condition == "new":
                url = util.create_url(MAIN_URL,item,DELIMITER) + "&condition=468"
        else:
                url = util.create_url(MAIN_URL,item,DELIMITER) + "&condition=467,469"     
        results=[]
        headers={
        'Host': 'www.labx.com',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'Referer': 'https://www.labx.com/item/vacuum-pump-230-v-50-hz/12183467',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'User-Agent': 'Chrome/80.0.3987.132, Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-site',
        'Upgrade-Insecure-Requests':'1',
        'x-runtime':'148ms'}
        #Check if page has data
        try:
            path_to_chromedriver = 'chromedriver.exe'
            option = webdriver.ChromeOptions()
            option.add_argument('headless')
            browser = webdriver.Chrome(executable_path = path_to_chromedriver,options=option)
            browser.get(url)
            time.sleep(5)
            soup = BeautifulSoup(browser.page_source,'html.parser')
            rows = soup.find_all('div',class_='product-card')
        except:
                  return []
        #Get 1st 10 results only
        for i in range(len(rows)):
                  row = rows[i]
                  new_result = Result(row.find('a', class_='card-title').text)
                  new_result.set_url(HOME_URL + row.find('a').get('href'))
                  new_result.set_price(util.get_price(row.find(class_='price').get_text()))
                  number = util.get_price(new_result.get_title())
                  new_result.set_image_src(row.find('div', class_='card-img-top').find("img").get("src"))
                  if util.is_valid_price(new_result.get_price()):
                          results.append(new_result)
                          if len(results) == 9:
                                  break
        return results

def main():
    print (extract_results("vacuum pump", "used"))

if __name__ == "__main__": main()
