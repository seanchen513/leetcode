"""
746. Min Cost Climbing Stairs
Easy

On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
"""

from typing import List

###############################################################################
"""
Solution 1: recursion w/ memoization via @functools.lru_cache().

O(n) time: recursion
O(n) extra space: for recursion

Runtime: 56 ms, faster than 76.70% of Python3 online submissions
Memory Usage: 15.3 MB, less than 7.69% of Python3 online submissions
"""
import functools
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @functools.lru_cache(None)
        def rec(i):
            if i >= n:
                return cost[i]
                
            return cost[i] + min(rec(i+1), rec(i+2))

        n = len(cost) - 2 # index for 2nd to last step

        return min(rec(0), rec(1))

###############################################################################
"""
Solution 2: tabulation w/ dp array.

O(n) time
O(n) extra space: for dp[]

Runtime: 52 ms, faster than 91.78% of Python3 online submissions
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

        return min(dp[-1], dp[-2])

"""
Solution 2b: tabulation w/ 2 vars.

Runtime: 48 ms, faster than 98.16% of Python3 online submissions
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions
"""
class Solution2b:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # min costs to end up at steps 0 and 1
        f1, f2 = cost[0], cost[1] 

        for c in cost[2:]:
            f1, f2 = f2, min(f1, f2) + c
            
        return min(f1, f2)

###############################################################################

if __name__ == "__main__":
    def test(cost, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(f"\ncosts = {cost}")
        
        res = sol.minCostClimbingStairs(cost)
        print(f"\nres = {res}")


    sol = Solution() # memo w/ functools.lru_cache()
    sol = Solution2() # tabulation w/ dp array
    sol = Solution2b() # tabulation w/ 2 vars

    comment = "LC ex1; answer = 15"
    cost = [10,15,20]
    test(cost, comment)
    
    comment = "LC ex1; answer = 6"
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    test(cost, comment)
