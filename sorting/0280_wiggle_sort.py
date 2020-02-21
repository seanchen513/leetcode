"""
280. Wiggle Sort
Medium

Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

Example:

Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]
"""

from typing import List

###############################################################################
"""
Solution 1: one-pass, swapping adjacent elements as needed

O(n) time
O(1) extra space

Runtime: 84 ms, faster than 99.55% of Python3 online submissions
Memory Usage: 13.4 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
    def wiggleSort(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        if n <= 1:
            return

        #up = False # start with False so that first pair will be non-dec

        for i in range(1, n):
            #if up == (arr[i] >= arr[i-1]):
            if (i & 1 == 0) == (arr[i] >= arr[i-1]):
                arr[i], arr[i-1] = arr[i-1], arr[i]
            
            #up = not up

###############################################################################
"""
Solution 2: sort and swap disjoint pairs of elements starting with 2nd elt.

O(n log n) time: for sorting
O(1) extra space: if using in-place sort like heapsort
"""
class Solution2:
    def wiggleSort(self, arr: List[int]) -> None:
        arr.sort()
        n = len(arr)

        for i in range(2, n, 2):
            arr[i], arr[i-1] = arr[i-1], arr[i]

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\narr = {arr}")
        
        sol.wiggleSort(arr)

        print(f"\narr = {arr}")


    sol = Solution() # one pass, swapping adjacent pairs as needed
    sol = Solution2() # sort and swap disjoint pairs starting with 2nd elt

    comment = "LC example"
    arr = [3,5,2,1,6,4]
    test(arr, comment)
   
    comment = "LC test case; empty list"
    arr = []
    test(arr, comment)
    
    comment = "LC test case"
    arr = [2,1]
    test(arr, comment)
    
    comment = "LC test case"
    arr = [1,3,2,4]
    test(arr, comment)
    