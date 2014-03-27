import collections

def isCircularPrime(n, isPrime):
	number = [a for a in str(n)]
	list = collections.deque(number)
	for i in range(0, len(number)):
		list.rotate(1)
		if not isPrime[int(''.join(list))]:
			return 0
	return 1

limit = 1000000
isPrime = [True]*limit

for i in range(5,limit):
	isPrime[i] = False

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
count = 0
for i in range(0, limit):
	if isPrime[i]:
		count += isCircularPrime(i, isPrime)

print(count)