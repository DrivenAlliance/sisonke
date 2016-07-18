#The aim of Fizz Buzz is to create a method that when you give a number 
#divisable by 3 the it returns Fizz, 
#if it's divisable by 5 you return buzz and 
#divisable by 3 qnd 5 you return FizzBuzz. 
#If not divisable by either, return the number.
#i.e. 3 will return Fizz, 5 will return Buzz, 15 will return FizzBuzz, 7 will return 7

import unittest
class FizzBuzzCalculator:
	def calculate(self,value):
		if value == 3:
			return "Fizz"
		if value ==5:
			return "Buzz"
		
		
				
class FizzBuzzTests(unittest.TestCase):
	
	def test_3_is_equal_to_fizz(self):
		fizz_buzz_calculator = FizzBuzzCalculator()
		answer = fizz_buzz_calculator.calculate(3)
		self.assertEqual(answer,"Fizz")
	
	def test_5_is_equal_to_buzz(self):
		fizz_buzz_calculator = FizzBuzzCalculator()
		answer = fizz_buzz_calculator.calculate(5)
		self.assertEqual(answer,"Buzz")
	
	def test_divisable_by_3_is_equal_to_fizz(self):
		fizz_buzz_calculator = FizzBuzzCalculator()
		answer = fizz_buzz_calculator.calculate(6)
		self.assertEqual(answer,"Fizz")			
		

if __name__ == '__main__':
    unittest.main()	

