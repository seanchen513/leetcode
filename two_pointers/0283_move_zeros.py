"""
283. Move Zeroes
Easy

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

from typing import List

###############################################################################
"""
Solution 1:

O(n) time
O(1) extra space

Runtime: 44 ms, faster than 90.86% of Python3 online submissions
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        p = 0 # position to move the next non-zero to

        for i in range(n):
            if arr[i] != 0:
                arr[p] = arr[i]
                p += 1

        # while p < n):
        #     arr[p] = 0
        #     p += 1

        arr[p:] = [0] * (n - p)

###############################################################################
"""
Solution 2:

Better than solution 1 if most of the array is 0's.

Invariants:
1. All elements before slow pointer "p" are non-zeros.
2. All elements between "p" and current pointer "i" are zeros.

O(n) time
O(1) extra space
"""
class Solution2:
    def moveZeroes(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """                
        n = len(arr)
        p = 0 # 1 + index of last non-zero 

        for i in range(n):
            if arr[i] != 0:
                arr[p], arr[i] = arr[i], arr[p]
                p += 1

###############################################################################
"""
Solution 3:

O(n) time

Seems to use O(n) extra space for intermediary list.

See comment here:
https://leetcode.com/problems/move-zeroes/discuss/72012/Python-short-in-place-solution-with-comments.

https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/262/discuss/395021/Pythonic-one-liner/tinvaan
"""
class Solution3:
    def moveZeroes(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """                
        count = arr.count(0)

        arr[:] = [x for x in arr if x != 0]
        
        arr += [0] * count

        #arr[:] = [x for x in arr if x != 0] + [0] * arr.count(0)

###############################################################################

if __name__ == "__main__":
    def test(s, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"arr = {arr}")
        
        sol.moveZeroes(arr)

        print(f"arr = {arr}")
        

    sol = Solution()
    sol = Solution2()
    sol = Solution3()

    comment = "LC ex1; answer = [1,3,12,0,0]"
    arr = [0,1,0,3,12]
    test(arr, comment)
