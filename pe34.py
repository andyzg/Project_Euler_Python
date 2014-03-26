import math

list = []
for i in range(3, 1000000):
	if i == sum([math.factorial(int(b)) for b in str(i)]):
		print(i)
		list.append(i)

print(sum(list))