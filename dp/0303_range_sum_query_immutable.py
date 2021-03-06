"""
303. Range Sum Query - Immutable
Easy

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

Note:
You may assume that the array does not change.
There are many calls to sumRange function.
"""

from typing import List

###############################################################################
"""
Solution: precalculate and store prefix sums.

O(1) time per query
O(n) time to precalculate prefix sums
O(n) extra space
"""
class NumArray:
    # sums[i] = nums[0] + ... + nums[i-1]
    def __init__(self, nums: List[int]):
        self.sums = [0]
        s = 0
        
        for x in nums:
            s += x
            self.sums.append(s)

    # nums[i] + ... + nums[j]
    # = sums(j+1) - sums(i)
    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j+1] - self.sums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

###############################################################################
