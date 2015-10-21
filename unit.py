name = raw_input("Please Enter your name: ")
name = name.title()

class MyUser:
	'Create new user class'
	def __init__(self, name, zipcode):
		self.name = name
		self.zipcode = zipcode

new = MyUser("Joey", 02302)