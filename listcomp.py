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

