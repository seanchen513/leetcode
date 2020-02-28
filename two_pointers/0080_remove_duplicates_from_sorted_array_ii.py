"""
26. Remove Duplicates from Sorted Array
Easy

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.

Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""

from typing import List

###############################################################################
"""
Solution: use pointer/index for position to put next value that is different.
Use counter for how many times last value has been seen.

O(n) time
O(1) extra space
"""
class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        n = len(arr)
        p = 0
        last_val = None
        counter = 0 # how many times has last_val been seen; capped at 2 here

        for i in range(n):
            if arr[i] != last_val:
                arr[p] = last_val = arr[i]
                p += 1
                counter = 1
            elif counter < 2:
                arr[p] = last_val = arr[i]
                p += 1
                counter += 1

        return p

###############################################################################

if __name__ == "__main__":
    def test(s, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\narr = {arr}")
        
        res = sol.removeDuplicates(arr)

        print(f"\narr = {arr}")
        print(f"res = {res}\n")
        

    sol = Solution()

    comment = "LC ex1; answer = 5"
    arr = [1,1,1,2,2,3]
    test(arr, comment)

    comment = "LC ex2; answer = 7"
    arr = [0,0,1,1,1,1,2,3,3]
    test(arr, comment)

    comment = "trivial LC case; answer = 0"
    arr = []
    test(arr, comment)
