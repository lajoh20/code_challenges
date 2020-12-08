data_unformated = open("input.txt")
data = data_unformated.read()
input = data.split("\n\n")
count = 0
for i in range(0,len(input)):
	input[i] = input[i].split()
	size_of_group = len(input[i])
	index = {}
	for j in range(0,len(input[i][0])):
		index[input[i][0][j]]=1
	input[i] = "".join(input[i])	
	for l in index:
		if input[i].count(l) == size_of_group:
			count = count + 1
print(count)
