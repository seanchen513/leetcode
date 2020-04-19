"""
33. Search in Rotated Sorted Array
Medium

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

from typing import List

###############################################################################
"""
Examples of rotated sorted arrays.
n = 8, lo = 0, hi = 7
mid = lo + (hi - lo) // 2 = 0 + (7 - 0) // 2 = 3

0 1 2 3 4 5 6 7: mid = 3 >= start = 0

1 2 3 4 5 6 7 0: mid = 4 >= start = 1

2 3 4 5 6 7 0 1: mid = 5 >= start = 2

3 4 5 6 7 0 1 2: mid = 6 >= start = 3

4 5 6 7 0 1 2 3: mid = 7 >= start = 4

//

5 6 7 0 1 2 3 4: mid = 0 < start = 5

6 7 0 1 2 3 4 5: mid = 1 < start = 6

7 0 1 2 3 4 5 6: mid = 2 < start = 7
"""

"""
If array is not already sorted, then arr[left] >= arr[right], and start and 
ending values are "adjacent" (in sorted array).  So value at mid must be bigger
than both or smaller than both (or equal to one), ie,

arr[mid] <= arr[left] and arr[mid] <= arr[right]
or
arr[mid] >= arr[right] and arr[mid] >= arr[left]

In the first case, the subarray from mid to right is sorted.
In the second case, the subarray from left to mid is sorted.
"""

###############################################################################
"""
Solution 1: iterative bsearch with lo <= hi. First branch on subinterval
that is sorted, then check if target is in that subinterval.

O(log n) time
O(1) extra space
"""
class Solution:
    def search(self, arr: List[int], target: int) -> int:
        lo = 0
        hi = len(arr) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if arr[mid] == target:
                return mid
            
            if arr[lo] <= arr[mid]: # subarray from lo to mid is sorted
                if arr[lo] <= target < arr[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            
            else: # arr[mid] <= arr[hi], subarray from mid to hi is sorted
                #if arr[mid + 1] <= target <= arr[hi]:
                if arr[mid] < target <= arr[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        
        # target not found
        return -1

"""
Solution 1b: recursive version of sol 1. 
"""
class Solution1b:
    def search(self, arr: List[int], target: int) -> int:
        def bsearch(lo, hi):
            if lo > hi:
                return -1
            
            mid = lo + (hi - lo) // 2

            if arr[mid] == target:
                return mid
            
            if arr[lo] <= arr[mid]: # subarray from lo to mid is sorted
                if arr[lo] <= target < arr[mid]:
                    return bsearch(lo, mid - 1)
                else:
                    return bsearch(mid + 1, hi)
            
            else: # arr[mid] <= arr[hi], subarray from mid to hi is sorted
                #if arr[mid + 1] <= target <= arr[hi]:
                if arr[mid] < target <= arr[hi]:
                    return bsearch(mid + 1, hi)
                else:
                    return bsearch(lo, mid - 1)
                
            return -1

        return bsearch(0, len(arr)-1)

###############################################################################
"""
Solution 2: iterative bsearch with lo < hi. First branch on subinterval
that is sorted, then check if target is in that subinterval.
"""
class Solution2:
    def search(self, arr: List[int], target: int) -> int:
        if not arr:
            return -1

        lo = 0
        hi = len(arr) - 1 # have to subtract 1 here
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            if arr[lo] <= arr[mid]: # subarray from lo to mid is sorted
                if arr[lo] <= target <= arr[mid]:
                    hi = mid
                else:
                    lo = mid + 1
            else: # arr[mid] <= arr[hi], subarray from mid to hi is sorted
                if arr[mid] < target <= arr[hi]:
                    lo = mid + 1
                else:
                    hi = mid
            
        if arr[lo] == target:
            return lo
        
        return -1
        
###############################################################################
"""
Solution 3: first find rotation index (index of smallest value), then do 
binary search accounting for rotation.

There are two approaches to this.  We do approach 1 here.

(1) Determine range to search target, and do bsearch on that range.

Based on approach 1 here:
https://leetcode.com/problems/search-in-rotated-sorted-array/solution/

or

(2) Do single loop with mid adjusted by rotation index:
real_mid = (mid + rot) % n
"""
class Solution3:
    def search(self, arr: List[int], target: int) -> int:
        if not arr:
            return - 1

        n = len(arr)
        lo = 0
        hi = n - 1

        # First, if array rotated, find the sorted subarray that the
        # target is in.

        if arr[lo] > arr[hi]: # if array actually rotated
            # Modified binary search to find rotation index.
            while lo <= hi: # ok to use <= since both lo and hi are adjusted
                mid = lo + (hi - lo) // 2

                # "IndexError: index out of range" if try on sorted array
                if arr[mid] > arr[mid + 1]:
                    rot = mid + 1
                    break
                else:
                    if arr[mid] < arr[lo]:
                        hi = mid - 1
                    else:
                        lo = mid + 1

            # Use rotation index to adjust indices for sorted subarray.
            if target < arr[0]: # search in second part
                lo = rot
                hi = n - 1
            else: # search in first part
                lo = 0
                hi = rot - 1

        # Usual binary search on sorted array.
        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                lo = mid + 1
            else: # arr[mid] > target
                hi = mid - 1

        # target not found
        return -1

###############################################################################
"""
Solution 4: first find rotation index (index of smallest value), then do 
binary search accounting for rotation.

There are two approaches to this.  We do approach 2 here, and also use a 
different way to find rotation index.

(1) Determine range to search target, and do bsearch on that range.

or

(2) Do single loop with mid adjusted by rotation index:
real_mid = (mid + rot) % n
https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14425/Concise-O(log-N)-Binary-search-solution
"""
class Solution4:
    def search(self, arr: List[int], target: int) -> int:
        n = len(arr)

        # First, use modified binary search to look for rotatation index, 
        # ie, index of smallest value.
        lo = 0
        hi = n - 1

        while lo < hi: # Note: use < not <=, since only lo is adjusted
            mid = lo + (hi - lo) // 2
            if arr[mid] > arr[hi]:
                lo = mid + 1
            else:
                hi = mid

        rot = lo # lo == hi is the rotation index after the loop
        lo = 0
        hi = n - 1

        # Do usual binary search on sorted array.
        while lo <= hi:
            mid = lo + (hi - lo) // 2

            # index of where actual middle value is
            real_mid = (mid + rot) % n

            if arr[real_mid] == target:
                return real_mid
            elif arr[real_mid] < target:
                lo = mid + 1
            else: # arr[real_mid] > target
                hi = mid - 1

        # target not found
        return -1

"""
Example: n = 8
0 1 2 3 4 5 6 7
2 3 4 5 6 7 0 1: mid = 5 >= start = 2

rot = 6
lo = 0, hi = 7, mid = 3, real_mid = (3 + 6) % 8 = 1, value is 3
"""

###############################################################################

if __name__ == "__main__":
    def test(arr, target, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\narr = {arr}")
        print(f"\ntarget = {target}")

        res = sol.search(arr, target)

        print(f"\nres = {res}")


    sol = Solution() # iterative bsearch with lo <= hi; branch on sorted subarray
    sol = Solution1b() # recursive ...

    sol = Solution2() # iterative bsearch with lo < hi

    sol = Solution3() # use rotation to find sorted subarray to do bsearch on
    #sol = Solution4() # use rotation index to do bsearch using (mid + rot) % n

    comment = "LC ex1; answer = 4"
    arr = [4,5,6,7,0,1,2]
    target = 0
    test(arr, target, comment)

    comment = "LC ex2; answer = -1"
    arr = [4,5,6,7,0,1,2]
    target = 3
    test(arr, target, comment)

    comment = "sorted array not rotated; answer = 4"
    arr = [2,3,5,8,13,21]
    target = 13
    test(arr, target, comment)

    comment = "trivial test case; answer = 0"
    arr = [5]
    target = 5
    test(arr, target, comment)

    comment = "LC test case; answer = -1"
    arr = []
    target = 5
    test(arr, target, comment)

    comment = "LC test case; answer = 1"
    arr = [5,1,3]
    target = 1
    test(arr, target, comment)
