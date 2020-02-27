"""
852. Peak Index in a Mountain Array
Easy

Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1
Note:

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.
"""

from typing import List

"""
Linear scan for the index with max value, or a local max, works but is
O(n) time.

return arr.index(max(arr))
"""

###############################################################################
"""
Solution: modified binary search for peak pattern.  
Returns early if peak found.

3 possible patterns formed by arr[mid-1], arr[mid], arr[mid+1]:
/\ : peak found
increasing: peak is to right
decreasing: peak is to left
\/ : impossible

O(log n) time
O(1) extra space
"""
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lo = 0
        hi = len(arr) - 1

        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)
            #mid = lo + (hi - lo) // 2

            #print(f"lo,mid,hi = {lo},{mid},{hi}")
            
            if arr[mid-1] < arr[mid]:
                if arr[mid] > arr[mid+1]:
                    return mid
                else:
                    lo = mid + 1
            else:
                hi = mid - 1

###############################################################################
"""
Solution 2: modified binary search for largest index i such that
arr[i-1] < arr[i].  Biased towards lo.
Doesn't return until lo == hi.
"""
class Solution2:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lo = 0
        hi = len(arr) - 1

        while lo < hi: # Note strict < here
            mid = lo + (hi - lo) // 2 # biased towards lo
            
            #print(f"lo,mid,hi = {lo},{mid},{hi}")

            if arr[mid] < arr[mid + 1]:
                lo = mid + 1
            else:
                hi = mid

        return lo

"""
Solution 2b: modified binary search for largest index i such that
arr[i - 1] < arr[i].  Biased towards hi.
Doesn't return until lo == hi.
"""
class Solution2b:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lo = 0
        hi = len(arr) - 1

        while lo < hi: # Note strict < here
            mid = lo + (hi - lo + 1) // 2 # biased towards hi
            
            #print(f"lo,mid,hi = {lo},{mid},{hi}")

            if arr[mid-1] < arr[mid]:
                lo = mid
            else:
                hi = mid - 1

            #print(f"lo,mid,hi = {lo},{mid},{hi}")

        return lo

"""
Solution 2c: modified binary search for smallest index i such that
arr[i] > arr[i+1].  Biased towards lo.
Doesn't return until lo == hi.
"""
class Solution2c:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lo = 0
        hi = len(arr) - 1

        while lo < hi: # Note strict < here
            mid = lo + (hi - lo) // 2 # biased towards lo
            
            #print(f"lo,mid,hi = {lo},{mid},{hi}")

            if arr[mid] > arr[mid + 1]:
                hi = mid
            else:
                lo = mid + 1

            #print(f"lo,mid,hi = {lo},{mid},{hi}")

        return lo

"""
Solution 2d: modified binary search for smallest index i such that
arr[i] > arr[i+1].  Biased towards hi.
Doesn't return until lo == hi.
"""
class Solution2d:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lo = 0
        hi = len(arr) - 1

        while lo < hi: # Note strict < here
            mid = lo + (hi - lo + 1) // 2 # biased towards hi
            
            #print(f"lo,mid,hi = {lo},{mid},{hi}")

            if arr[mid-1] > arr[mid]:
                hi = mid - 1
            else:
                lo = mid

            #print(f"lo,mid,hi = {lo},{mid},{hi}")

        return lo

###############################################################################
"""
Solution 3: golden section search.

https://leetcode.com/problems/peak-index-in-a-mountain-array/discuss/139848/C%2B%2BJavaPython-Better-than-Binary-Search

https://stackoverflow.com/questions/4247111/is-golden-section-search-better-than-binary-search

https://en.wikipedia.org/wiki/Fibonacci_search_technique

O(log n) time
O(1) extra space
"""
class Solution3:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        def gold1(l, r):
            return l + int(round((r-l) * 0.382))

        def gold2(l, r):
            return l + int(round((r-l) * 0.618))

        l = 0
        r = len(arr) - 1

        x1 = gold1(l, r)
        x2 = gold2(l, r)

        while x1 < x2:
            if arr[x1] < arr[x2]:
                l = x1
                x1 = x2
                x2 = gold1(x1, r)
            else:
                r = x2
                x2 = x1
                x1 = gold2(l, x2)

        return arr.index(max(arr[l:r+1]), l)

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(arr)

        res = sol.peakIndexInMountainArray(arr)

        print(f"\nres = {res}")


    sol = Solution() # bsearch for peak pattern

    #sol = Solution2() # bsearch for largest i such that arr[i-1] < arr[i]
    sol = Solution2b() # same but hi biased

    sol = Solution2c() # bsearch for smallest i such that arr[i] > arr[i+1]
    sol = Solution2d() # same but hi biased
    
    sol = Solution3() # golden section search

    comment = "LC ex1; answer = 1"
    arr = [0,1,0]
    test(arr, comment)

    comment = "LC ex1; answer = 1"
    arr = [0,2,1,0]
    test(arr, comment)

    comment = "good test case for golden-section search; answer = 3"
    arr = [0,5,10,15,3,2,1]
    test(arr, comment)
