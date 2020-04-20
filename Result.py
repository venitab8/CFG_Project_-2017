'''
Created by Abigail Katcoff (complete)

This class represents one search result corresponding to one item of equipment outputted by a search
'''

class Result: 
	def __init__(self, title):
		self.image_src="http://dhakaprice.com/images/No-image-found.jpg"
		self.title=title
		self.url=None
		self.price=None
		self.origin_website=None

	def __str__(self):
		string=""
		if self.title!=None:
			string=string+"title: " + self.title
		if self.image_src!=None:
			string=string+"\nimage source: "+ self.image_src
		if self.url!=None:
			string=string+ "\nurl: " + self.url
		if self.price!=None:
			string=string+ "\nprice: " + self.price
		if self.origin_website!=None:
			string=string+"\norigin website: " + self.origin_website
		return string + "\n"

	def __repr__(self):
		string=""
		if self.title!=None:
			string=string+"title: " + self.title
		if self.image_src!=None:
			string=string+"\nimage source: "+ self.image_src
		if self.url!=None:
			string=string+ "\nurl: " + self.url
		if self.price!=None:
			string=string+ "\nprice: " + self.price
		if self.origin_website!=None:
			string=string+"\norigin website: " + self.origin_website
		return string + "\n"
	
	def get_title(self):
		return self.title
		
	def get_url(self):
		return self.url 
	
	def get_price(self):
		return self.price 
		
	def set_title(self,x):
		self.title = x
	
	def set_image_src(self, x):
		self.image_src = x
	
	def set_url(self, x):
		self.url = x
		
	def set_price(self, x):
		self.price = x