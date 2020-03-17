"""
287. Find the Duplicate Number
Medium

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2

Example 2:

Input: [3,1,3,4,2]
Output: 3

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""

from typing import List

###############################################################################
"""
Solution: treat array values as node values in a linked list.  The duplicate 
integer is the first node value in the linked list cycle.

O(n) time
O(1) extra space

Runtime: 64 ms, faster than 84.06% of Python3 online submissions
Memory Usage: 15.5 MB, less than 7.14% of Python3 online submissions
"""
class Solution:
    def findDuplicate(self, arr: List[int]) -> int:
        #slow = fast = 0
        slow = fast = arr[0]

        while 1:
            slow = arr[slow]
            fast = arr[arr[fast]]

            if slow == fast:
                break

        #slow = 0
        slow = arr[0]

        while slow != fast:
            slow = arr[slow]
            fast = arr[fast]

        return slow

###############################################################################
"""
Solution 2: use binary search.

If len(arr) = n+1, then the array values are in the range 1, ..., n.
The array indices are 0, ..., n.
Do binary search on value space 1, ..., n.

If mid < dup, then count(x <= mid) <=  mid.
If mid >= dup, then count(x <= mid) > mid. 

O(n log n) time
O(1) extra space:
"""
class Solution2:
    def findDuplicate(self, arr: List[int]) -> int:
        lo = 1
        hi = len(arr) - 1 # n

        while lo < hi:
            mid = lo + (hi - lo) // 2

            count = 0
            for x in arr:
                if x <= mid:
                    count += 1

            if count <= mid: # then mid < dup
                lo = mid + 1
            else:
                hi = mid

        return lo

###############################################################################
"""
Solution 3: use sorting.

O(n log n) time
O(n) extra space: if don't sort in-place
"""
class Solution3:
    def findDuplicate(self, arr: List[int]) -> int:
        s = sorted(arr)

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                return s[i]

        # This point is never reached if the array has a duplicate.
        return None

###############################################################################
"""
Solution 4: use set to store seen elements.

O(n) time
O(n) extra space: for "seen" set.
"""
class Solution4:
    def findDuplicate(self, arr: List[int]) -> int:
        seen = set()

        for x in arr:
            if x in seen:
                return x
            
            seen.add(x)

        # This point is never reached if the array has a duplicate.
        return None

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)
        
        print()       
        print(arr)

        res = sol.findDuplicate(arr)

        print(f"\nres = {res}\n")


    sol = Solution() # use Floyd's cycle detection algo
    sol = Solution2() # use binary search
    #sol = Solution3() # use sorting
    #sol = Solution4() # use set()

    comment = "LC ex1; answer = 2"
    arr = [1,3,4,2,2]
    test(arr, comment)

    comment = "LC ex2; answer = 3"
    arr = [3,1,3,4,2]
    test(arr, comment)

    comment = "LC test case; answer = 2"
    arr = [2,2,2,2,2]
    test(arr, comment)
