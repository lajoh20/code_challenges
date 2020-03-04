"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""
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

print(new_list_of_nums)

