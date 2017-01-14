# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 15:21:14 2017

@author: thotran
"""
main_url='http://www.medwow.com/tag/fronthandler/browse?actions=sales&searchstring='
def search_url(search_word):
    if len(search_word)==0:
        return 'Please use a keyword for searching'
    if ' ' in search_word:
        search=search_word.replace(' ', '+')
    else:
        search=search_word
    return main_url+search
    

def equipments(search_word):
    web=search_url(search_word)
    page =urllib2.urlopen(web).read()
    soup=BeautifulSoup(page)
    product_grid=soup.find('div', class_='pagebody')
    equips=[]
    for equip in product_grid.find_all('div')[2::]:
        print equip
        photo=equip.find('div',class_='image')
        print photo
        #photo=equip.find('div',class_='image').find('img').get('src')
        url=equip.find('a').get('href')
        price=equip.find('div', class_='price').find('span').find(text=True)
        title=equip.find('div', class_='item_details').find_all(text=True)
        equipment=Result(title)
        equipment.url=url
        equipment.image_src=photo
        equipment.price=price
        equips.append(equipment)
    return equips
    
print(equipments('centrifuge'))