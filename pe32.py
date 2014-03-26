import math
import itertools
list = [1,2,3,4,5,6,7,8,9]
a = itertools.permutations(list)

product = []

for i in a:
	for j in range(1, len(i)+1):
		for k in range(j+1, len(i)+1):
			if len(i[k:len(i)]) is 0:
				break
			else:
				x = int("".join(str(a) for a in i[k:len(i)]))
				y = int("".join(str(a) for a in i[0:j]))
				z = int("".join(str(a) for a in i[j:k]))
				if y*z > x:
					break
				if y*z == x:
					if not x in product:
						product.append(x)
print(sum(product))