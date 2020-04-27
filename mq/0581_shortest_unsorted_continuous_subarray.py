"""
581. Shortest Unsorted Continuous Subarray
Easy

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5

Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""

from typing import List

###############################################################################
"""
BEST SOLUTION
Solution 1: find min/max values over all decreasing pairs of adjacent elements.
Then scan array again to find where they belong for the array to be sorted.

O(n) time - 3 unnested loops
O(1) extra space
"""
class Solution:
    def findUnsortedSubarray(self, arr: List[int]) -> int:
        if not arr: 
            return 0
        
        n = len(arr)

        # min/max values over all decreasing pairs
        min1 = float('inf')
        max1 = float('-inf')
        
        # bounds for the shortest continuous subarray to sort
        left = n - 1
        right = 0

        # find the min and max over all decreasing pairs
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                min1 = min(min1, arr[i])
                max1 = max(max1, arr[i-1])

        # find the first index where array value is > min1
        for i in range(n):
            if arr[i] > min1:
                left = i
                break

        # in reverse, find the first index where array value < max1
        for i in reversed(range(n)):
            if arr[i] < max1:
                right = i
                break

        return right - left + 1 if right > left else 0

###############################################################################
"""
Solution 2: use monotone stacks

O(n) time
O(n) extra space - stack can grow to n
"""
class Solution2:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        
        n = len(nums)

        # bounds for the shortest continuous subarray to sort
        left = n
        right = 0

        # Use increasing stack to find left bound.
        # Anytime we find a decrease to x, we have to go back and check which
        # values are greater than x.
        stack = []
        for i, v in enumerate(nums):
            while stack and v < nums[stack[-1]]:
                left = min(left, stack.pop())
            stack.append(i)

        # Use decreasing stack to find right bound.
        stack = []
        for i in reversed(range(n)):
            while stack and nums[i] > nums[stack[-1]]:
                right = max(right, stack.pop())
            stack.append(i)

        return right - left + 1 if right > left else 0

###############################################################################
"""
Solution 3: use sorting.

O(n log n) time
O(n) extra space

Runtime: 204 ms, faster than 94.77% of Python3 online submissions
Memory Usage: 13.9 MB, less than 95.00% of Python3 online submissions
"""
class Solution3:
    def findUnsortedSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        s = sorted(arr)

        for left in range(n):
            if arr[left] != s[left]:
                break
        
        for right in reversed(range(n)):
            if arr[right] != s[right]:
                break

        return right - left + 1 if right > left else 0

###############################################################################
"""
Solution 4: brute force. Find min/max indices over all decreasing pairs,
not necessarily adjacent.

O(n^2) time
O(1) extra space

LC TLE
"""
class Solution4:
    def findUnsortedSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        left = n - 1
        right = 0

        for i in range(n):
            x = arr[i]

            for j in range(i+1, n):
                if x > arr[j]:
                    left = min(left, i)
                    right = max(right, j)

        return right - left + 1 if right > left else 0

###############################################################################

if __name__ == "__main__":

    def test(arr, comment=None):
        res = s.findUnsortedSubarray(arr)
        
        print("="*80)
        if comment:
            print(comment)
            
        print(f"\n{arr}")
        print(f"\nresult = {res}\n")


    s = Solution() # use min/max values over all decreasing pairs of adjacent elts
    #s = Solution2() # use monotone stacks
    #s = Solution3() # use sorting
    #s = Solution4() # brute force; find min/max indices over all decreasing pairs
    
    comment = "LC example 1; answer = 5"
    arr = [2, 6, 4, 8, 10, 9, 15]
    test(arr, comment)

    comment = "LC test case; answer = 2"
    arr = [2,1]
    test(arr, comment)

    comment = "LC test case; answer = 4"
    arr = [1,3,2,2,2]
    test(arr, comment)

    comment = "LC TC; answer = 0"
    arr = [1,2,3,4]
    test(arr, comment)

    comment = "LC TC; answer = 2"
    arr = [1,3,2,3,3]
    test(arr, comment)
    
    comment = "LC TC; answer = 2"
    arr = [2,1]
    test(arr, comment)
    
    comment = "already sorted"
    arr = [1,2,3,4,5]
    test(arr, comment)

    comment = "already reverse sorted"
    arr = [5,4,3,2,1]
    test(arr, comment)

    comment = "constant values"
    arr = [1,1,1,1,1]
    test(arr, comment)
