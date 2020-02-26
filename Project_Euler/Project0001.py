"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
mult_3 = 0
mult_5 = 0
mult_15 = 0
for i in range(0,1000,3):
	mult_3 = mult_3 + i
for i in range(0,1000,5):
		mult_5 = mult_5 + i
for i in range(0,1000,15):
		mult_15 = mult_15 + i
mult_3and5 = mult_3 + mult_5 - mult_15
print(mult_3and5)
