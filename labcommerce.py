"""
@author Venita Boodhoo
Website: LabCommerce
Status: Complete
Note: Sells used products only
"""

import urllib.request
from bs4 import BeautifulSoup
from util import *
from Result import Result


MAIN_URL = 'https://www.labcommerce.com'
SEARCH_URL = "https://www.labcommerce.com/searchresults.php?txtsearch="
DELIMITER = "+"

def extract_results(item,condition=None):
        results=[]
        if condition != 'new':
                page = urllib.request.urlopen(create_url(SEARCH_URL,item,DELIMITER)+"&image.x=0&image.y=0")
                soup = BeautifulSoup(page,"html.parser")
                table = soup.find_all('div',class_="search_result")
                
                for row in table:
                        match = False
                        new_result = Result(row.a.text)
                        url = re.sub('/catid/','.php?catid=',row.find('a').get('href'))
                        #Omit last slash
                        specific_url = re.sub('/prodid/','&prodid=',url)[:-1]
                        new_result.url = MAIN_URL + specific_url
                        new_soup = BeautifulSoup(urllib.request.urlopen(new_result.url),"html.parser")
                        #Omit surrounding text, get decimal only
                        new_result.price = get_price(str(new_soup.find('td',class_='price').find_all(text=True)[0]))
                        #Omit 1st char (a period)
                        new_result.image_src = MAIN_URL+new_soup.find('td',align='center')\
                                               .find('img').get('src')[1:]
                        bad_condition_types = ['bad','poor','not working','broken','not functional']
                        condition_type_text = new_soup.find(text='Condition:')
                        #Matches on condition and omits bad conditions
                        if condition_type_text != None:
                                condition_type = condition_type_text.find_next(text=True)
                                for word in bad_condition_types:
                                        if word not in condition_type and is_valid_price(new_result.price):
                                                match = True
                                if match:
                                        results.append(new_result)
                                if len(results) == 9:
                                        break
                        elif is_valid_price(new_result.price):
                                results.append(new_result)
                        if len(results) == 9:
                                break     
        return results

def main():
    print (extract_results("Vacuum Stainless Flex Hose"))

if __name__ == "__main__": main()
