"""
1437. Check If All 1's Are at Least Length K Places Away
Medium

Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away from each other, otherwise return False.

Example 1:

Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.

Example 2:

Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other.

Example 3:

Input: nums = [1,1,1,1,1], k = 0
Output: true

Example 4:

Input: nums = [0,1,0,1], k = 1
Output: true

Constraints:

1 <= nums.length <= 10^5
0 <= k <= nums.length
nums[i] is 0 or 1
"""

from typing import List

###############################################################################
"""
Solution: 

O(n) time
O(1) extra space
"""
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return True

        n = len(nums)

        # If nums[0] is 1, then i - last = 0 - last = k if k = -last.
        # So we can initialize last to any number < -last.
        #last = float('-inf')
        last = -k - 1

        for i in range(n):
            if nums[i] == 1:
                if i - last <= k:
                    return False
                
                last = i

        return True
