def isReallyPrime(n, isPrime):
	for i in range(1, len(str(n))):
		if not isPrime[int(str(n)[i:])] or not isPrime[int(str(n)[:i])]:
			return 0
	print(n)
	return n


limit = 1000000
isPrime = [True]*limit

for i in range(5,limit):
	isPrime[i] = False

# sieves of atkin
for x in range(1, int(limit**0.5)):
	for y in range(1, int(limit**0.5)):
		n = 4*x**2 + y**2
		if n <= limit and (n%12 == 1 or n%12 == 5):
			isPrime[n] = not isPrime[n]
		n = 3*x**2 + y**2
		if n <= limit and n%12 == 7:
			isPrime[n] = not isPrime[n]
		n = 3*x**2 - y**2
		if x > y and n <= limit and n%12 == 11:
			isPrime[n] = not isPrime[n]

for n in range(5, int(limit**0.5)):
	if isPrime[n]:
		for k in range(n**2, limit, n**2):
			isPrime[k] = False

isPrime[0] = False
isPrime[1] = False
isPrime[4] = False

sum = 0

for i in range(8, limit):
	if isPrime[i]:
		sum += isReallyPrime(i, isPrime)

print(sum)