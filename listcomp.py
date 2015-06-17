sqlist = []
for x in range(1,11):
	sqlist.append(x*x)

print(sqlist)

wordlist = ['cat', 'dog', 'rabbit']
letterlist = []
for aword in wordlist:
	for aletter in aword:
		if aletter not in letterlist:
			letterlist.append(aletter)
print(letterlist)

newletterlist = []
[ newletterlist.append(letter) for word in wordlist for letter in word if letter not in newletterlist]

print(newletterlist)