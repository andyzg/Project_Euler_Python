import math

count = 0
number=2
check = True

while count !=10001:
	check = True
	for i in range(2,int(number**0.5)+1):
		if number%i==0:
			check = False
			break
	if check:
		count+=1
		print(str(number) + " " + str(count))
	number+=1
print(number)