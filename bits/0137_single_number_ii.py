"""
137. Single Number II
Medium

Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3

Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
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
    def singleNumber(self, nums: List[int]) -> int:
        d = collections.Counter(nums)
        
        for k in d:
            if d[k] == 1:
                return k

###############################################################################
"""
Solution: use set to find unique numbers, and use math.

O(n) time
O(n) space
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (3 * sum(set(nums)) - sum(nums) ) // 2

###############################################################################
"""
Solutions: bits

https://medium.com/@lenchen/leetcode-137-single-number-ii-31af98b0f462

There are 4 states: appeared 0, 1, 2, or 3 times. 
We can combine the states for 0 and 3. So there are 3 states.

We need 2 bits to store the state for each bit of input. 
(Why can we use the same bits across all inputs?)

00: appeared 0 times
01: appeared 1 time
10: appeared 2 times
11: appeared 3 times

We want to design a logic operation that cycles from 
00 -> 01 -> 10 -> 11 and back to 00.

Let i = input bit, h = high bit of state, l = low bit of state.

     hl  i   h'l'
1    00  0   00  # no input, no change
2    01  0   01  # no input, no change
3    10  0   10  # no input, no change

4    00  1   01  # 00 -> 01
5    01  1   10  # 01 -> 10
6    10  1   00  # 10 -> 00

Note h' = 1 for rows 3 and 5.
h' = (h & ~l & ~i) | (~h & l & i)

Note l' = 1 for rows 2 and 4.
l' = (~h & l & ~i) | (~h & ~l & i)

This can be reduced to:
l' = ~h & ((l & ~i) | (~l & i))
l' = ~h & (l ^ i)

If we let l' be assigned first, then h' can be computed using l' using
rows 3 and 5:
h' = (h & ~i & ~l') | (~h & i & ~l')
h' = ~l' & ((h & ~i) | (i & ~h))
h' = ~l' & (h ^ i)

In summary:
l' = ~h & (l ^ i)
h' = ~l' & (h ^ i)

###

operations:
- seen ^ x flips the presence of x in seen
- ~seen

1st appearance of number:
- add number to seen_once
- don't add to seen_twice because of presence in seen_once

2nd appearance of number:
- remove number from seen_once
- add number to seen_twice

3rd appearance of number:
- don't add to seen_once because of presence in seen_twice
- remove nunmber from seen_twice


O(n) time
O(1) space
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = 0
        seen_twice = 0

        for x in nums:
            
            seen_once = ~seen_twice & (seen_once ^ x)

            seen_twice = ~seen_once & (seen_twice ^ x)

        return seen_once
