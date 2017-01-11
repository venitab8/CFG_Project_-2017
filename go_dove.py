# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 00:49:07 2017

@author: thotran
"""
main_url='http://www.go-dove.com/en/auction/search?cmd=results&fromsearch=true&words='

def search_url(search_word):
    if ' ' in search_word:
        search=search_word.replace(' ', '+')
    else:
        search=search_word
    return main_url+search+'&Submit='