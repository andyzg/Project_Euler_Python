for i in range(0,1000):
	for j in range(0,1000):
		k = (i**2+j**2)**0.5
		if i+j+k == 1000:
			print i*j*k