"""
213. House Robber II
Medium

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.

Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
"""

from typing import List

###############################################################################
"""
Solution:

Let houses be labeled 1, 2, ..., n.
If can rob house 1, then cannot rob house n.
If can't rob house 1, then can rob house n.
So the circular case reduces to two linear cases (LC198).

O(n) time
O(1) extra space
"""
class Solution:
    def rob(self, arr: List[int]) -> int:
        if not arr: # not needed for LC submission
            return 0
        
        n = len(arr)
        if n == 1:
            return arr[0]
        
        # Case 1: can rob house 1, but not house n.
        mx = prev_max = 0

        for i in range(n-1):
            prev_max, mx = mx, max(prev_max + arr[i], mx)

        # Case 2: cannot rob house 1, but can rob house n.
        mx2 = prev_max = 0

        for i in range(1, n):
            prev_max, mx2 = mx2, max(prev_max + arr[i], mx2)

        return max(mx, mx2)

"""
Solution 1b: one-pass version.
"""
class Solution1b:
    def rob(self, arr: List[int]) -> int:
        if not arr: # not needed for LC submission
            return 0
        
        n = len(arr)
        if n == 1:
            return arr[0]
        
        mx = prev_max = 0 # for case 1: can rob houses 1, ..., n-1
        mx2 = prev_max2 = 0 # for case 2: can rob houses 2, ..., n

        for i in range(n-1):
            prev_max, mx = mx, max(prev_max + arr[i], mx)
            prev_max2, mx2 = mx2, max(prev_max2 + arr[i+1], mx2)

        return max(mx, mx2)

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(arr)

        res = sol.rob(arr)

        print(f"\nres = {res}\n")


    sol = Solution()
    sol = Solution1b() # one-pass version

    comment = "LC ex1; answer = 3"
    arr = [2,3,2]
    test(arr, comment)

    comment = "LC ex2; answer = 4"
    arr = [1,2,3,1]
    test(arr, comment)

    comment = "LC test case; answer = 1"
    arr = [1]
    test(arr, comment)
