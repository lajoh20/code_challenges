"""basic implmentation of the count of deisers of 3 and 5"""

long = 0
count = input("how high should i go? ")
countint = int(count)
result = countint + 1
for i in range(1,result):
	print(long)
	if i%3 == 0 and i%5 == 0:
		print("FizzBuzz")
		long = long + i
	elif i%3 == 0 and i%5 !=0:
		print("Fizz")
		long = long + i
	elif i%5 == 0 and i%3 !=0:
		print("Buzz")
		long = long + i
	else:
		print(i)
print(long)
