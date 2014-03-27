import fileinput
buffer = 64
words = open("words.txt", "r")
text = words.read().split(',')

triangle = []
for i in range(1, 20):
	triangle.append(i*(i+1)/2)

count = 0
for i in text:
	lol = sum([(ord(a)-buffer) for a in i[1:len(i)-1]])
	if lol in triangle:
		count += 1
print(count)