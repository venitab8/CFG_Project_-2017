'''
Created by Abigail Katcoff
Modified by Venita Boodhoo (04/2020)
New and Used Equipment
'''

import util
import urllib.request
from bs4 import BeautifulSoup
from Result import Result
import requests

HOME_URL='https://www.google.com'
MAIN_URL='https://www.google.com/search?output=search&tbm=shop&q='
DELIMITER= '+'

def extract_results(search_term, condition=None):
        url=util.create_url(MAIN_URL, search_term, DELIMITER)
        if condition=='new':
            url = url + '&tbs=vw:l,mr:1,new:1'
        else:
            url = url + '&tbs=vw:l,mr:1,new:3'
        print(url)
        headers={
        'Connection': 'keep-alive',
        'Accept': 'text/html',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
        r = requests.get(url,timeout=5,headers=headers)
        soup = BeautifulSoup(r.content,"html.parser")
        table=soup.find('div', class_='sh-pr__product-results')
        try:
                rows=table.findAll('div', class_='sh-dlr__list-result')
                print(len(rows),"length")
        except:
                return []

        results=[]
        for row in rows:
                if condition!='new':
                    condition_text = str(row.find('span', class_='h1Wfwb O8U6h').text)
                    if (('used' not in condition_text) and ('refurbished' not in condition_text)):
                        #skip over items that do not say "used" when searching for used items 
                        continue
                if "eBay" in str(row.find('a', class_='shntl hy2WroIfzrX__merchant-name').text):
                        #many google results overlap with eBay. Do not include these.
                        continue
                new_result=Result(row.find('h3', class_='xsRiS').text)
                new_result.set_url(HOME_URL+row.find('a').get('href'))
                new_result.set_price(util.get_price(row.find('span','aria--hidden'=='true').text))
                # if condition!='new':
                    # new_result.set_image_src(row.find('img',class_='TL92Hc').get('src'))
                #r = requests.get(new_result.get_url(),timeout=5,headers=headers)
                #new_soup = BeautifulSoup(r.content,"html.parser")
                #new_result.set_image_src(new_soup.find('img',class_='sh-div__image sh-div__current').get('src'))
                if util.is_valid_price(new_result.get_price()):
                        results.append(new_result)
                        if len(results)==10:
                            return results
        return results


def main():
    print (extract_results("centrifuge","used"))

if __name__ == "__main__": main()
