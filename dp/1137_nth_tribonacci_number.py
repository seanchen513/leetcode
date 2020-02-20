"""
1137. N-th Tribonacci Number
Easy

The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:

Input: n = 25
Output: 1389537

Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
"""

###############################################################################
"""
Solution 1: recursion w/ memoization via @functools.lru_cache().

O(n) time
O(n) extra space
"""
import functools
class Solution:
    @functools.lru_cache(None)
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        if n == 2:
            return 1

        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

###############################################################################
"""
Solution 2: tabulation

O(n) time
O(1) extra space
"""
class Solution2:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        if n == 2:
            return 1

        a, b, c = 0, 1, 1 # for n = 0, 1, 2

        for _ in range(3, n+1):
            a, b, c = b, c, a + b + c

        return c

###############################################################################

if __name__ == "__main__":
    def test(n, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(f"\nn = {n}")
        
        res = sol.tribonacci(n)
        print(f"\nres = {res}")


    sol = Solution() # memo via functools.lru_cache()
    sol = Solution2() # tabulation

    comment = "LC ex1; answer = 4"
    n = 4
    test(n, comment)
    
    comment = "LC ex2; answer = 1389537"
    n = 25
    test(n, comment)
