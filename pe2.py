a = 1
b = 2
c=0
count = 2
sum = 2
while b < 4000000:
	c = a + b
	a=b
	b=c
	
	if c%2==0:
		sum+=c
print(sum)