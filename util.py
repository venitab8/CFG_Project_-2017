import re
import string

#Helper function to get price
def get_price(price):
  allow = string.digits
  number = re.sub('[^%s]' %allow,'',price)
  return number
