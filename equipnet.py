import urllib2
from bs4 import BeautifulSoup

MAIN_URL= "http://www.equipnet.com/search/?q="

def create_url(search_term):
	specific_url=MAIN_URL
	search_words=search_term.split()
	for i in range(len(search_words)):
		if i!=0:
			specific_url.append("%20"+ search_words[i])
		else:
			specific_url.append(search_words[i])
	return specific_url

def extract_results(search_term):
	page=urllib2.urlopen(create_url(search_term))
	soup = BeautifulSoup(page)