"""
496. Next Greater Element I
Easy

You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.

Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.
"""

from typing import List
import collections

###############################################################################
"""
Solution: use mono decreasing stack, and dict that maps values in nums2
to their next greater values in nums2.

O(mn) time
O(m) extra space: for output

Runtime: 36 ms, faster than 99.32% of Python3 online submissions
Memory Usage: 14 MB, less than 7.41% of Python3 online submissions
"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        stack = []
        d = {}

        for i, y in enumerate(nums2):
            while stack and stack[-1][0] < y:
                z, _ = stack.pop()
                d[z] = y

            stack.append((y, i))

        for x in nums1:
            if x in d:
                res.append(d[x])
            else:
                res.append(-1)

        return res
        #return [d[x] if x in d else -1 for x in nums1]

"""
Solution 1b: same idea, but pop remaining elements in stack and set their values
in the dict to -1. Store only indices in stack.
"""
class Solution1b:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d = {}

        for i, y in enumerate(nums2):
            while stack and nums2[stack[-1]] < y:
                k = stack.pop()
                d[nums2[k]] = y

            stack.append(i)

        while stack:
            d[nums2[stack.pop()]] = -1

        return [d[x] for x in nums1]

"""
Solution 1c: same idea, but use defaultdict with default value -1, and store
only indices in stack.
"""
class Solution1c:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d = collections.defaultdict(lambda: -1)

        for i, y in enumerate(nums2):
            while stack and nums2[stack[-1]] < y:
                k = stack.pop()
                d[nums2[k]] = y

            stack.append(i)

        return [d[x] for x in nums1]

###############################################################################
"""
Solution: brute force

O(mn) time
O(m) extra space: for output

Runtime: 192 ms, faster than 7.89% of Python3 online submissions
Memory Usage: 14 MB, less than 7.41% of Python3 online submissions
"""
class Solution2:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        res = []
        
        for i, x in enumerate(nums1):
            # find x from nums1 in nums2 first
            for j, y in enumerate(nums2):
                if x == y:
                    break
                    
            # continue searching nums2 for next greater element
            for k in range(j+1, n):
                if nums2[k] > x:
                    res.append(nums2[k])
                    break
                    
            if len(res) == i: # x not found
                res.append(-1)
                    
        return res
                    
###############################################################################

if __name__ == "__main__":
    def test(nums1, nums2, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\nnums1 = {nums1}")
        print(f"nums2 = {nums2}")

        res = sol.nextGreaterElement(nums1, nums2)

        print(f"\nres = {res}\n")


    sol = Solution() # mono dec stack
    sol = Solution1b() #
    #sol = Solution1c() #

    #sol = Solution2() # brute force

    comment = "LC ex1; answer = [-1,3,-1]"
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    test(nums1, nums2, comment)

    comment = "LC ex2; answer = [3,-1]"
    nums1 = [2,4]
    nums2 = [1,2,3,4]
    test(nums1, nums2, comment)
