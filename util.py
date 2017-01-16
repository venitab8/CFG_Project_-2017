import re
import string
import numpy
from Result import *

'''
Takes in a string containing the price of the equipment and results the price only (decimal in a string)
@param price a String of text containing the price of the equipment
@return number a String containing only numbers and a decimal pt representing the price of the equipment
'''
def get_price(price):
    #price input is string
    allow = string.digits + '.,'
    number = re.sub('[^%s]' %allow,'',price)
    return number.strip()

def is_valid_price(price):
    price=get_price(price)
    return bool(price)


def create_url(main_url, search_term, delimiter):
    specific_url=main_url
    search_words=search_term.split()
    for i in range(len(search_words)):
        if i!=0:
            specific_url= specific_url + delimiter+ search_words[i]
        else:
            specific_url= specific_url + search_words[i]
    return specific_url

def min_price(results):
    #results is list of result objects
    prices=[]
    for equip in results:
        if equip.price!=None and equip.price!='': 
            prices.append(equip.price)
        
    return min(prices)
    
def max_price(results):
    prices=[]
    for equip in results:
        if equip.price!=None and equip.price!='': 
            prices.append(equip.price)
        
    return max(prices)
    
def median_price(results):
    prices=[]
    for equip in results:
        if equip.price!=None and equip.price!='': 
            prices.append(equip.price)
    return numpy.median(numpy.array(prices))
    
