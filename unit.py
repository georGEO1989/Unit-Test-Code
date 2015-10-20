'''
name = raw_input("Please Enter your name: ")
name = name.title()
'''
class MyUser:

	def first_name(self):
		name = raw_input("What is your name?")

	def zipcode(self):
		zipcode = raw_input("What is your name?")

	def __init__(self, user):
		self.user = user

new = MyUser

print MyUser