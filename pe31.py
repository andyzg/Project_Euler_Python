#Solutions structure copied off http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/

# List: array of different existing coins
# m: Index of element
# n: Number to sum up to
def getCount(list, m, n):
	table = []
	table.append([])

	for i in range(0, m):
		table[0].append(1)

	for i in range(1, n+1):
		table.append([])
		for j in range(0, m):
			#Count solutions with list[j]
			x = table[i-list[j]][j] if i - list[j] >= 0 else 0
			#Count solutions without list[j]
			y = table[i][j-1] if j >= 1 else 0

			table[i].append(x+y)
	return table[n][m-1]
def main():
	list = [1,2,5,10,20,50,100,200]
	m = len(list)
	print(getCount(list, m, 200))

main()