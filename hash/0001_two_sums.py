"""
1. Two Sum
Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

from typing import List
import string
import collections

"""
This problem is a slightly harder variation since it asks to return the indices.

Easier versions: (1) return whether any two integers sum to the given target;
(2) give the values that sum to the given target.
"""

###############################################################################
"""
Solution 1: brute force

O(n^2) time, where n = len(nums)
O(1) extra space
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        # return statement not required here since (unique) answer is guaranteed

"""
Solution 1b: same, but slightly optimized
"""
class Solution1b:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        for i in range(n):
            target2 = target - nums[i]
            
            for j in range(i+1, n):
                if nums[j] == target2:
                    return [i, j]

###############################################################################
"""
Solution 2: sort input array, and then use two pointers

O(n log n) time: for sorting
O(n) extra space: to build sorted array
"""
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # build sorted array of tuples (value, index in nums)
        a = []
        for i, x in enumerate(nums):
            a.append((x, i))

        a = sorted(a)

        # two pointers method
        i = 0
        j = len(nums) - 1

        while i < j:
            curr = a[i][0] + a[j][0] # current sum

            if curr < target:
                i += 1
            elif curr > target:
                j -= 1
            else:
                return [a[i][1], a[j][1]]

###############################################################################
"""
Solution 3: use dictionary to store number needed to hit target, and map this 
to index of original number.

O(n) time, where n = len(nums)
O(n) extra space: for dict
"""
class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need = dict() # needed number to hit target -> index of original number
        
        for i in range(len(nums)):
            if nums[i] in need:
                return [i, need[nums[i]]]
            
            need[target - nums[i]] = i

"""
Solution 3b: same, but use enumerate()
"""
class Solution3b:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need = dict() # needed number to hit target -> index of original number
        
        for i, v in enumerate(nums):
            if v in need:
                return [i, need[v]]
            
            need[target - v] = i

###############################################################################

if __name__ == "__main__":
    def test(nums, target, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(f"nums = {nums}")
        print(f"target = {target}")

        res = sol.twoSum(nums, target)

        print(f"\nres = {res}\n")


    sol = Solution() # brute force
    #sol = Solution1b() # brute force, slightly optimized
    
    #sol = Solution2() # sorting, 2 pointers

    #sol = Solution3() # dict
    #sol = Solution3b() # dict, enumerate()

    comment = "LC example 1; answer = [0,1]"
    nums = [2,7,11,15]
    target = 9
    test(nums, target, comment)

    comment = "LC example 2; answer = [1,2]"
    nums = [3,2,4]
    target = 6
    test(nums, target, comment)

    comment = "LC example 3; answer = [0,1]"
    nums = [3,3]
    target = 6
    test(nums, target, comment)
