import random
referencestr = "methinks it is like a weasel"

def generateBitmap(expectedstr, inputstr):
	bitmap = [ 1 if expectedstr[x] == inputstr[x] else 0 for x in range(len(expectedstr))  ]
	return bitmap

def typeMonkeyType(strlen, beststring):
	alphabet = "abcdefghijklmnopqrstuvwxyz "
	output = ""

	if beststring == "":
		for i in range(strlen):
			output += alphabet[random.randint(0, len(alphabet)-1)]
		return output
	else:
		output = beststring
		bitmap = generateBitmap(referencestr, beststring)
		for i in range(strlen):
			if bitmap[i] == 0:
				output = output[:i] + alphabet[random.randint(0, len(alphabet) -1)] + output[i+1:]
				break
		return output	

def scoreMonkey(reference, inputstr):
	score = 0
	if len(reference) != len(inputstr):
		return 0

	for i in range(len(reference)):
		if inputstr[i] == reference[i]:
			score += 1

	return int(score/len(reference) * 100)

def run():
	tries = 0
	score = 0
	bestscore = 0
	bestguess = ""
	lenstring = len(referencestr)
	while (score != 100):
		tries += 1
		monkeyoutput = typeMonkeyType(lenstring, bestguess)
		score = scoreMonkey(referencestr, monkeyoutput)
		if score > bestscore:
			bestscore = score
			bestguess = monkeyoutput
	print("Got it after ", tries, " trys. Good on you monkeys!")

run()


		

