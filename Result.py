class Result: 
	def __init__(self, title):
		self.image_src=None
		self.title=title
		self.url=None
		self.price=None
		self.condition=None

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
		if self.condition!=None:
			string=string+"\ncondition: " + self.condition
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
		if self.condition!=None:
			string=string+"\ncondition: " + self.condition
		return string+"\n"