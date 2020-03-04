"""

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers
 from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 
is 17.

"""

k = 17
list_of_nums = [10,15,3,7]
x = False
for i in range (0,len(list_of_nums)):
	if (k-list_of_nums[i]) in list_of_nums:
		x = True
	if (list_of_nums[i]*2 == k) and list_of_nums.count(list_of_nums[i]) == 1:
			x = False


print("True"*x)
