
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
		
		if not isinstance(top, int):
			raise RuntimeError("Error: Numerator not an integer.")

		if not isinstance(bottom, int):
			raise RuntimeError("Error: Denominator not an integer.")

		self.num = top
		self.den = bottom
		self.gcd = gcd(self.num, self.den)
		self.num = self.num//self.gcd
		self.den = self.den//self.gcd

	def show(self):
		print(self.num, "/", self.den)

	def getNum(self):
		return self.num

	def getDen(self):
		return self.den

	def __repr__(self):
		return "Fraction(" + str(self.num) +  ", " + str(self.den)+ ")" 

	def __str__(self):
		return str(self.num) + "/" + str(self.den)

	def __add__(self, otherfraction):
		newnum = self.num*otherfraction.den + self.den*otherfraction.num
		newden = self.den * otherfraction.den

		return Fraction(newnum, newden)

	def __radd__(self, other):
		newfraction = Fraction(other, 1)
		return newfraction + self

	def __iadd__(self, other):
		self = self + other
		return self

	def __sub__(self, otherfraction):
		newnum = self.num*otherfraction.den - self.den*otherfraction.num
		newden = self.den*otherfraction.den
		
		return Fraction(newnum, newden)

	def __mul__(self, other):
		newnum = self.num * other.num
		newden = self.den * other.den
		common = gcd(newnum, newden)

		return Fraction(newnum//common, newden//common)

	def __div__(self, other):
		return self.__truediv__(other)

	def __truediv__(self, other):
		newnum = self.num * other.den
		newden = self.den * other.num
		common = gcd(newnum, newden)

		return Fraction(newnum//common, newden//common)

	def __lt__(self, other):
		selfratio = self.num / self.den
		otherratio = other.num / other.den

		return selfratio < otherratio

	def __gt__(self, other):
		selfratio = self.num / self.den
		otherratio = other.num / other.den

		return selfratio > otherratio

	def __eq__(self, other):
		firstnum = self.num * other.den
		secondnum = other.num * self.den

		return firstnum == secondnum

	def __ge__(self, other):
		selfratio = self.num / self.den
		otherratio = other.num / other.den

		return selfratio >= otherratio

	def __le__(self, other):
		selfratio = self.num / self.den
		otherratio = other.num / other.den

		return selfratio <= otherratio

	def __ne__(self, other):
		selfratio = self.num / self.den
		otherratio = other.num / other.den

		return selfratio != otherratio


# This is where the magic happens
def main():

	x = Fraction(1,2)
	y = Fraction(1,3)

	#print (x < y)
	#print (x > y)
	x += y
	print (repr(x))


main()

