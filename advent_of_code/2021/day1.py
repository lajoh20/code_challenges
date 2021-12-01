#part1
f = open("input.txt", "r")
inputtxt = f.readlines()
cleaninput=[]
for item in inputtxt:
    newitem = item.replace("\n","")
    cleaninput.append(int(newitem))
count = 0
for i in range(2,len(cleaninput)-1):
    if cleaninput[i]>cleaninput[i-1]:
        count = count+1
    else:
        pass
print(count)
print(len(cleaninput))

#part2
f = open("input.txt", "r")
inputtxt = f.readlines()
cleaninput=[]
for item in inputtxt:
    newitem = item.replace("\n","")
    cleaninput.append(int(newitem))
count = 0
for i in range(2,len(cleaninput)-1):
    if cleaninput[i]+cleaninput[i-1]+cleaninput[i+1]>cleaninput[i-1]+cleaninput[i-2]+cleaninput[i]:
        count = count+1
    else:
        pass
print(count)
print(len(cleaninput))
