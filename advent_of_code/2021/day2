part #1

f = open("input.txt", "r")
inputtxt = f.readlines()
cleaninput=[]
for item in inputtxt:
    item = item.replace("\n","")
    item = item.split(" ")
    cleaninput.append((item))
depth = 0
horizontal = 0
for item in cleaninput:
    if item[0] == 'forward':
       horizontal = horizontal+int(item[1])
    elif item[0] == 'down':
       depth = depth+int(item[1])
    elif item[0] == 'up':
       depth = depth-int(item[1])
print(horizontal*depth)

part #2

f = open("input.txt", "r")
inputtxt = f.readlines()
cleaninput=[]
for item in inputtxt:
    item = item.replace("\n","")
    item = item.split(" ")
    cleaninput.append((item))
depth = 0
horizontal = 0
aim = 0 
for item in cleaninput:
    if item[0] == 'forward':
       horizontal = horizontal+int(item[1])
       depth = depth + ((aim) * int(item[1]))
    elif item[0] == 'down':
       aim = aim+int(item[1])
    elif item[0] == 'up':
       aim = aim-int(item[1])
print(horizontal*depth)
