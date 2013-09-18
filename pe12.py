def triang(number):
	sum=0
	for i in range(0,number+1):
		sum+=i
	return sum
	
def divisor(number):
	count=2
	for i in range(2,int(number**0.5)):
		if number%i==0:
			count+=2
	return count

x = 1

while divisor(triang(x))<500:
	x+=1
	print(divisor(triang(x)))
print(triang(x))