"""
70. Climbing Stairs
Easy

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

###############################################################################
"""
Solution 1: recursion w/ memoization via @functools.lru_cache().

O(n) time
O(n) extra space

Without memoization, this would be O(2^n) time due to branching factor of 2
and recursion depth of n.  It would still be O(n) extra space for recursion.

Runtime: 28 ms, faster than 58.33% of Python3 online submissions
Memory Usage: 12.9 MB, less than 98.51% of Python3 online submissions
"""
import functools
class Solution:
    @functools.lru_cache(None)
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        return self.climbStairs(n-1) + self.climbStairs(n-2)

###############################################################################
"""
Solution 2: tabulation.

O(n) time
O(1) extra space

Runtime: 24 ms, faster than 84.53% of Python3 online submissions
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        f1, f2 = 1, 2

        for _ in range(3, n+1):
            f1, f2 = f2, f1 + f2

        return f2

###############################################################################
"""
Solution 3: use math formula for Fibonacci numbers involving golden ratio.
"""
class Solution3:
    def climbStairs(self, n: int) -> int:
        phi = (1 + 5**0.5) / 2

        return int(( phi**(n+1) - (1-phi)**(n+1) ) / 5**0.5)

###############################################################################

if __name__ == "__main__":
    def test(n, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(f"\nn = {n}")
        
        res = sol.climbStairs(n)
        print(f"\nres = {res}")


    sol = Solution() # memo via functools.lru_cache()
    sol = Solution2() # tabulation
    #sol = Solution3() # use math

    comment = "LC ex1; answer = 2"
    n = 2
    test(n, comment)
    
    comment = "LC ex2; answer = 3"
    n = 3
    test(n, comment)

    comment = "answer = 90"
    n = 10
    test(n, comment)

    comment = "answer = 10946"
    n = 20
    test(n, comment)

    comment = "answer = 1346269"
    n = 30
    test(n, comment)
