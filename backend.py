from Result import Result
#import the 15 websites
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
import go_dove
import sibgene

import util 
import math

FUNCTIONS=[ebay.extract_results, marshallscientific.extract_results, equipnet.extract_results, google.extract_results, medwow.extract_results, used_line.extract_results \
eurekaspot.extract_results, labcommerce.extract_results, newlifescientific.extract_results, biosurplus.extract_results, sci_bay.extract_results, \
dotmed.extract_results, go_dove.extract_results, sibgene.extract_results, labx.extract_results] #sibgene and labx are the slowest websites to scrape from

MATCH_RATIO=.8

MAX_RESULTS=10

MIN_RESULTS=3


'''
searches the 15 websites until MAX_RESULTS close results are found or all the websites are searched
returns searchSuccessful (boolean), message, results
'''
def do_search(search_term, condition=None):
	results=[]
	for func in FUNCTIONS:
		website_results=func(search_term, condition)
		for website_result in website_results:
			if is_close_match(search_term, website_result.title):
				results.append(website_result)
			if len(results) >=MAX_RESULTS:
				return true, "", results
		if len(results) >= MAX_RESULTS:
			return true, "", results
	if len(results) < MIN_RESULTS:
		return false, "Fewer than %s results found" MIN_RESULTS, results


'''
checks if the result contains at least MATCH_RATIO of the search words
'''
def is_close_match(search_term, result_term):
	search_words=search_term.split()
	match_number=0
	for word in search_words:
		if word in result_term:
			match_number+=1
	return match_number >= math.ceil(len(search_words)*MATCH_RATIO)