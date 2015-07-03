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
		if self.pinA == None:
			return int(input("Enter Pin A input for gate " + self.getLabel() + "-->"))
		else:
			return self.pinA.getFrom().getOutput()

	def getPinB(self):
		if self.pinB == None:
			return int(input("Enter Pin B input for gate " + self.getLabel() + "-->"))
		else:
			return self.pinB.getFrom().getOutput()

	def setNextPin(self, source):
		if self.pinA == None:
			self.pinA = source
		else:
			if self.pinB == None:
				self.pinB = source
			else:
				print("Cannot Connect: NO EMPTY PINS")


class UnaryGate(LogicGate):

	def __init__(self,n):
		# call the super class constructor first
		LogicGate.__init__(self,n)

		# then initialise the unique member variables
		self.Pin = None

	def getPin(self):
		if self.Pin == None:
			return int(input("Enter Pin input for gate "+ self.getLabel() + "-->"))
		else:
			return self.Pin.getFrom().getOutput()

	def setNextPin(self, source):
		if self.Pin  == None:
			self.Pin = source
		else:
			print("Cannot Connect: NO EMPTY PINS")


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


class Connector:

	def __init__(self, fgate, tgate):
		self.fromgate = fgate
		self.togate = tgate

		tgate.setNextPin(self)

	def getFrom(self):
		return self.fromgate

	def getTo(self):
		return self.togate

class NandGate(BinaryGate):

	def __init__(self, n):
		BinaryGate.__init__(self,n)

		self.gateAnd = AndGate(n)
		self.gateNot = NotGate(n)
		self.conn = Connector(self.gateAnd, self.gateNot)

	def performGateLogic(self):
		return self.gateNot.getOutput()

class NorGate(BinaryGate):

	def __init__(self, n):
		BinaryGate.__init__(self, n)

		self.gateOr = OrGate(n)
		self.gateNot = NotGate(n)
		self.conn = Connector(self.GateOr, self.gateNot)

	def performGateLogic(self):
		return self.gateNot.getOutput()

def main():
	# prove NOT ((A and B) or (C and D)) 
	#       == NOT (A and B) and NOT (C and D)

	g1 = AndGate("AB")
	g2 = AndGate("CD")
	g3 = OrGate("ABCD")
	g4 = NotGate("Output1")
	c1 = Connector(g1, g3)
	c2 = Connector(g2, g3)
	c3 = Connector(g3, g4)

	g5 = NandGate("AB")
	g6 = NandGate("CD")
	g7 = AndGate("ABCD")
	c4 = Connector(g5, g7)
	c5 = Connector(g6, g7)

	if g4.getOutput() == g7.getOutput():
		print("Success: Circuit outputs matched.")
	else:
		print("Fail: Circuit outputs did not match.")

main()