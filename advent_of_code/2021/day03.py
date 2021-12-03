part #1 25min
f = open("input.txt", "r")
inputtxt = f.readlines()
cleaninput=[]
for item in inputtxt:
    item = item.replace("\n","")
   # item = item.split(" ")
    cleaninput.append((item))
countlen=0
result=[0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(0,len(cleaninput)):
    for j in range(-1,11):
        if(cleaninput[i][j])=='1':
            result[j]=result[j]+1
print(result)            
print(len(cleaninput))    


010100010100
101011101011

part#2
