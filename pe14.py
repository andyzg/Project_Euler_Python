def even(n):
	return n/2

def odd(n):
	return (3*n+1)

def check(n):
	if n%2==1:
		return odd(n)
	elif n%2==0:
		return even(n)
	
count = 0
max = 0
number = 0
hash = {"1":0,"2":1}

a = 0
for i in range(3,1000000):
	count=0
	a = i
	while check(i)!=1:

		#print(str(i)[0:len(str(i))-2])
		if i<100:
			if str(i)[0:len(str(i))-2] in hash:
				count+=hash.get(str(i)[0:len(str(i))-2])
				#print("Magic")
				break
		elif i>=100:
			if str(i)[0:len(str(i))] in hash:
				count+=hash.get(str(i)[0:len(str(i))])
				#print("Magic")
				break
		count+=1
		i = check(i)
		if i == 2:
			count+=1
	if count>max:
		max=count
		number = a
		print(number)
	hash[str(a)] = count
	
#print(hash)
print(number)