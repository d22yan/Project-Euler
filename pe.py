#!/user/bin/python

import itertools

def GenerateCombinations(inputList, inputlength):
	return itertools.combinations(inputList, inputlength)

def GeneratePrimeFactors(number):
	PrimeFactors = []
	Factor = 2
	while number%Factor == 0:
		PrimeFactors.append(Factor)
		number /= Factor
	Factor += 1
	while Factor*Factor <= number:
		if number%Factor == 0:
			PrimeFactors.append(Factor)
			number /= Factor
		else:
			Factor += 2
	if number != 1:
		PrimeFactors.append(number)
	return PrimeFactors

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
#	Multiples of 3 and 5
#	Find the sum of all the multiples of 3 or 5
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
#	Find the sum of the even-valued terms of the Fibonacci sequence whose values does not exceed four million
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
#	Return the largest prime factor
def LargestPrimeFactor(number):
	if IsPrime(number):
		return number
	result = 2
	for counter in range(3, int(number**0.5)+2, 2):
		if IsPrime(counter) and number % counter == 0:
			result = counter
	return result

#	ID	4
#	Largest palindrome product
#	Find the largest palindrome made from the product of two 3-digit numbers
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
def SmallestMultiple(number=20):
	MaxPrimeFactorsDictionary = {}
	PrimeFactorsCount = {}
	Result = 1
	for counter in range(2,number+1):
		for PrimeFactor in GeneratePrimeFactors(counter): 
			if PrimeFactorsCount.has_key(PrimeFactor):
				PrimeFactorsCount[PrimeFactor] += 1
			else:
				PrimeFactorsCount[PrimeFactor] = 1
		for Key in PrimeFactorsCount:
			if MaxPrimeFactorsDictionary.has_key(Key) and MaxPrimeFactorsDictionary[Key] >= PrimeFactorsCount[Key]:
				continue
			MaxPrimeFactorsDictionary[Key] = PrimeFactorsCount[Key]
		PrimeFactorsCount.clear()
	for Key in MaxPrimeFactorsDictionary:
		Result *= Key**MaxPrimeFactorsDictionary[Key]
	return Result

#	ID	6
#	Sum square difference
#	Find the difference between the sum of the squares of the first hundred natural numbers and the square of the sum
def SumSquareDifference(number=100):
	Result = 0
	for Combination in GenerateCombinations(range(number+1),2):
		Result += 2*Combination[0]*Combination[1]
	return Result
