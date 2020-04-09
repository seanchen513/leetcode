"""
594. Longest Harmonious Subsequence
Easy

We define a harmounious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:

Input: [1,3,2,2,5,2,3,7]
Output: 5

Explanation: The longest harmonious subsequence is [3,2,2,2,3].

Note: The length of the input array will not exceed 20,000.
"""

from typing import List
import collections

###############################################################################
"""
Solution: use dict to count digits in nums.

One pass through nums for building dict, and one pass through dict.

Note: careful about case [1,1,1,1]. Answer is 0, not 4.

O(n) time
O(n) extra space: for dict.
"""
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = collections.Counter(nums)
        mx = 0
        
        for k in d:
            if k + 1 in d:
                mx = max(mx, d[k] + d[k+1])
                
        return mx

        # return max([d[k] + d[k+1] for k in d if k+1 in d] or [0])

###############################################################################
"""
Solution: same idea, but just one pass through nums.

Update dict and max length within same loop.
Need to check for x-1 as well as x+1.

O(n) time
O(n) extra space: for dict.
"""
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = collections.defaultdict(int)
        mx = 0
        
        for x in nums:
            d[x] += 1

            if x + 1 in d:
                mx = max(mx, d[x] + d[x + 1])
            if x - 1 in d:
                mx = max(mx, d[x] + d[x - 1])

            ### Just doing this with no "if" statements doesn't work.
            ### Example: [1,1,1,1]. Answer is 0, not 4.
            #mx = max(mx, d[x] + d[x+1], d[x] + d[x-1])

        return mx
                