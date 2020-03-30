"""
154. Find Minimum in Rotated Sorted Array II
Hard

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1

Example 2:

Input: [2,2,2,0,1]
Output: 0

Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?
"""

from typing import List

###############################################################################
"""
Solution: 

O(n) time worst case, eg, when all elements are equal.
O(1) extra space
"""
class Solution:
    def findMin(self, arr: List[int]) -> int:
        lo = 0
        hi = len(arr) - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if arr[mid] > arr[hi]: # then min is on right side, exclusive
                lo = mid + 1
            elif arr[mid] < arr[hi]: # then min is on left side, inclusive
                hi = mid
            else: # arr[mid] == arr[hi], so it's safe to exclude hi
                hi -= 1

        return arr[lo]
