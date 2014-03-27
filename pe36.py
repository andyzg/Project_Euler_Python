import math

# Lets just brute force it lol
def isDoublePal(n):
	stuff = str(n)
	for i in range(0, len(stuff)/2):
		if not stuff[i] == stuff[len(stuff)-1-i]:
			return 0
	binStuff = str(bin(n))[2:]
	for i in range(0, len(binStuff)/2):
		if not binStuff[i] == binStuff[len(binStuff)-1-i]:
			return 0
	print(n)
	return n

sum = 0
for i in range(0, 1000000):
	sum += isDoublePal(i)

print(sum)