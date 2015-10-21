import unittest
import unit

class MyTests(unittest.TestCase):
	def test_true(self):
		self.assertTrue(1 == 1)

	def test_false(self):
		self.assertFalse(2 == 3)	
	
	def test_cap(self):
		self.assertTrue(unit.name[0].isupper())

	def test_user(self):
		self.assertTrue(unit.new.name)	
		self.assertTrue(unit.new.zipcode)

if __name__ == '__main__':
	unittest.main()		