"""
75. Sort Colors
Medium

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""

from typing import List

###############################################################################
"""
Solution 1: two passes, using dict to count colors.

Easy to generalize this two-pass 3-way partitioning to n-way partitioning.

O(n) time: two passes
O(1) extra space
"""
class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = {0:0, 1:0, 2:0}
        for x in arr:
            d[x] += 1

        arr[:d[0]] = [0] * d[0]
        arr[ d[0] : d[0]+d[1]] = [1] * d[1]
        arr[ d[0]+d[1] :] = [2] * d[2]

###############################################################################
"""
Solution 2: use 3 pointers and do 2 types of swaps:

i = current pointer
p0 = rightmost boundary of 0s
p2 = leftmost boundary of 2s

O(n) time: single pass
O(1) extra space
"""
class Solution2:
    def sortColors(self, arr: List[int]) -> None:
        n = len(arr)
        p0 = 0 # rightmost boundary of 0s
        p2 = n - 1 # leftmost boundary of 2s
        
        i = 0
        while i <= p2:
            if arr[i] == 0:
                arr[i], arr[p0] = arr[p0], arr[i]
                p0 += 1
                i += 1

            elif arr[i] == 1:
                i += 1                

            else: # arr[i] == 2:
                arr[i], arr[p2] = arr[p2], arr[i]
                p2 -= 1
                # Don't increment "i" since need to check new arr[i].


        
###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\narr = {arr}")

        sol.sortColors(arr)

        print(f"\narr = {arr}\n")


    sol = Solution()
    sol = Solution2()

    comment = "LC example; answer = [0,0,1,1,2,2]"
    arr = [2,0,2,1,1,0]
    test(arr, comment)

    comment = "LC test case; answer = [0,0]"
    arr = [0,0]
    test(arr, comment)

    comment = "LC test case; answer = [0,2]"
    arr = [2,0]
    test(arr, comment)
    
    comment = "LC test case; answer = [0,0,1]"
    arr = [0,1,0]
    test(arr, comment)
    
    comment = "LC test case; answer = [0,1,1]"
    arr = [1,0,1]
    test(arr, comment)
    
    comment = "LC test case; answer = [0,1,2]"
    arr = [2,0,1]
    test(arr, comment)

    comment = "LC test case; answer = [0,1,2]"
    arr = [1,2,0]
    test(arr, comment)

    comment = "LC test case; answer = [0,0,1,1,2,2]"
    arr = [2,0,2,1,1,0]
    test(arr, comment)

    comment = "answer = [2,2,2,2,2]"
    arr = [2,2,2,2,2]
    test(arr, comment)
