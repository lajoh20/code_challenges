"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
Example 2:

Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
 

Constraints:

1 <= n <= 10^5
"""
import math,numpy
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        int_n =[]
        str_n = str(n)
        for i in range(0,len(str_n)):
            int_n.append(int(str_n[i]))
        sum_i = sum(int_n)
        prod = numpy.prod(int_n)
        return(prod-sum_i)      
        
"""
Runtime: 96 ms, faster than 6.01% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
Memory Usage: 27.9 MB, less than 100.00% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
"""
