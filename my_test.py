import unittest
import unit

class UserTests(unittest.TestCase):
	def test_false(self):
		self.assertFalse(2 == 3)	
	
	def test_cap(self):
		self.assertTrue(unit.name[0].isupper())

	def test_user(self):
		self.assertTrue(unit.new.name)	
		self.assertTrue(unit.new.zipcode)

	def test_password(self):
		self.assertTrue(unit.pwd.password)	

if __name__ == '__main__':
	unittest.main()		