from Result import Result
#import the 17 websites
import ebay
import marshallscientific
import equipnet
import google
import medwow
import used_line
import eurekaspot
import labcommerce
import newlifescientific
import labx
import biosurplus
import sci_bay
import dotmed
import sibgene
import daigger
import coleparmer
import ika

import util 
import math
import time 

USED_FUNCS=[equipnet.extract_results, \
labx.extract_results, \
ebay.extract_results, \
dotmed.extract_results, \
google.extract_results, \
biosurplus.extract_results, \
medwow.extract_results, \
labcommerce.extract_results, \
marshallscientific.extract_results, \
newlifescientific.extract_results, \
eurekaspot.extract_results, \
sci_bay.extract_results, \
sibgene.extract_results, \
used_line.extract_results ]

#TODO include coleparmer
#NEW_FUNCS=[daigger.extract_results, \
##ika.extract_results, \
#dotmed.extract_results, \
#ebay.extract_results, \
#google.extract_results, \
#labx.extract_results, \
#medwow.extract_results, \
#sibgene.extract_results
##coleparmer.extract_results
#] 

NEW_FUNCS=[daigger.extract_results, \
dotmed.extract_results, \
ebay.extract_results, \
google.extract_results, \
labx.extract_results, \
medwow.extract_results, \
sibgene.extract_results
] 

#WEBSITE_NAMES={ebay.extract_results : "ebay" , equipnet.extract_results : "equipnet" , google.extract_results : "google" , used_line.extract_results : "used line", \
#eurekaspot.extract_results : "eurekaspot", labcommerce.extract_results :"labcommerce", newlifescientific.extract_results :"newlifescientific", biosurplus.extract_results: "biosurplus" , sci_bay.extract_results : "sci_bay", \
#dotmed.extract_results : "dotmed" , sibgene.extract_results: "sibgene" , labx.extract_results : "labx", medwow.extract_results: "medwow", marshallscientific.extract_results: \
#"marshallscientific", daigger.extract_results: "daigger", coleparmer.gextract_results: "coleparmer", ika.extract_results: "ika"}

WEBSITE_NAMES={ebay.extract_results : "ebay" , equipnet.extract_results : "equipnet" , google.extract_results : "google" , used_line.extract_results : "used line", \
eurekaspot.extract_results : "eurekaspot", labcommerce.extract_results :"labcommerce", newlifescientific.extract_results :"newlifescientific", biosurplus.extract_results: "biosurplus" , sci_bay.extract_results : "sci_bay", \
dotmed.extract_results : "dotmed" , sibgene.extract_results: "sibgene" , labx.extract_results : "labx", medwow.extract_results: "medwow", marshallscientific.extract_results: \
"marshallscientific", daigger.extract_results: "daigger"}
MATCH_RATIO=.8

MAX_RESULTS=10

MIN_RESULTS=3


'''
searches a website until MAX_RESULTS close results are found
@param search_term: string, 
@param condition: string ("new" or "used") 
@param website_number: the index of the website to search
returns website_number_valid (boolean), message (string), results (list of Results)
'''
def search_a_website(search_term, condition=None, website_number=0):
    results=[]
    error_message=""
    function_list=NEW_FUNCS if condition =='new' else USED_FUNCS
    if website_number>=len(function_list):
        return False, error_message, []
    try:
        func=function_list[website_number]
        print "scraping ",  WEBSITE_NAMES[func]
        website_results=func(search_term, condition)
        for website_result in website_results:
            if is_close_match(search_term, website_result.title):
                results.append(website_result)
            if len(results) >=MAX_RESULTS:
                return True, error_message, results
    except Exception, e: 
        print "Error scraping ",  WEBSITE_NAMES[func]
        print "Error was: ", e.message 
        error_message=error_message + "Error scraping %s.\n" %(WEBSITE_NAMES[func])
    return True, error_message, results

'''
checks if the result contains at least MATCH_RATIO of the search words
search_term, result_term are strings
'''
def is_close_match(search_term, result_term):
    search_words=search_term.split()
    match_number=0
    for word in search_words:
        if word.lower().strip() in result_term.lower():
            match_number+=1
    return match_number >= math.ceil(len(search_words)*MATCH_RATIO)


def main():
    for i in range(10):
        print search_a_website("vacuum bump", condition='new', website_number=i)

if __name__ == "__main__": main()
