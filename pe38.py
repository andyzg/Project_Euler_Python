list = []

def isPandigital(n):
	global list
	stuff = []
	for i in range(1,10):
		for j in str(n*i):
			if j in stuff:
				return
			stuff.append(j)
		if len(stuff) > 9:
			return
		elif len(stuff) == 9:
			print(stuff)
			list.append(''.join(stuff))
			return

for i in range(0,10000):
	isPandigital(i)
list.sort()
print(list)