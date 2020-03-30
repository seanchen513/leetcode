"""
153. Find Minimum in Rotated Sorted Array
Medium

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1

Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""

from typing import List

###############################################################################
"""
Solution: 

Loop invariants:
1. lo < hi
2. mid < hi; in particular, arr[mid] != arr[hi] since no duplicates exist.
3. Keep min in range [lo, hi].

lo < hi, and since we calc mid by rounding down, we always have mid < hi.
Proof: lo < hi, so lo + hi < 2*hi, so mid < hi.

Since mid never equals hi, we can compare arr[mid] and arr[hi].

If arr[mid] < arr[hi], then the min is on the left side. Since arr[mid]
still might be the min, we make hi = mid. The new interval [lo, hi] is smaller
since originally mid != hi.

If arr[mid] > arr[hi], then the min is on the right side and the min cannot
be arr[mid] since arr[hi] is smaller. So we can make lo = mid + 1.

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/48484/A-concise-solution-with-proof-in-the-comment

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/158940/Beat-100%3A-Very-Simple-(Python)-Very-Detailed-Explanation

"""
class Solution:
    def findMin(self, arr: List[int]) -> int:
        lo = 0
        hi = len(arr) - 1 # minus 1 required here

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if arr[mid] < arr[hi]: # then min on left side, inclusive
                hi = mid
            else: # then min on right side, exclusive
                lo = mid + 1

        return arr[lo]

###############################################################################
"""
Solution: 

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/48493/Compact-and-clean-C%2B%2B-solution

"""
class Solution:
    def findMin(self, arr: List[int]) -> int:
        lo = 0
        hi = len(arr) - 1

        while lo < hi:
            if arr[lo] < arr[hi]:
                return arr[lo]

            mid = lo + (hi - lo) // 2

            if arr[mid] >= arr[lo]: # then min is on right side
                lo = mid + 1
            else: # then min is on left side; arr[mid] might be min
                hi = mid

        return arr[lo]

###############################################################################
"""
Solution: 
"""
class Solution:
    def findMin(self, arr: List[int]) -> int:
        # sorted array case
        if arr[0] <= arr[-1]: # required: = sign takes care of case len(arr) == 1
            return arr[0]

        lo = 0
        hi = len(arr) - 1 # doesn't work if we don't subtract 1 here
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            if arr[mid] > arr[mid+1]:
                return arr[mid+1]
            elif arr[mid] > arr[lo]: # then min on right side
                lo = mid + 1
            else: # min on left side
                hi = mid

###############################################################################
"""
Solution:  

"""
class Solution:
    def findMin(self, arr: List[int]) -> int:
        # sorted array case
        if arr[0] <= arr[-1]: # required: = sign takes care of case len(arr) == 1
            return arr[0]

        lo = 0
        hi = len(arr) - 1 # don't need -1 here

        while lo < hi:
            mid = lo + (hi - lo + 1) // 2

            if arr[mid] < arr[lo]: # then min on left side, inclusive
                hi = mid - 1 
            else: # then min on right side
                lo = mid

        return arr[lo+1]

###############################################################################
"""
Solution:  

"""
class Solution:
    def findMin(self, arr: List[int]) -> int:
        # sorted array case
        if arr[0] <= arr[-1]: # required: = sign takes care of case len(arr) == 1
            return arr[0]

        lo = 0
        hi = len(arr) - 1 # minus 1 required here

        while lo < hi:
            mid = lo + (hi - lo + 1) // 2

            if arr[mid] < arr[lo]: # then min on left side, inclusive
                hi = mid - 1 
            else: # then min on right side
                lo = mid

        return arr[lo+1]

###############################################################################
"""
Solution: 
"""
class Solution:
    def findMin(self, arr: List[int]) -> int:
        # sorted array case
        if arr[0] < arr[-1]: # optional: = sign takes care of case len(arr) == 1
            return arr[0]

        lo = 0
        hi = len(arr) - 1 # doesn't work if we don't subtract 1 here
        
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            
            if arr[mid] > arr[lo]: # then min on right side
                lo = mid
            else: # min on left side
                hi = mid

        return arr[hi]

"""

arr[lo] < arr[mid] > arr[hi]
0 1 2 3 4 5 6
4 5 6 7 0 1 2 

0 1 2 3 4 5 6
1 2 4 5 6 7 0

0 1 2 3 4 5 6
2 4 5 6 7 0 1


arr[lo] > arr[mid] < arr[hi]
0 1 2 3 4 5 6
7 0 1 2 4 5 6

"""
