"""
1389. Create Target Array in the Given Order
Easy

Given two arrays of integers nums and index. Your task is to create target array under the following rules:

Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.

It is guaranteed that the insertion operations will be valid.

Example 1:

Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]

Example 2:

Input: nums = [1,2,3,4,0], index = [0,1,2,3,0]
Output: [0,1,2,3,4]
Explanation:
nums       index     target
1            0        [1]
2            1        [1,2]
3            2        [1,2,3]
4            3        [1,2,3,4]
0            0        [0,1,2,3,4]

Example 3:

Input: nums = [1], index = [0]
Output: [1]

Constraints:

1 <= nums.length, index.length <= 100
nums.length == index.length
0 <= nums[i] <= 100
0 <= index[i] <= i
"""

from typing import List
import collections

###############################################################################
"""
Solution: use list.insert().

O(n^2) time
O(n) extra space for output
"""
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        t = []
        #t = collections.deque([])

        for i, idx in enumerate(index):
            t.insert(idx, nums[i])

        return t

###############################################################################
"""
Solution 2: update "index" array first. Simulates moving subarrays up if a
lower index is found later.

O(n^2) time
O(n) extra space for output
"""
class Solution2:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        n = len(index)

        for i in range(n):
            for j in range(i):
                if index[j] >= index[i]:
                    index[j] += 1

        t = [0] * n

        for i, idx in enumerate(index):
            t[idx] = nums[i]

        return t

###############################################################################

if __name__ == "__main__":
    #def test(arr, comment=None):
    def test(arr, k, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\nnums = {nums}")
        print(f"index = {index}")

        res = sol.createTargetArray(nums, index)

        print(f"\nres = {res}\n")


    sol = Solution() # use list.insert()
    sol = Solution2() # update "index" array first

    comment = "LC ex1; answer = [0,4,1,3,2]"
    nums = [0,1,2,3,4]
    index = [0,1,2,2,1]
    test(nums, index, comment)

    comment = "LC ex2; answer = [0,1,2,3,4]"
    nums = [1,2,3,4,0]
    index = [0,1,2,3,0]
    test(nums, index, comment)

    comment = "LC ex3; answer = [1]"
    nums = [1]
    index = [0]
    test(nums, index, comment)
