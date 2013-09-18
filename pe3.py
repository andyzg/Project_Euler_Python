number = 600851475143
check = True


while check:
	for i in range(2,int(number**0.5)+1):
		if number%i==0:
			number=number/i
			print(number)
			break
		if i==int(number**0.5):
			check=False
print(number)