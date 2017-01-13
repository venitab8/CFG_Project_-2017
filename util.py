import re
import string
import numpy
from Result import *
#Helper function to get price
def get_price(price):
    #price input is string
  allow = string.digits
  number = re.sub('[^%s]' %allow,'',price)
  return number


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
    
    
        
        