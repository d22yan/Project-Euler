#!/user/bin/python

def IsPrime(number):
	if number < 2:
		return False
	if number == 2:
		return True
	if not number & 1:
		return False
	for counter in range(3, int(number**0.5)+2, 2):
		if number % counter == 0:
			return False
	return True

def ReverseString(string):
	return string[::-1]

#	ID	1
# 	Multiples of 3 and 5
#	Finds the sum of all the multiples of 3 or 5
def MultiplesOf3And5(number):
	result = 0
	for counter in range(0,number,3):
		result += counter
	for counter in range(0,number,5):
		if counter % 3 != 0:
			result += counter
	return result

#	ID	2
#	Even Fibonacci numbers
#	Finds the sum of the even-valued terms of the Fibonacci sequence whose values does not exceed four million
def EvenFibonacciNumbers(number):
	result = 0
	x1 = 1
	x2 = 2
	while x2 <= number:
		result += x2 if x2 % 2 == 0 else 0
		temp = x2
		x2 = x2 + x1
		x1 = temp
	return result

#	ID	3
#	Largest prime factor
#	Returns the largest prime factor
def LargestPrimeFactor(number):
	result = 1
	for counter in range(1, int(number**0.5)+2, 2):
		if IsPrime(counter) and number % counter == 0:
			result = counter
	return result

#	ID	4
#	Largest palindrome product
#	Finds the largest palindrome made from the product of two 3-digit numbers
def LargestPalindromeProduct(digit=3):
	HalfOfMaxPalindromeNumber = 0
	PalindromeString = ""
	for counter in range(0,digit-1):
		HalfOfMaxPalindromeNumber += 9
		HalfOfMaxPalindromeNumber *= 10
	HalfOfMaxPalindromeNumber += 8
	for counter in range(int(HalfOfMaxPalindromeNumber), 10**(digit-1), -1):
		PalindromeString = str(counter) + ReverseString(str(counter))
		PalindromeNumber = int(PalindromeString)
		if not IsPrime(PalindromeNumber):
			for factor in range(10**(digit-1)+1, 10**(digit)-1):
				if PalindromeNumber%factor == 0:
					factor2 = PalindromeNumber/factor
					if len(str(factor2)) == digit:
						return PalindromeNumber
	return
	
#	ID	5
#	Smallest multiple
#	Return the smallest positive number that is evenly divisible by all of the numbers from 1 to 20
def SmallestMultiple(number=10):
	return
