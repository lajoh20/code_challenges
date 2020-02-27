"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""
missing_int_found = False
input_arr = [3, 4, -1,1]
if 1  not in input_arr:
	print(1)
else:
	input_arr.sort()
	index_point = input_arr.index(1)
	while missing_int_found == False:
		if (input_arr[index_point-1]) > input_arr[index_point]:
			index_point = index_point + 1
		else:
			print((input_arr[index_point])+1)
			missing_int_found = True
