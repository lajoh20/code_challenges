"""
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10,
since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

nums = [1,2,3,4,6,5,5,5,5,5,7,7,7]

def top_2_sum(nums):
	x = max(nums)
	nums.remove(x)
	y = max(nums)
	return(x+y)

def top_2_sum_no(nums):
	x = max(nums)
	index_x = nums.index(x)
	nums.pop(index_x-1)
	try:
		nums.pop(index_x-1)
	except:
		nums.pop()
	try:	
		nums.pop(index_x-1)
	except:
		nums.pop()
	y = max(nums)
	return(x+y)

nums_even = []
nums_odd = []

for i in range(0,len(nums)):
	if i%2==0:
		nums_even.append(nums[i])
	else:
		nums_odd.append(nums[i])
	
odd = top_2_sum(nums_odd)
even = top_2_sum(nums_even)
no = top_2_sum_no(nums)




print(max(odd,even,no))

