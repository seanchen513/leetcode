"""
260. Single Number III
Medium

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]

Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""

from typing import List
import collections

###############################################################################
"""
Solution: use dict to count numbers.

O(n) time
O(n) space
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d = collections.Counter(nums)
        res = []

        for x in d:
            if d[x] == 1:
                res.append(x)

        return res

###############################################################################
"""
Solution: use set.

O(n) time
O(n) space
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        s = set()

        for x in nums:
            if x in s:
                s.remove(x)
            else:
                s.add(x)

        return list(s)

###############################################################################
"""
Solution: use bits.

O(n) time
O(1) space
"""
import functools
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Find XOR of the two unique numbers. If we can find one of the two
        # unique numbers (say "a"), then the other one will be "a ^ mask". 
        mask = 0
        for x in nums:
            mask ^= x
        # mask = functools.reduce(operator.xor, nums)

        # Find rightmost 1-bit of xor.
        # ie, the rightmost bit where the two unique numbers differ
        diff = mask & -mask

        # Use "diff" to filter for the unique number that has a 1-bit in 
        # the position of the 1-bit of diff.
        # This unique number will be "a".
        # The other unique number will be "a ^ xor".
        # All the other numbers either (1) have x & diff == 0, or
        # (2) have x & diff == 1, but get XOR'd into "a" twice, thus
        # cancelling itself out.
        a = 0
        for x in nums:
            if x & diff:
                a ^= x

        return [a, a ^ mask]
