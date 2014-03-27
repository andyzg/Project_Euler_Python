string = ""
limit = 500000
for i in range(1, limit):
	string = string + str(i)

prod = 1
for i in ([0,9,99,999,9999,99999,999999]):
	prod *= int(string[i])
print(prod)