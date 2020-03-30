"""
162. Find Peak Element
Medium

A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.

Note:
Your solution should be in logarithmic complexity.
"""

from typing import List

###############################################################################
"""
Solution: binary search using "while lo < hi".
Iterates until lo = hi.
Compares arr[mid-1], arr[mid], and arr[mid+1], and returns early.

Note: solution works without early return by by simply letting hi = mid
(not hi = mid-1) when arr[mid] > arr[mid+1].
"""
class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        lo = 0
        hi = len(arr) - 1

        # At anytime, peak index can be anywhere from lo to hi.

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if arr[mid] > arr[mid + 1]: # decreasing
                if arr[mid] > arr[mid - 1]:
                    return mid
                else: # decreasing from mid-1 to mid+1
                    # Check left side since it's increasing then decreasing
                    hi = mid - 1 # might be peak index
            
            else: # increasing from mid to mid+1
                # Check right side since it's increasing then decreasing
                lo = mid + 1 # might be peak index

        """
        On last iteration, there are 3 cases: (inc/dec refers to mid to mid+1)
        1. lo = hi-1 = mid, decreasing: hi' = mid-1 (lo is peak index)
        2. lo = hi-1 = mid, increasing: lo' = mid+1 = hi (peak index)

        3. lo = hi-2 = mid-1, decreasing: hi' = mid-1 = lo (peak index)
        4. lo = hi-2 = mid-1, increasing: lo' = mid+1 = hi (peak index)

        In the 3 relevant cases, lo is the peak index after the loop ends.
        """

        return lo

"""
Solution 1b: same as sol 1, but no early return, so use "hi = mid".
"""
class Solution1b:
    def findPeakElement(self, arr: List[int]) -> int:
        lo = 0
        hi = len(arr) - 1

        # At anytime, peak index can be anywhere from lo to hi.

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if arr[mid] > arr[mid + 1]: # decreasing
                # Check left side since it's increasing then decreasing
                hi = mid # hi - 1 might be peak index
            
            else: # increasing from mid to mid+1
                # Check right side since it's increasing then decreasing
                lo = mid + 1 # might be peak index

        """
        On last iteration, there are 3 cases: (inc/dec refers to mid to mid+1)
        1. lo = hi-1 = mid, decreasing: hi' = mid = lo (peak index)
        2. lo = hi-1 = mid, increasing: lo' = mid+1 = hi (peak index)

        3. lo = hi-2 = mid-1, decreasing: hi' = mid > lo, so this case
        actually involves another iteration.
        4. lo = hi-2 = mid-1, increasing: lo' = mid+1 = hi (peak index)

        In the 3 relevant cases, lo == hi is the peak index after the loop ends.
        """

        return lo # or hi

"""
Other variations involving comparing arr[mid] to arr[mid-1].
"""

###############################################################################
"""
Solution 2: binary search using "while lo <= hi" and comparing arr[mid-1], 
arr[mid], and arr[mid+1].  Because of this, we need to check cases at the
start for when n <= 2.

Early return if peak index found.

O(log n) time
O(1) extra space

"""
class Solution2:
    def findPeakElement(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0

        if arr[0] > arr[1]:
            return 0

        if arr[n-1] > arr[n-2]:
            return n-1

        # Now, 0 and n-1 cannot be peak indices.
        # Increasing at start (0 to 1), and decreasing at end (n-2 to n-1)
        lo = 0 # 0 or 1 works
        hi = n-1 # n-1 or n-2 works; n-3 works if we include "return lo" at end

        # At anytime, peak index can be anywhere from lo to hi.
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if arr[mid] > arr[mid+1]: # decreasing
                if arr[mid] > arr[mid-1]:
                    return mid
                else: # decreasing from mid-1 to mid+1
                    # Check left side since it's increasing then decreasing
                    hi = mid - 1 # might be peak index
            
            else: # increasing from mid to mid+1
                # Check right side since it's increasing then decreasing
                lo = mid + 1 # might be peak index

        # This point should not be reached if a peak element exists.

###############################################################################
"""
Solution 3: binary search using "while lo <= hi"
This variation compares arr[mid] and arr[mid+1].
Doesn't return until lo <= hi isn't True.

O(log n) time
O(1) extra space
"""
class Solution3:
    def findPeakElement(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0

        if arr[0] > arr[1]:
            return 0

        if arr[n-1] > arr[n-2]:
            return n-1

        # Now, 0 and n-1 cannot be peak indices.
        # Increasing at start (0 to 1), and decreasing at end (n-2 to n-1)
        lo = 1 # 0 or 1 works
        hi = n-3 # n-1, n-2, or n-3 works

        # At anytime, peak index can be anywhere from lo to hi+1.
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            #print(f"lo,mid,hi = {lo},{mid},{hi}")

            if arr[mid] > arr[mid+1]: # decreasing
                # Check left side since its increasing, then decreasing
                hi = mid - 1 # hi + 1 = mid might be peak index

            else: # increasing; lo assigned index of higher element
                # Check right side since its increasing then decreasing
                lo = mid + 1 # might be peak index
            
        """
        On last iteration, there are 3 cases:
        1. lo = hi = mid, decreasing: hi' = mid-1 = lo-1 (lo is peak index)
        2. lo = hi = mid, increasing: lo' = mid+1 = hi+1 (peak index)
        
        3. lo = hi - 1 = mid, decreasing: hi' = mid-1 = lo-1 (lo is peak index)
        4. lo = hi - 1 = mid, increasing: lo' = mid+1 = hi, so this case
        actually involves another iteration.
        """

        return lo

"""
Solution 3b: like sol 3, binary search using "while lo <= hi",
but compare arr[mid] and arr[mid-1].
Doesn't return until lo <= hi isn't True.
"""
class Solution3b:
    def findPeakElement(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0

        if arr[0] > arr[1]:
            return 0

        if arr[n-1] > arr[n-2]:
            return n-1

        # Now, 0 and n-1 cannot be peak indices.
        # Increasing at start (0 to 1), and decreasing at end (n-2 to n-1)
        lo = 2 # 0, 1, or 2 works
        hi = n-2 # n-1 or n-2 works

        # At anytime, peak index can be anywhere from lo-1 to hi.
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            #print(f"lo,mid,hi = {lo},{mid},{hi}")

            if arr[mid] < arr[mid-1]: # decreasing
                # Check left side since its increasing, then decreasing
                hi = mid - 1 # might be peak index

            else: # increasing; lo assigned index of higher element
                # Check right side since its increasing then decreasing
                lo = mid + 1 # lo-1 might be peak index

        """
        On last iteration, there are 3 cases:
        1. lo = hi = mid, decreasing: hi' = mid-1 = lo-1 (hi' is peak index)
        2. lo = hi = mid, increasing: lo' = mid+1 = hi+1 (hi is peak index)
        3. lo = hi - 1 = mid, decreasing: hi' = mid-1 = lo-1 (hi' is peak index)
        4. lo = hi - 1 = mid, increasing: lo' = mid+1 = hi, so this case
        actually involves another iteration.
        """

        return hi

###############################################################################
"""
Solution 4: linear scan.

O(n) time
O(1) extra space
"""
class Solution4:
    def findPeakElement(self, arr: List[int]) -> int:
        n = len(arr)

        for i in range(n-1):
            if arr[i] > arr[i+1]:
                return i

        return n-1

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(arr)

        res = sol.findPeakElement(arr)

        print(f"\nres = {res}")


    sol = Solution() # bsearch for peak (early return); "while lo < hi"
    sol = Solution1b() # same, but no early return

    #sol = Solution2() # bsearch for peak (early return); "while lo <= hi"
    #sol = Solution3() # bsearch "while lo <= hi"; check arr[mid] vs arr[mid+1]
    #sol = Solution3b() # bsearch "while lo <= hi"; check arr[mid] vs arr[mid-1]
    
    #sol = Solution4() # linear scan

    comment = "LC ex1; answer = 2"
    arr = [1,2,3,1]
    test(arr, comment)

    comment = "LC ex1; answer = 1 or 5"
    arr = [1,2,1,3,5,6,4]
    test(arr, comment)

    comment = "LC test case; answer = 0"
    arr = [1]
    test(arr, comment)
    
    comment = "inc seq; answer = 7"
    arr = [1,2,3,4,5,6,7,8]
    test(arr, comment)

    comment = "dec seq; answer = 0"
    arr = [8,7,6,5,4,3,2,1]
    test(arr, comment)

    comment = "LC test case; answer = 2"
    arr = [2,3,4,3,2,1]
    test(arr, comment)

    comment = "LC test case; answer = 1"
    arr = [3,4,3,2,1]
    test(arr, comment)
