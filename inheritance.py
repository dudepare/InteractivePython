class LogicGate:

	def __init__(self, n):
		self.label = n
		self.output = None

	def getLabel(self):
		return self.label

	def getOutput(self):
		self.output = self.performGateLogic()
		return self.output


class BinaryGate(LogicGate):

	def __init__(self,n):
		# call the constructor of the super class first
		LogicGate.__init__(self,n)

		# then initialise the members specific to this class
		self.pinA = None
		self.pinB = None

	def getPinA(self):
		return int(input("Enter Pin A input for gate " + self.getLabel() + "-->"))

	def getPinB(self):
		return int(input("Enter Pin B input for gate " + self.getLabel() + "-->"))

class UnaryGate(LogicGate):

	def __init__(self,n):
		# call the super class constructor first
		LogicGate.__init__(self,n)

		# then initialise the unique member variables
		self.Pin = None

	def getPin(self):
		return int(input("Enter Pin input for gate "+ self.getLabel() + "-->"))

class AndGate(BinaryGate):

	def __init__(self,n):
		BinaryGate.__init__(self, n)

	def performGateLogic(self):

		a = self.getPinA()
		b = self.getPinB()

		if a == 1 and b == 1:
			return 1
		else:
			return 0

class OrGate(BinaryGate):

	def __init__(self,n):
		BinaryGate.__init__(self,n)

	def performGateLogic(self):
		
		a = self.getPinA()
		b = self.getPinB()

		if a == 1 or b == 1:
			return 1
		else:
			return 0

class NotGate(UnaryGate):

	def __init__(self,n):
		UnaryGate.__init__(self, n)

	def performGateLogic(self):

		a = self.getPin()

		if a == 1:
			return 0
		else:
			return 1

g1 = AndGate("And Gate ")
print(g1.getLabel(), g1.getOutput())

g2 = OrGate("Or Gate ")
print(g2.getLabel(), g2.getOutput())

g3 = NotGate("Not Gate ")
print(g3.getLabel(), g3.getOutput())