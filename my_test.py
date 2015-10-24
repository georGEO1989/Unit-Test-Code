import unittest
from unit import new
from unit import pwd

class UserTests(unittest.TestCase):
	def test_false(self):
		self.assertFalse(2 == 3)	
	
	def test_cap(self):
		self.assertTrue(new.name[0].isupper())

	def test_user(self):
		self.assertTrue(new.name)	
		self.assertTrue(new.zipcode)

	def test_password(self):
		self.assertTrue(pwd.password)	

if __name__ == '__main__':
	unittest.main()		