"""
724. Find Pivot Index
Easy

Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

Example 1:

Input: 
nums = [1, 7, 3, 6, 5, 6]
Output: 3

Explanation: 
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.

Example 2:

Input: 
nums = [1, 2, 3]
Output: -1
Explanation: 
There is no index that satisfies the conditions in the problem statement.
 
Note:

The length of nums will be in the range [0, 10000].
Each element nums[i] will be an integer in the range [-1000, 1000].
"""

from typing import List

###############################################################################
"""
Solution: track left sum, and use total sum, left sum, and current value
to calculate right sum.

O(n) time
O(1) extra space
"""
class Solution:
    def pivotIndex(self, arr: List[int]) -> int:
        n = len(arr)
        left_sum = 0
        s = sum(arr)
        
        for i, x in enumerate(arr):
            if left_sum == s - left_sum - x:
                return i

            left_sum += x
            
        return -1
        
###############################################################################
"""
Solution 2: track sums from left and right

O(n) time
O(1) extra space
"""
class Solution2:
    def pivotIndex(self, arr: List[int]) -> int:
        n = len(arr)
        l_sum = 0
        r_sum = sum(arr)
        
        for i in range(n):
            if i >= 1:
                l_sum += arr[i-1]
                
            r_sum -= arr[i]
            
            if l_sum == r_sum:
                return i
            
        return -1
        