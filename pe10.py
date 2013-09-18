def prime(x):
	for i in range(2,int(x**0.5)+1):
		if x%i==0:
			return False
	return True
	
sum=0	
for i in range(2,2000000):
	if prime(i):
		print(i)
		sum+=i
print(sum)