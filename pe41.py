import itertools

def checkPrime(num):
	for i in range(2, int(num**0.5)):
		if num%i == 0:
			print(i)
			return False
	return True

#because stupid 45 and 36 are multiples of 3...
number = [1,2,3,4,5,6,7]
perm = itertools.permutations(number)
num = sorted(perm, reverse=True)
for i in num:
	temp = int(''.join([str(a) for a in i]))
	if checkPrime(temp):
		print(temp)
		break