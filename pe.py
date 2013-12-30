#!/user/bin/python
import itertools

def IsPrime(number):
	if number < 2:
		return False
	if number == 2:
		return True
	if not number & 1:
		return False
	for Counter in range(3, int(number**0.5)+2, 2):
		if number % Counter == 0:
			return False
	return True

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

def GeneratePrimes(size):
	PrimeList = []
	Counter = 3
	IsNotPrime = False
	if size < 1:
		return PrimeList
	PrimeList.append(2)
	size -= 1
	while size:
		IsNotPrime = False;
		for Prime in PrimeList:
			if Counter%Prime == 0:
				IsNotPrime = True
				break
		if not IsNotPrime:
			print str(size) + " " + str(Counter)
			PrimeList.append(Counter)
			size -= 1
		Counter += 2;
	return PrimeList;


def ReverseString(string):
	return string[::-1]

#	ID	1
#	Multiples of 3 and 5
#	Find the sum of all the multiples of 3 or 5
def MultiplesOf3And5(number):
	result = 0
	for Counter in range(0,number,3):
		result += Counter
	for Counter in range(0,number,5):
		if Counter % 3 != 0:
			result += Counter
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
	for Counter in range(3, int(number**0.5)+2, 2):
		if IsPrime(Counter) and number % Counter == 0:
			result = Counter
	return result

#	ID	4
#	Largest palindrome product
#	Find the largest palindrome made from the product of two 3-digit numbers
def LargestPalindromeProduct(digit=3):
	HalfOfMaxPalindromeNumber = 0
	PalindromeString = ""
	for Counter in range(0,digit-1):
		HalfOfMaxPalindromeNumber += 9
		HalfOfMaxPalindromeNumber *= 10
	HalfOfMaxPalindromeNumber += 8
	for Counter in range(int(HalfOfMaxPalindromeNumber), 10**(digit-1), -1):
		PalindromeString = str(Counter) + ReverseString(str(Counter))
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
	for Counter in range(2,number+1):
		for PrimeFactor in GeneratePrimeFactors(Counter): 
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

#	ID	7
#	10001st prime
#	Find the 10 001st prime number
def NthPrime(Size=10001):
	return GeneratePrimes(Size)[-1]

#	ID	8
#	Largest product in a series
# 	Find the greatest product of five consecutive digits in the 1000-digit number
def LargestProductInASeries(consecutiveDigits, number=7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450):
	ProductList = []
	Length = len(str(number))
	Result = 0
	StringNumberList = list(str(number))
	for index in range(0, Length-consecutiveDigits+1):
		Product = 1
		for counter in range(0, consecutiveDigits):
			Product *= int(StringNumberList[index+counter])
		ProductList.append(Product)
	for Product in ProductList:
		if Product > Result:
			Result = Product
	return Result

#	ID 	9
#	Special Pythagorean triplet
#	Find the product of abc where there exists exactly one Pythagorean triplet for which a + b + c = 1000
def SpecialPythagoreanTriple(number=1000):
	for a in range(1, number):
		for b in range(1, number):
			c = (a**2 + b**2)**(0.5)
			if (a + b + c) == number:
				print str(a) + " " + str(b)+ " " + str(c)
				return a*b*c
	return

#	ID 	10
#	Summation of primes
#	Find the sum of all the primes below two million
def SummationOfPrimes(number=2000000):
	if number <= 1:
		return 
	Result = 0
	PrimeList = list(range(3,number,2))
	SquaredNumberIndex = 0
	SquaredNumber = int(number**0.5) + 2
	for Counter in range(len(PrimeList)):
		if PrimeList[Counter] > SquaredNumber:
			SquaredNumberIndex = Counter
			break
	for Index in range(0,SquaredNumberIndex+1):
		Length = len(PrimeList)
		Index2 = Index + 1
		while Index2 < Length:
			if PrimeList[Index2]%PrimeList[Index] == 0:
				print str(PrimeList[Index]) + " " + str(PrimeList[Index2])
				PrimeList.pop(Index2)
				Length -= 1
				Index2 -= 1
			Index2 += 1
	for Prime in PrimeList:
		Result += Prime
	print PrimeList
	return Result + 2

#	ID 	11
#	Largest product in a grid
#	Find the greatest product of four adjacent numbers in the any direction in the 20x20 grid
def LargestProductInAGrid(adjacentNumbers, number=[[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],[49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],[81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],[52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],[22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],[24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],[32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],[67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],[24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],[21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],[78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],[16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],[86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],[19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],[04, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],[88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],[04, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],[20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],[20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],[01, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]):
	Result = 0
	for CoordinateX in range(0,20):
		for CoordinateY in range(0,20):
			ProductA = ProductB = ProductC = ProductD = 1
			for Next in range(0,adjacentNumbers):
				if CoordinateX + Next < 20:
					ProductA *= number[CoordinateX+Next][CoordinateY]
				if max(CoordinateX,CoordinateY) + Next < 20:
					ProductB *= number[CoordinateX+Next][CoordinateY+Next]
				if CoordinateY + Next < 20:
					ProductC *= number[CoordinateX][CoordinateY+Next]
				if CoordinateX + Next < 20 and CoordinateY - Next >= 0:
					ProductD *= number[CoordinateX+Next][CoordinateY-Next]
			MaxProduct = max(ProductA, ProductB, ProductC, ProductD)
			if MaxProduct > Result:
				Result = MaxProduct
	return Result
