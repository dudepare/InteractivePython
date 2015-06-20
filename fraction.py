
# Helper function
def gcd(m,n):
	while m%n != 0:
		oldm = m
		oldn = n

		m = oldn
		n = oldm%oldn
	
	return n

class Fraction:

	#the methods go here
	def __init__(self, top, bottom):
		self.num = top
		self.den = bottom

	def show(self):
		print(self.num, "/", self.den)

	def __str__(self):
		return str(self.num) + "/" + str(self.den)

	def __add__(self, otherfraction):
		newnum = self.num*otherfraction.den + self.den*otherfraction.num
		newden = self.den * otherfraction.den
		common = gcd(newnum, newden)

		return Fraction(newnum//common, newden//common)

	def __sub__(self, otherfraction):
		newnum = self.num*otherfraction.den - self.den*otherfraction.num
		newden = self.den * otherfraction.den
		common = gcd(newnum, newden)

		return Fraction(newnum//common, newden//common)

	def __mul__(self, other):
		newnum = self.num * other.den
		newden = self.den * other.num
		common = gcd(newnum, newden)

		return Fraction(newden, )

	def __eq__(self, other):
		firstnum = self.num * other.den
		secondnum = other.num * self.den

		return firstnum == secondnum

# This is where the magic happens
def main():
	x = Fraction(1,4)
	y = Fraction(4,16)

	print(x+y)
	print(x == y)


main()

