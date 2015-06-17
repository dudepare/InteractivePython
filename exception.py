import math

anumber = int(input("Please enter an integer"))
if anumber < 0:
	raise RuntimeError("You can't use a negative number")
else:
	print(math.sqrt(anumber))
