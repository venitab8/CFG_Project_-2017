"""
@author Venita Boodhoo
Website: LabX
Status: Complete
Comment: For both new and used equipment
"""

import urllib.request
import util 
from Result import Result
import requests

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
        #Check if page has data
        try:
            soup = util.check_exceptions(url)
            table = soup.find('div', class_='product-grid')
            rows=table.find_all('div',class_='product-card')
        except:
                  return []
        #Get 1st 10 results only
        for i in range(len(rows)):
                  row= rows[i]
                  print(row.contents)
                  new_result = Result(row.find('a', class_='card-title').text)
                  new_result.url = HOME_URL + row.find('a').get('href')
                  new_result.price = util.get_price(row.find(class_='price').get_text())
                  number = util.get_price(new_result.title)
                  #print((row.find('div', class_='card-img-top').contents))
                  #new_result.image_src = row.find_all('src')
                  if util.is_valid_price(new_result.price):
                          results.append(new_result)
                          if len(results) == 9:
                                  break
        return results

def main():
    print (extract_results("vacuum pump", "new"))

if __name__ == "__main__": main()
