"""
198. House Robber
Easy

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""

from typing import List

###############################################################################
"""
Solution:

Never optimal to skip more than 2 houses.  Therefore, track:
(1) max amount robbed if we robbed the current house
(2) max amount robbed if the last house robbed was the previous one
(3) max amount robbed if the last house robbed was the one before the previous

Reasoning: Suppose we have houses 1 2 3 4 5, and skip 3 houses, eg, rob 
house 1 and 5.  Then could have robbed house 3 as well.

O(n) time
O(1) extra space
"""
class Solution:
    def rob(self, arr: List[int]) -> int:
        mx = mx1 = mx2 = 0
        
        for x in arr:
            mx2, mx1, mx = mx1, mx, max(mx2 + x, mx1 + x)
            
        return max(mx1, mx)

"""
Solution 1b: actually, only need to track 2 max vars.

n = 1: f(1) = a1
n = 2: f(2) = max(a1, a2)

n = 3: f(3) = max(a1 + a3, a2) = max(a1 + a3, max(a1, a2))

n = 4:

1 2 3 4   
x   x     mx
x     x   prev_max + x
  x   x   prev_max + x

When calculating mx = max(prev_max + x, mx) for position i, mx is referring
to the max as of position i-1, and prev_max is referring to the max as of
position i-2.

https://leetcode.com/problems/house-robber/solution/

"""
class Solution1b:
    def rob(self, arr: List[int]) -> int:
        mx = prev_max = 0

        for x in arr:
            prev_max, mx = mx, max(prev_max + x, mx)

        return mx

###############################################################################
"""
Follow up: print the houses to rob to get the max amount of money.

"""
class Followup:
    def rob(self, arr: List[int]) -> int:
        mx = prev_max = 0
        houses = []
        houses_prev = []

        for x in arr:
            temp = mx
            
            if prev_max + x > mx:
                mx = prev_max + x
                houses_prev, houses = houses, houses_prev + [x]
            else:
                houses_prev = houses
            
            prev_max = temp

        return houses

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
    sol = Solution1b()

    sol = Followup()

    comment = "LC ex1; answer = 4"
    arr = [1,2,3,1]
    test(arr, comment)

    comment = "LC ex2; answer = 12"
    arr = [2,7,9,3,1]
    test(arr, comment)

    comment = "LC test case; answer = 4"
    arr = [2,1,1,2]
    test(arr, comment)
