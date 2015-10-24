import random

name = raw_input("Please Enter your name: ")
name = name.title()

class MyUser:
	'Create new user class'
	def __init__(self, name, zipcode):
		self.name = name
		self.zipcode = zipcode
		'''
		# figure out the best way to create a unique_id
		unique_id = uuid.uuid4()

		self.unique_id = unique_id
		'''

class PasswordGen:
	'Create password for user'
	def __init__(self):
		alphabet = "abcdefghijklmnopqrstuvwxyz"
		upperalphabet = alphabet.upper()
		pw_len = 8
		pwlist = []

		for i in range(pw_len//3):
		    pwlist.append(alphabet[random.randrange(len(alphabet))])
		    pwlist.append(upperalphabet[random.randrange(len(upperalphabet))])
		    pwlist.append(str(random.randrange(10)))
		for i in range(pw_len-len(pwlist)):
		    pwlist.append(alphabet[random.randrange(len(alphabet))])

		random.shuffle(pwlist)
		pwstring = "".join(pwlist)

		self.password = pwstring	


new = MyUser("Joey", 02302)
pwd = PasswordGen()

print new