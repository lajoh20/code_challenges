""" a triditional print vertion useing trutheness and a fuction"""

def fizz_buzz(x):
	return(("Fizz"*(0==x%3))+("Buzz"*(0==x%5)) or (x))

for i in range(1,101):
	print(fizz_buzz(i))
