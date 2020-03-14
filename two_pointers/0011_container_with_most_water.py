"""
11. Container With Most Water
Medium

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""

from typing import List

###############################################################################
"""
Solution: use 2 pointers for left and right side of containers.

Start with max width container.  For side with smaller height, move side
inwards until a higher height is found, and check volume of new container.

Note: if both sides are the same height, it doesn't matter which side is
moved first.  The only way to get a container of greater volume is for
both sides to be moved eventually.  Can modify code to take this case
into consideration.

O(n) time
O(1) extra space

Runtime: 112 ms, faster than 99.68% of Python3 online submissions
Memory Usage: 14.5 MB, less than 44.21% of Python3 online submissions
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        left = 0
        right = n - 1

        ht = min(height[0], height[n-1])
        mx = (n-1) * ht

        while left < right:
            if height[left] < height[right]:
                while left < right and height[left] <= ht:
                    left += 1

                if left < right:
                    ht = min(height[left], height[right])
                    mx = max(mx, (right - left) * ht)

            else:
                while left < right and height[right] <= ht:
                    right -= 1

                if left < right:
                    ht = min(height[left], height[right])
                    mx = max(mx, (right - left) * ht)

        return mx

"""
Solution 1b: more concise, but slower.  Increments left or right one step
at a time, and recalculates and checks volume at each step.

O(n) time
O(1) extra space

Runtime: 132 ms, faster than 63.52% of Python3 online submissions
Memory Usage: 14.5 MB, less than 41.05% of Python3 online submissions
"""
class Solution1b:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        mx = 0
        left = 0
        right = n - 1

        while left < right:
            mx = max(mx, (right - left) * min(height[left], height[right]) )

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return mx

###############################################################################
"""
Solution 2: brute force

O(n^2) time
O(1) extra space

TLE
"""
class Solution2:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        mx = 0
        
        for i in range(n):
            ht_i = height[i]

            for j in range(i+1, n):
                mx = max(mx, (j-i)*min(ht_i, height[j]) )
                
        return mx

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(arr)

        res = sol.maxArea(arr)

        print(f"\nres = {res}\n")


    sol = Solution() # use 2 pointers
    #sol = Solution1b() # concise but slower version
    #sol = Solution2() # brute force

    comment = "LC example; answer = 49"
    arr = [1,8,6,2,5,4,8,3,7]
    test(arr, comment)

    comment = "LC test case; answer = 2"
    arr = [1,2,1]
    test(arr, comment)
