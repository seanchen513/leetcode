"""
34. Find First and Last Position of Element in Sorted Array
Medium

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

from typing import List

###############################################################################
"""
Solution: do 2 binary searches of form "lo < hi".
"""
class Solution:
    def searchRange(self, arr: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(arr)
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            if arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid
                
        if lo == len(arr) or arr[lo] != target:
            return [-1, -1]
        
        first = lo
        lo = 0
        hi = len(arr)
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            if arr[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
                
        return [first, lo - 1]
        