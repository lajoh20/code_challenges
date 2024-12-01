import math
data =[]
left=[]
right=[]
result = 0
with open('your_input.txt', 'r') as file:
    for line in file.readlines():
        line = line.rstrip('\n')
        line = line.split('   ')
        data.append(line[0])
        data.append(line[1])     
for i in range(0,len(data)):
    if i == 0 or i % 2 ==0:
        left.append(int(data[i]))
    else:
        right.append(int(data[i]))
for i in range(0, len(left)):
    count = 0
    for j in range(0,len(right)):
        if left[i]==right[j]:
            count = count +1
    result = result +(left[i]*count)
print(result)
