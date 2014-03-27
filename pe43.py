import itertools
num = [0,1,2,3,4,5,6,7,8,9]
prime = [2,3,5,7,11,13,17]
gen = itertools.permutations(num)

sum = 0
for i in gen:
	number = ''.join([str(a) for a in i])
	isGood = True
	for i in range(1, 8):
		if not int(number[i:i+3]) % prime[i-1] == 0:
			isGood = False
			break
	if isGood:
		print(number)
		sum += int(number)
print(sum)