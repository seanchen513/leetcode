"""
35. Search Insert Position
Easy

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2

Example 2:

Input: [1,3,5,6], 2
Output: 1

Example 3:

Input: [1,3,5,6], 7
Output: 4

Example 4:

Input: [1,3,5,6], 0
Output: 0
"""

from typing import List
import bisect

###############################################################################
"""
Solution: use binary search (left version) with "lo < hi".

Similar to bisect.bisect(), aka, bisect.bisect_left().
"""
class Solution:
    def searchInsert(self, arr: List[int], target: int) -> int:
        lo = 0
        hi = len(arr)
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            if arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid
                
        return lo

###############################################################################
"""
Solution: use binary search (right version) with "lo < hi".
Check "lo" (or "hi") after loop.

Similar to bisect.bisect_right().
"""
class Solution:
    def searchInsert(self, arr: List[int], target: int) -> int:
        lo = 0
        hi = len(arr)
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            if arr[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
                
        if lo > 0 and arr[lo-1] == target:
            return lo - 1

        return lo

###############################################################################
"""
Solution: use binary search with "lo <= hi". Return "lo" after loop.
"""
class Solution:
    def searchInsert(self, arr: List[int], target: int) -> int:
        lo = 0
        hi = len(arr) - 1
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            
            if arr[mid] < target:
                lo = mid + 1
            elif arr[mid] > target:
                hi = mid - 1
            else:
                return mid
                
        return lo

###############################################################################
"""
Solution: use bisect_left().
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)
            
"""
Solution: use bisect(), aka, bisect_right().
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = bisect.bisect(nums, target)
        
        if i > 0 and nums[i-1] == target:
            return i-1
        
        return i
            
                