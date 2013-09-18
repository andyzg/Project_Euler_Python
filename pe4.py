max = 0

for i in range(100,1000):
	for j in range(100,1000):
		a = str(i*j)
		if a[::-1]==a:
			if i*j>max:
				max=i*j
print(max)