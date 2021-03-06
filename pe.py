from collections import defaultdict
from datetime import date
from fractions import Fraction
from itertools import combinations
from itertools import permutations
from math import factorial
from math import sqrt
from sets import Set
import re

def Tree(): 
	return defaultdict(Tree)

def ConvertIntListToInt(numberList):
    Number = ''.join(map(str, numberList))
    return int(Number)

def ConvertStringListToInt(inputList):
	return int(''.join(inputList))

def FormulaTriangle(index):
	return index * (index + 1) / 2

def FormulaTriangleInverse(index):
	return (-1 + sqrt(8 * index + 1)) / 2

def FormulaPentagon(index):
	return index * (3 * index - 1) / 2

def FormulaPentagonInverse(index):
	return (1 + sqrt(24 * index + 1)) / 6

def FormulaHexagon(index):
	return index * (2 * index - 1)

def FormulaHexagonInverse(index):
	return (1 + sqrt(8 * index + 1)) / 4

def GeneratePrimeFactors(number):
	PrimeFactors = []
	Factor = 2
	while number % Factor == 0:
		PrimeFactors.append(Factor)
		number /= Factor
	Factor += 1
	while Factor*Factor <= number:
		if number % Factor == 0:
			PrimeFactors.append(Factor)
			number /= Factor
		else:
			Factor += 2
	if number != 1:
		PrimeFactors.append(number)
	return PrimeFactors

def GeneratePrimes(size):
	PrimeList = []
	if size < 1:
		return PrimeList
	PrimeList.append(2)
	size -= 1
	Number = 3
	while size:
		IsPrime = True
		for Prime in PrimeList:
			if Number % Prime == 0:
				IsPrime = False
				break
		if IsPrime:
			PrimeList.append(Number)
			size -= 1
		Number += 2
	return PrimeList

def GeneratePrimesRange(fromX, toY):
	PrimeList = []
	for Number in range(fromX, toY + 1):
		if IsPrime(Number):
			PrimeList.append(Number)
	return PrimeList

def IsPalindrome(inputString):
	PivotLength = len(inputString) / 2
	if PivotLength == 0:
		return True
	return inputString[:PivotLength] == ReverseString(inputString[-PivotLength:])

def IsPrime(number):
	if number < 2:
		return False
	if number == 2:
		return True
	if not number & 1:
		return False
	for Counter in range(3, int(number ** 0.5) + 1, 2):
		if number % Counter == 0:
			return False
	return True

def NumberOfDivisors(number):
	if number < 1:
		return 0
	if number == 1:
		return 1
	Counter = 0
	for Divisors in range(2,int(number ** 0.5) + 1):
		if number % Divisors == 0:
			Counter += 1
	return (Counter+1)*2

def NumberOfKCombinations(n,k):
    return factorial(n) / factorial(k) / factorial(n-k)

def NthTriangleNumber(triangleNumber):
	if triangleNumber < 0:
		return
	a = 1
	b = 1
	c = -2 * triangleNumber
	d = b ** 2 - 4 * a * c # n**2 + n - 2*TriangleLevel = 0
	if d > 0:
		Root = (-b + sqrt((b ** 2) - (4 * a * c))) / (2 * a)
		if Root % 1 == 0:
			return int(Root)
	return

def ReverseChained(chained):
	List = list(chained)
	List.reverse()
	return List

def ReverseString(string):
	return string[::-1]

def RotateString(inputString, rotateBy):
	return inputString[-rotateBy:] + inputString[0:-rotateBy] if rotateBy < len(inputString) else inputString

def SameDigit(Number):
	NumberString = str(Number)
	SameDigit = NumberString[0]
	for Digit in NumberString:
		if SameDigit != Digit:
			return False
	return True

def SumOfDivisors(number):
	if number < 1:
		return 0
	if number == 1:
		return 1
	SumOfDivisors = 1
	for Divisors in range(2, int(number ** 0.5) + 1):
		if number % Divisors == 0:
			SumOfDivisors += Divisors 
			if Divisors != number / Divisors:
				SumOfDivisors += number / Divisors
	return SumOfDivisors 

#	ID	1
#	Multiples of 3 and 5
#	Find the sum of all the multiples of 3 or 5
def MultiplesOf3And5(number=1000):
	MultiplesOf3And5 = 0
	for Counter in range(0, number, 3):
		MultiplesOf3And5 += Counter
	for Counter in range(0, number, 5):
		if Counter % 3 != 0:
			MultiplesOf3And5 += Counter
	return MultiplesOf3And5

#	ID	2
#	Even Fibonacci numbers
#	Find the sum of the even-valued terms of the Fibonacci sequence whose values does not exceed four million
def EvenFibonacciNumbers(number=4000000):
	EvenFibonacciNumbers = 0
	x1 = 1
	x2 = 2
	while x2 <= number:
		EvenFibonacciNumbers += x2 if x2 % 2 == 0 else 0
		Temp = x2
		x2 = x2 + x1
		x1 = Temp
	return EvenFibonacciNumbers

#	ID	3
#	Largest prime factor
#	Return the largest prime factor
def LargestPrimeFactor(number=600851475143):
	if IsPrime(number):
		return number
	LargestPrimeFactor = 2
	for Counter in range(3, int(number ** 0.5) + 1, 2):
		if IsPrime(Counter) and number % Counter == 0:
			LargestPrimeFactor = Counter
	return LargestPrimeFactor

#	ID	4
#	Largest palindrome product
#	Find the largest palindrome made from the product of two 3-digit numbers
def LargestPalindromeProduct(digit=3):
	HalfOfMaxPalindromeNumber = 0
	PalindromeString = ''
	for Counter in range(0,digit-1):
		HalfOfMaxPalindromeNumber += 9
		HalfOfMaxPalindromeNumber *= 10
	HalfOfMaxPalindromeNumber += 8
	for Counter in range(int(HalfOfMaxPalindromeNumber), 10 ** (digit - 1), -1):
		PalindromeString = str(Counter) + ReverseString(str(Counter))
		PalindromeNumber = int(PalindromeString)
		if not IsPrime(PalindromeNumber):
			for factor in range(10 ** (digit - 1) + 1, 10 ** (digit) - 1):
				if PalindromeNumber % factor == 0:
					factor2 = PalindromeNumber / factor
					if len(str(factor2)) == digit:
						return PalindromeNumber
	return
	
#	ID	5
#	Smallest multiple
#	Return the smallest positive number that is evenly divisible by all of the numbers from 1 to 20
def SmallestMultiple(number=20):
	MaxPrimeFactorsDictionary = {}
	PrimeFactorsCount = {}
	SmallestMultiple = 1
	for Counter in range(2, number + 1):
		for PrimeFactor in GeneratePrimeFactors(Counter): 
			PrimeFactorsCount[PrimeFactor] = PrimeFactorsCount[PrimeFactor] + 1 if PrimeFactorsCount.has_key(PrimeFactor) else 1
		for Key in PrimeFactorsCount:
			if MaxPrimeFactorsDictionary.has_key(Key) and MaxPrimeFactorsDictionary[Key] >= PrimeFactorsCount[Key]:
				continue
			MaxPrimeFactorsDictionary[Key] = PrimeFactorsCount[Key]
		PrimeFactorsCount.clear()
	for Key in MaxPrimeFactorsDictionary:
		SmallestMultiple *= Key**MaxPrimeFactorsDictionary[Key]
	return SmallestMultiple

#	ID	6
#	Sum square difference
#	Find the difference between the sum of the squares of the first hundred natural numbers and the square of the sum
def SumSquareDifference(number=100):
	SumSquareDifference = 0
	for Combination in combinations(range(number + 1),2):
		SumSquareDifference += 2 * Combination[0] * Combination[1]
	return SumSquareDifference

#	ID	7
#	10001st prime
#	Find the 10 001st prime number
def NthPrime(Size=10001):
	return GeneratePrimes(Size)[-1]

#	ID	8
#	Largest product in a series
# 	Find the greatest product of five consecutive digits in the 1000-digit number
def LargestProductInASeries(number=7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450):
	ConsecutiveDigits = 5
	ProductList = []
	Length = len(str(number))
	LargestProductInASeries = 0
	StringNumberList = list(str(number))
	for index in range(0, Length - ConsecutiveDigits + 1):
		Product = 1
		for counter in range(0, ConsecutiveDigits):
			Product *= int(StringNumberList[index + counter])
		ProductList.append(Product)
	for Product in ProductList:
		if Product > LargestProductInASeries:
			LargestProductInASeries = Product
	return LargestProductInASeries

#	ID 	9
#	Special Pythagorean triplet
#	Find the product of abc where there exists exactly one Pythagorean triplet for which a + b + c = 1000
def SpecialPythagoreanTriple(number=1000):
	for a in range(1, number):
		for b in range(1, number):
			c = (a ** 2 + b ** 2) ** (0.5)
			if (a + b + c) == number:
				return int(a * b * c)
	return

#	ID 	10
#	Summation of primes
#	Find the sum of all the primes below two million
def SummationOfPrimes(number=2000000):
	if number < 2:
		return 0
	SummationOfPrimes = 0
	for Counter in range (3, number + 1, 2):
		if IsPrime(Counter):
			SummationOfPrimes += Counter
	return SummationOfPrimes + 2

#	ID 	11
#	Largest product in a grid
#	Find the greatest product of four adjacent numbers in the any direction in the 20x20 grid
def LargestProductInAGrid(grid=[[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],[49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],[81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],[52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],[22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],[24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],[32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],[67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],[24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],[21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],[78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],[16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],[86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],[19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],[04, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],[88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],[04, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],[20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],[20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],[01, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]):
	AdjacentNumbers = 4
	LargestProductInAGrid = 0
	for CoordinateX in range(0, 20):
		for CoordinateY in range(0, 20):
			ProductA = ProductB = ProductC = ProductD = 1
			for Next in range(0, AdjacentNumbers):
				if CoordinateX + Next < 20:
					ProductA *= grid[CoordinateX + Next][CoordinateY]
				if max(CoordinateX,CoordinateY) + Next < 20:
					ProductB *= grid[CoordinateX + Next][CoordinateY + Next]
				if CoordinateY + Next < 20:
					ProductC *= grid[CoordinateX][CoordinateY + Next]
				if CoordinateX + Next < 20 and CoordinateY - Next >= 0:
					ProductD *= grid[CoordinateX + Next][CoordinateY - Next]
			MaxProduct = max(ProductA, ProductB, ProductC, ProductD)
			if MaxProduct > LargestProductInAGrid:
				LargestProductInAGrid = MaxProduct
	return LargestProductInAGrid

#	ID 	12
#	Highly divisible triangular number
#	Find the value of the first triangle number to have over five hundred divisors
def HighlyDivisibleTriangularNumber(divisors=500):
	if divisors < 1:
		return
	HighlyDivisibleTriangularNumber = 0
	Counter = 1
	while divisors > NumberOfDivisors(HighlyDivisibleTriangularNumber):
		HighlyDivisibleTriangularNumber += Counter
		Counter += 1
	return HighlyDivisibleTriangularNumber
	
#	ID 	13
#	Large sum
#	Find the first ten digits of the sum of the following one-hundred 50-digit numbers
def LargeSum(oneHundred50DigitNumbers=[37107287533902102798797998220837590246510135740250,46376937677490009712648124896970078050417018260538,74324986199524741059474233309513058123726617309629,91942213363574161572522430563301811072406154908250,23067588207539346171171980310421047513778063246676,89261670696623633820136378418383684178734361726757,28112879812849979408065481931592621691275889832738,44274228917432520321923589422876796487670272189318,47451445736001306439091167216856844588711603153276,70386486105843025439939619828917593665686757934951,62176457141856560629502157223196586755079324193331,64906352462741904929101432445813822663347944758178,92575867718337217661963751590579239728245598838407,58203565325359399008402633568948830189458628227828,80181199384826282014278194139940567587151170094390,35398664372827112653829987240784473053190104293586,86515506006295864861532075273371959191420517255829,71693888707715466499115593487603532921714970056938,54370070576826684624621495650076471787294438377604,53282654108756828443191190634694037855217779295145,36123272525000296071075082563815656710885258350721,45876576172410976447339110607218265236877223636045,17423706905851860660448207621209813287860733969412,81142660418086830619328460811191061556940512689692,51934325451728388641918047049293215058642563049483,62467221648435076201727918039944693004732956340691,15732444386908125794514089057706229429197107928209,55037687525678773091862540744969844508330393682126,18336384825330154686196124348767681297534375946515,80386287592878490201521685554828717201219257766954,78182833757993103614740356856449095527097864797581,16726320100436897842553539920931837441497806860984,48403098129077791799088218795327364475675590848030,87086987551392711854517078544161852424320693150332,59959406895756536782107074926966537676326235447210,69793950679652694742597709739166693763042633987085,41052684708299085211399427365734116182760315001271,65378607361501080857009149939512557028198746004375,35829035317434717326932123578154982629742552737307,94953759765105305946966067683156574377167401875275,88902802571733229619176668713819931811048770190271,25267680276078003013678680992525463401061632866526,36270218540497705585629946580636237993140746255962,24074486908231174977792365466257246923322810917141,91430288197103288597806669760892938638285025333403,34413065578016127815921815005561868836468420090470,23053081172816430487623791969842487255036638784583,11487696932154902810424020138335124462181441773470,63783299490636259666498587618221225225512486764533,67720186971698544312419572409913959008952310058822,95548255300263520781532296796249481641953868218774,76085327132285723110424803456124867697064507995236,37774242535411291684276865538926205024910326572967,23701913275725675285653248258265463092207058596522,29798860272258331913126375147341994889534765745501,18495701454879288984856827726077713721403798879715,38298203783031473527721580348144513491373226651381,34829543829199918180278916522431027392251122869539,40957953066405232632538044100059654939159879593635,29746152185502371307642255121183693803580388584903,41698116222072977186158236678424689157993532961922,62467957194401269043877107275048102390895523597457,23189706772547915061505504953922979530901129967519,86188088225875314529584099251203829009407770775672,11306739708304724483816533873502340845647058077308,82959174767140363198008187129011875491310547126581,97623331044818386269515456334926366572897563400500,42846280183517070527831839425882145521227251250327,55121603546981200581762165212827652751691296897789,32238195734329339946437501907836945765883352399886,75506164965184775180738168837861091527357929701337,62177842752192623401942399639168044983993173312731,32924185707147349566916674687634660915035914677504,99518671430235219628894890102423325116913619626622,73267460800591547471830798392868535206946944540724,76841822524674417161514036427982273348055556214818,97142617910342598647204516893989422179826088076852,87783646182799346313767754307809363333018982642090,10848802521674670883215120185883543223812876952786,71329612474782464538636993009049310363619763878039,62184073572399794223406235393808339651327408011116,66627891981488087797941876876144230030984490851411,60661826293682836764744779239180335110989069790714,85786944089552990653640447425576083659976645795096,66024396409905389607120198219976047599490197230297,64913982680032973156037120041377903785566085089252,16730939319872750275468906903707539413042652315011,94809377245048795150954100921645863754710598436791,78639167021187492431995700641917969777599028300699,15368713711936614952811305876380278410754449733078,40789923115535562561142322423255033685442488917353,44889911501440648020369068063960672322193204149535,41503128880339536053299340368006977710650566631954,81234880673210146739058568557934581403627822703280,82616570773948327592232845941706525094512325230608,22918802058777319719839450180888072429661980811197,77158542502016545090413245809786882778948721859617,72107838435069186155435662884062257473692284509516,20849603980134001723930671666823555245252804609722,53503534226472524250874054075591789781264330331690]):
	return str(sum(oneHundred50DigitNumbers))[:10]

#	ID 	14
#	Longest Collatz sequence
#	Find the starting number of a Collatz Sequence, under one million that produces the longest chain
def LongestCollatzSequence(number=1000000):
	LongestCollatzSequence = 1
	LongestChain = 0
	for number in range(2,number):
		StartingNumber = number
		Chain = 0
		while number > 1:
			number = number / 2 if number % 2 ==0 else 3 * number + 1
			Chain += 1
		if Chain > LongestChain:
			LongestCollatzSequence = StartingNumber
			LongestChain = Chain
	return LongestCollatzSequence

#	ID 	15
#	Lattice paths
#	Find the number of route are there through a 20x20 grid
def LatticePaths(gridSize=20):
	return factorial(gridSize * 2) / factorial(gridSize) ** 2

#	ID 	16
#	Power digit sum
#	Find the sum of the digits of the number 2**1000
def PowerDigitSum(exponent=1000):
	PowerString = str(2**exponent)
	PowerDigitSum = 0
	for Character in range(0, len(PowerString)):
		PowerDigitSum += int(PowerString[Character])
	return PowerDigitSum

#	ID 	17
#	Number letter counts
#	Find the number of letters would be used when 1 to 1000 are written out in words
def NumberLetterCounts():
	NumberOfCharactersFrom1To9 = 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4
	NumberOfCharactersFrom11To19 = + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8
	NumberOfCharactersFrom1To19 = NumberOfCharactersFrom1To9 + 3 + NumberOfCharactersFrom11To19
	NumberOfCharactersFrom1To99 = NumberOfCharactersFrom1To19 + 8*NumberOfCharactersFrom1To9 + 10*(6 + 6 + 5 + 5 + 5 + 7 + 6 + 6)
	NumberOfCharactersFrom1To999 = 10*NumberOfCharactersFrom1To99 + 100*NumberOfCharactersFrom1To9 + 900*7 + 9*99*3
	return NumberOfCharactersFrom1To999 + 3 + 8

#	ID 	18
#	Maximum path sum 1
#	Find the maximum total from top to bottom of a triangle
def MaximumPathSum1(numbers=[75, 95, 64, 17, 47, 82, 18, 35, 87, 10, 20, 4, 82, 47, 65, 19, 1, 23, 75, 3, 34, 88, 2, 77, 73, 7, 63, 67, 99, 65, 4, 28, 6, 16, 70, 92, 41, 41, 26, 56, 83, 40, 80, 70, 33, 41, 48, 72, 33, 47, 32, 37, 16, 94, 29, 53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14, 70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57, 91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48, 63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31, 4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]):
	TriangleNumber = len(numbers) # get triangle number from length of input
	NthTriangle = NthTriangleNumber(TriangleNumber)
	TriangleLevel = 0
	Counter = 0
	Grid = [[0 for x in range(15)] for x in range(15)]
	for Value in numbers:
		if TriangleLevel + 1 == Counter:
			TriangleLevel += 1
			Counter = 0
		Grid[TriangleLevel][Counter] = Value
		Counter += 1
	for Row in range(TriangleLevel, 0, -1):
		for Col in range(Row):
			Buffer = Grid[Row][Col]
			if Grid[Row][Col] < Grid[Row][Col + 1]:
				Buffer = Grid[Row][Col + 1]
			Grid[Row - 1][Col] += Buffer 
	return Grid[0][0]

#	ID 	19
#	Counting Sundays
#	Find the number of Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)
def CountingSundays(startingYear=1901):
	NumberOfSundays = 0
	startDate = date(startingYear, 1, 1)
	for Year in range(100):
		for Month in range(1,13):
			if date(startingYear + Year, Month, 1).weekday() == 6:
				NumberOfSundays += 1
	return NumberOfSundays

#	ID 	20
#	Factorial digit sum
#	Find the sum of the digits in the number 100!
def FactorialDigitSum(number=100):
	if number < 0:
		return
	SumOfTheDigits = 0
	FactorialString = str(factorial(number))
	Length = len(FactorialString)
	for Index in range(Length):
		SumOfTheDigits += int(FactorialString[Index])
	return SumOfTheDigits

#	ID 	21
#	Amicable numbers
#	Find the sum of all the amicable numbers under 1000
def AmicableNumbers(number=10000):
	if number < 1: 
		return
	SumOfAmicableNumbers = 0
	AmicableNumbers = [0 for x in range(number)]
	for Index in range(number):
		AmicableNumbers[Index] = SumOfDivisors(Index)
	for Index in range(number):
		AmicableNumbeOfIndex = AmicableNumbers[Index]
		if AmicableNumbeOfIndex < number and Index != AmicableNumbeOfIndex and Index == AmicableNumbers[AmicableNumbeOfIndex]:
			SumOfAmicableNumbers += Index
	return SumOfAmicableNumbers

#	ID 	22
#	Names scores
#	Find the total of all the name scores in the file, "names.txt". The name scores is the alphabetical value of a name multiplied by its position in the list.
def NamesScores(fileName='names.txt'):
	NameList = []
	Result = 0
	with open(fileName) as FileReader:
		NameList = sorted(FileReader.readline().replace('"','').upper().split(','))
	for Index in range(len(NameList)):
		for Character in NameList[Index]:
			Result += (ord(Character) - 64)*(Index + 1)
	return Result 

#	ID 	23
#	Non-abundant sums
#	Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers
def NonAbundantSums():
	AbundantNumbers = []
	NonAbundantSums = 0
	UpperLimit = 28124
	for Number in range(1, UpperLimit):
		if (Number % 2 == 0 or Number % 5 == 0) and SumOfDivisors(Number) > Number:
			AbundantNumbers.append(Number)
	NonSumsOfTwoAbundantNumbers = [1 for x in range(UpperLimit)]
	for AbundantNumber in AbundantNumbers:
		for AbundantNumber2 in AbundantNumbers:
			SumOfTwoAbundantNumbers = AbundantNumber + AbundantNumber2
			if SumOfTwoAbundantNumbers < UpperLimit: 
				NonSumsOfTwoAbundantNumbers[SumOfTwoAbundantNumbers] = 0
	for Index in range(UpperLimit):
		if NonSumsOfTwoAbundantNumbers[Index] == 1:
			NonAbundantSums += Index
	return NonAbundantSums

#	ID 	24
#	Lexicographic permutations
#	Find the millionth lexicographic permutation of the digits 0 to 9
def LexicographicPermutations(lexicographicPosition=1000000):
	Counter = 0
	Digit = 10
	Elements = [x for x in range(Digit)]
	Result = [0 for x in range(Digit)]
	for Index in range(Digit):
		PossiblePermutation = factorial(len(Elements) - 1)
		for Element in Elements:
			Counter += PossiblePermutation
			if Counter >= lexicographicPosition:
				Counter -= PossiblePermutation
				Result[Index] = Element
				Elements.remove(Element)
				break
	return ConvertIntListToInt(Result)

#	ID 	25
#	1000-digit Fibonacci number
#	Find the first term in the Fibonacci sequence to contain 1000 digits
def NDigitFibonacciNumber(digits=1000):
	if digits < 1:
		return
	if digits == 1:
		return 1
	NthTerm = 3
	x1 = 1
	x2 = 2
	while len(str(x2)) < digits:
		Temp = x2
		x2 = x2 + x1
		x1 = Temp
		NthTerm += 1
	return NthTerm

#	ID 	26
#	Reciprocal cycles
#	Find the value of the denominator < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part
def ReciprocalCycles(limit=1000): 
	Base = 10
	PrimeList = GeneratePrimesRange(0, limit)
	Regex = re.compile('^([0-9]+)\\1+$')
	for Prime in PrimeList[::-1]:
		CyclicNumber = (Base ** (Prime - 1) - 1) / Prime
		if not Regex.match(str(CyclicNumber).replace('0','')):
			return Prime
	return

#	ID 	27
#	Quadratic primes
#	Find the product of the coefficients, a and b, for the quadratic expression, n^2 + an +b that produces the maximum number of primes for consecutive values of n, starting with n = 0
def QuadraticPrimes(limit=1000):
	PrimeList = GeneratePrimesRange(0, limit)
	CoefficientBList = [-x for x in PrimeList[::-1]]
	CoefficientBList.extend(PrimeList)
	MaxCounter = 0
	for CoefficientB in PrimeList:
		for CoefficientA in range(-(limit - 1), limit):
			Counter = 1
			while IsPrime(Counter ** 2 + CoefficientA * Counter + CoefficientB):
				Counter += 1				
			if Counter > MaxCounter:
				MaxCounter = Counter
				MaxCoefficientA = CoefficientA
				MaxCoefficientB = CoefficientB
	return abs(MaxCoefficientA * MaxCoefficientB)

#	ID 	28
#	Number spiral diagonals
#	What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
def NumberSpiralDiagonals(diagonalLength=1001):
	if diagonalLength < 1 or diagonalLength % 2 == 0: 
		return 
	if diagonalLength == 1:
		return 1
	SpiralLevel = (diagonalLength - 1) / 2
	SpiralNumber = [1,1,1,1]
	SumSpiralDiagonals = 1
	for Level in range(SpiralLevel):
		for Direction in range(4):
			SpiralNumber[Direction] += 8 * Level + 2 * (Direction + 1)
			SumSpiralDiagonals += SpiralNumber[Direction]
	return SumSpiralDiagonals

#	ID 	29
#	Distinct powers
#	How many distinct terms are in the sequence generated by a^b, where 1 < a <= limit and 1 < b <= limit
def DistinctPowers(limit=100):
	DistinctPowers = Set([])
	for A in range(2, limit + 1): 
		for B in range(2, limit + 1):
			DistinctPowers.add(A ** B)
	return len(DistinctPowers)

#	ID  30
#	Digit fifth powers
#	Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
def DigitFifthPowers():
	Power = 5
	SumDigitNthPowers = 0
	for Counter in range(2, 10 ** (Power + 1)):
		StringCounter = str(Counter)
		SumPoweredStringCounter = 0
		for Digit in StringCounter:
			SumPoweredStringCounter += int(Digit) ** Power
		if Counter == SumPoweredStringCounter:
			SumDigitNthPowers += Counter
	return SumDigitNthPowers

#	ID  31
#	Coin sums
#	How many different ways can 2 pound be made using any number of coins?
def CoinSums(pound=200):
	Coins = [1, 2, 5, 10, 20, 50, 100, 200]
	Ways = [0 for x in range(pound+1)]
	Ways[0] = 1
	for Coin in Coins:
		for x in range(Coin, pound + 1):
			Ways[x] += Ways[x - Coin]
	return Ways[pound]

#	ID 	32
#	Pandigital products
#	Find the sum of all products whose multipilcand/multiplier/product identity can be written as a 1 through 9 pandigital.
def PandigitalProducts():
	AllDigit = [str(x) for x in range(1,10)]
	Permutation = permutations(AllDigit)
	PandigitalProducts = Set([])
	for Number in Permutation:
		Product = ConvertStringListToInt(Number[5:])
		for Position in range(1,5):
			Multiplicand = ConvertStringListToInt(Number[:Position])
			Mulitplier = ConvertStringListToInt(Number[Position:5])
			if Multiplicand * Mulitplier == Product:
				PandigitalProducts.add(Product)
				break
	return sum(PandigitalProducts)

#	ID 	33
#	Digit canceling fractions
#	Find the value of denominator product of four non trivial curious fraction in its lowest common terms.  
def DigitCancelingFractions():
	NominatorProduct = DenominatorProduct = 1
	for Denominator in range(11, 100):
		if Denominator % 10 != 0:
			for Nominator in range(11, 100):
				if Nominator % 10 != 0 and Nominator < Denominator:
					DenominatorString = str(Denominator)
					NominatorString = str(Nominator)
					NominatorDividedByDenominator = Nominator / float(Denominator)
					if len(DenominatorString) == 2 and len(NominatorString) == 2:
						if 	(NominatorString[0] == DenominatorString[0] and float(NominatorString[1]) / float(DenominatorString[1]) == NominatorDividedByDenominator) or (NominatorString[1] == DenominatorString[0] and float(NominatorString[0]) / float(DenominatorString[1]) == NominatorDividedByDenominator) or (NominatorString[0] == DenominatorString[1] and float(NominatorString[1]) / float(DenominatorString[0]) == NominatorDividedByDenominator) or (NominatorString[1] == DenominatorString[1] and float(NominatorString[0]) / float(DenominatorString[0]) == NominatorDividedByDenominator):
							NominatorProduct *= Nominator
							DenominatorProduct *= Denominator
	return Fraction(NominatorProduct, DenominatorProduct).denominator

#	ID 	34
#	Digit factorial
#	Find the sum of all numbers which are equal to the sum of the factorial of their digits
def DigitFactorial():
	SumDigitFactorial = 0
	for Number in range(3, factorial(9) * 7):
		NumberString = str(Number)
		if Number == sum([factorial(int(Digit)) for Digit in NumberString]):
			SumDigitFactorial += Number
	return SumDigitFactorial

#	ID 	35
#	Circular primes
#	Find the number of circular primes that are below one million
def CircularPrimes(limit=10**6):
	CircularPrimes = 0
	CircularPrimesCount = [0 for x in range(0, len(str(limit)))]
	for Number in range(3, limit, 2):
		if IsPrime(Number):
			NumberStringLength = len(str(Number))
			Counter = 0
			for RotateBy in range(1, NumberStringLength + 1):
				if not IsPrime(int(RotateString(str(Number), RotateBy))):
					break
				Counter += 1
			if Counter == NumberStringLength:
				CircularPrimes = CircularPrimes + NumberStringLength if SameDigit(Number) else CircularPrimes + 1
	return CircularPrimes

#	ID 	36
#	Double-base palindromes
#	Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2
def DoubleBasePalindromes(limit=10**6):
	Result = 0
	LimitBinary = bin(limit)[2:]
	Max = LimitBinary[:len(LimitBinary) / 2]
	for Number in range(1, int(Max, 2) + 1):
		PalindromeBinaryOdd = bin(Number)[2:] + ReverseString(bin(Number)[2:][:-1])
		PalindromeBinaryEven = bin(Number)[2:] + ReverseString(bin(Number)[2:])
		if IsPalindrome(str(int(PalindromeBinaryOdd, 2))):
			Result += int(PalindromeBinaryOdd, 2)
		if IsPalindrome(str(int(PalindromeBinaryEven, 2))):
			Result += int(PalindromeBinaryEven, 2)
	return Result

#	ID 	37
#	Truncatable primes
#	Find the sum of the only eleven primes that are both truncatable from left to right and right to left
def TruncatablePrimes():
	Counter = 0
	Result = 0
	PrimeCandidates = [3, 7]
	TruncatableNumbers = [1, 2, 3, 5, 7, 9]
	while Counter < 11:
		Buffer = list(PrimeCandidates)
		PrimeCandidates = []
		for PrimeCandidate in Buffer:
			if IsPrime(PrimeCandidate):
				Flag = True
				for Index in range(1, len(str(PrimeCandidate)) + 1):
					if not IsPrime(int(str(PrimeCandidate)[:Index])):
						Flag = False
						break
				if Flag and PrimeCandidate > 7:
					Result += PrimeCandidate
					Counter += 1
				for TruncatableNumber in TruncatableNumbers:
					PrimeCandidates.append(TruncatableNumber * 10 ** int(len(str(PrimeCandidate))) + PrimeCandidate)
	return Result

#	ID 	38
#	Pandigital multiples
#	What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
def PandigitalMultiples():
	Result = 0
	Permutations = ReverseChained(permutations([str(x) for x in range(1,9)]))
	for Permutation in Permutations:
		PandigitalString = str(9) + ''.join(Permutation)
		if (float(PandigitalString[4:]) / float(PandigitalString[:4]) == 2.0) or ((float(PandigitalString[2:5]) / float(PandigitalString[:2]) == 2.0) and (float(PandigitalString[5:9]) / float(PandigitalString[:2]) == 2.0)):
			Result = int(PandigitalString)
			return Result

#	ID 	39
#	Integer right triangles
#	For which value of perimeter greater or equal to 1000 of a right angle triangle, is the number of solutions maximised?
def IntegerRightTriangles(limit=1000):
	ChosenPerimeter = 0
	MaxSolution = 0
	for Perimeter in range(1, limit + 1):
		Counter = 0
		for A in range(1, int((Perimeter / (2 + sqrt(2))) + 1)):
			B = (Perimeter ** 2 - 2 * Perimeter * A) / (2 * Perimeter - 2 * A)
			if float(B).is_integer() and sqrt(A ** 2 + B ** 2).is_integer():				
				Counter += 1
		if Counter > MaxSolution:
			ChosenPerimeter = Perimeter
			MaxSolution = Counter
	return ChosenPerimeter

#	ID 	40
#	Champernowne's constant
#	If dn represents the nth digit of the irrational decimal fraction created by concatenating positive integers, find the value of the following expression. d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000
def ChampernownesConstant(maxDigit=6):
	Result = 1
	Counter = 0
	ChampernownesConstantString = ''
	while (len(ChampernownesConstantString) < 10 ** maxDigit):
		Counter += 1
		ChampernownesConstantString += str(Counter)
	for Number in range(0, maxDigit + 1):
		Result *= int(ChampernownesConstantString[10 ** Number - 1])
	return Result

#	ID 	41
#	Pandigital prime
#	What is the largest n-digit pandigital prime that exists?
def PandigitalPrime():
	for MaxNDigit in range(9, 0, -1):
		Digits = [x for x in range(1, MaxNDigit)]
		Permutations = ReverseChained(permutations(Digits))
		for Permutation in Permutations:
			PandigitalPrime = ConvertIntListToInt(Permutation)
			if IsPrime(PandigitalPrime):
				return PandigitalPrime

#	ID 	42
#	Coded triangle numbers
#	Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
def CodedTriangleNumbers(fileName='words.txt'):
	NameList = []
	Counter = 0
	with open(fileName) as FileReader:
		NameList = FileReader.readline().replace('"','').upper().split(',')
	for Index in range(len(NameList)):
		CharacterSum = 0
		for Character in NameList[Index]:
			CharacterSum += ord(Character) - 64
		if CharacterSum > 0 and sqrt(1 + 8 * CharacterSum).is_integer():
			Counter += 1
	return Counter

#	ID 	43
#	Sub-string divisibility
#	Find the sum of all 0 to 9 pandigital numbers with this property.
def SubStringDivisibility():
	Counter = 0
	DivisiblePrimes = GeneratePrimesRange(2,17)
	Permutations = permutations([str(x) for x in range(0, 10)])
	for Permutation in Permutations:
		Flag = True
		Index = 1
		PandigitalString = ''.join(Permutation)
		for DivisiblePrime in DivisiblePrimes:
			if int(PandigitalString[Index:Index + 3]) % DivisiblePrime != 0:
				Flag = False
			Index += 1
		if Flag:
			Counter += int(PandigitalString)
	return Counter

#	ID 	44
#	Pentagon numbers
#	Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk - Pj| is minimised; what is the value of D?
def PentagonNumbers():
	IndexK = 0
	IndexJ = 0
	while True:
		IndexK += 1
		IndexJ = IndexK
		while IndexJ > 1:
			IndexJ -= 1
			PentagonSum = FormulaPentagon(IndexK) + FormulaPentagon(IndexJ)
			PentagonDifference = FormulaPentagon(IndexK) - FormulaPentagon(IndexJ)
			if FormulaPentagonInverse(PentagonSum).is_integer() and FormulaPentagonInverse(PentagonDifference).is_integer():
				return int(PentagonDifference)

#	ID 	45
#	Triangular, pentagonal, and hexagonal
#	Find the next triangle number that is also pentagonal and hexagonal.
def TriangularPentagonalAndHexagonal(StartingIndex=285):
	Index = StartingIndex
	while True:
		Index += 1
		TriangleNumber = FormulaTriangle(Index)
		if FormulaPentagonInverse(TriangleNumber).is_integer() and FormulaHexagonInverse(TriangleNumber).is_integer():
			return TriangleNumber

#	ID 	46
#	Goldbach's other conjecture
#	What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
def GoldbachsOtherConjecture():
	OddNumber = 5
	while True:
		Flag = False
		SquareNumber = 1
		while True:
			Number = OddNumber - 2 * SquareNumber ** 2
			if Number < 0:
				break
			if IsPrime(Number):
				Flag = True
				break
			SquareNumber += 1
		if not Flag:
			return OddNumber
		OddNumber += 2
		while IsPrime(OddNumber):
			OddNumber += 2

#	ID 	47
#	Distinct primes factors
#	Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
def DistinctPrimesFactors(consecutive=4):
	ConsecutiveInteger = 1
	Counter = 0
	while True:
		ConsecutiveInteger += 1
		PrimeFactorSet = Set(GeneratePrimeFactors(ConsecutiveInteger))
		Counter = Counter + 1 if len(PrimeFactorSet) == consecutive else 0
		if Counter == consecutive:
			return ConsecutiveInteger - consecutive + 1

#	ID 	48
#	Self powers
#	Find the last ten digits of the sum of positive intergers to the exponent itself.
def SelfPowers(Limit=10**3):
	Result = 0
	Number = 0
	while Number < Limit:
		Number += 1
		Result += Number ** Number
	return str(Result)[-10:]

#	ID 	49
#	Prime permutations
#	What 12-digit number do you form by concatenating the three terms in an prime permutated arithemtic sequence?
def PrimePermutations():
	for FirstArithmeticSequence in range(10 ** 3, 10 ** 4):
		if IsPrime(FirstArithmeticSequence) and FirstArithmeticSequence != 1487:
			PermutationDigitSet = set([])
			BufferSet = set([])
			FirstArithmeticSequenceString = str(FirstArithmeticSequence)
			for Index in range(len(FirstArithmeticSequenceString)):
				PermutationDigitSet.add(FirstArithmeticSequenceString[Index])
			for Addition in range(2, (10 ** 4 - FirstArithmeticSequence) / 2):
				SecondArthmeticSequence = FirstArithmeticSequence + Addition
				SecondArthmeticSequenceString = str(SecondArthmeticSequence)
				BufferSet.clear()
				for Index in range(len(SecondArthmeticSequenceString)):
					BufferSet.add(SecondArthmeticSequenceString[Index])
				if PermutationDigitSet == BufferSet and IsPrime(SecondArthmeticSequence):
					ThirdArthmeticSequence = SecondArthmeticSequence + Addition
					ThirdArthmeticSequenceString = str(ThirdArthmeticSequence)
					BufferSet.clear()
					for Index in range(len(ThirdArthmeticSequenceString)):
						BufferSet.add(ThirdArthmeticSequenceString[Index])
					if PermutationDigitSet == BufferSet and IsPrime(ThirdArthmeticSequence):
						return FirstArithmeticSequenceString + SecondArthmeticSequenceString + ThirdArthmeticSequenceString

#	ID 	50
#	Consecutive prime sum
#	Which prime, below one-million, can be written as the sum of the most consecutive primes?
def ConsecutivePrimeSum(limit=10**6):
	PrimeList = GeneratePrimesRange(1, limit + 1)
	ConsecutivePrimeSum = [0 for x in range(len(PrimeList) + 1)]
	Sum = OverLimitIndex = 0
	Index = 1
	for Prime in PrimeList:
		Sum += Prime
		ConsecutivePrimeSum[Index] = Sum
		if Sum < limit:
			OverLimitIndex = Index
		Index += 1
	NumberOfPrimes = len(PrimeList)	
	for NumberOfConsecutivePrimes in reversed(range(1, OverLimitIndex + 1)):
		for Index in range(NumberOfPrimes - NumberOfConsecutivePrimes):
			ConsecutivePrime = ConsecutivePrimeSum[ NumberOfConsecutivePrimes + Index] - ConsecutivePrimeSum[Index]
			if ConsecutivePrime < limit and IsPrime(ConsecutivePrime):
				return ConsecutivePrime

print ConsecutivePrimeSum()
