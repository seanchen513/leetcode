"""
62. Unique Paths
Medium

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Above is a 7 x 3 grid. How many possible unique paths are there?

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:

Input: m = 7, n = 3
Output: 28
 
Constraints:
1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.
"""

import math
import functools
import operator

###############################################################################
"""
Solution 1: use math.comb() (Python 3.8).

Danger of overflow.

O( (m+n) (log(m+n) log log(m+n) )^2 ) time: if factorial is computed as
product of prime powers.  This beats O(mn) time of DP solutions.

O(1) extra space
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m+n-2,m-1) # Python 3.8

"""
Solution 1b: use math.factorial.

Danger of overflow.

O( (m+n) (log(m+n) log log(m+n) )^2 ) time: if factorial is computed as
product of prime powers.

O(1) extra space

On the Complexity of Calculating Factorials, 1983, Peter Borwein
http://www.cecm.sfu.ca/personal/pborwein/PAPERS/P29.pdf

Python3 implementation: built-in divide & conquer factorial algo
https://bugs.python.org/issue8692

Factorial algos:
http://www.luschny.de/math/factorial/description.html
"""
class Solution1b:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.factorial(m+n-2) // math.factorial(m-1) // math.factorial(n-1)

"""
Solution 1c: do multiplications instead of factorials.

Danger of overflow.

O(min(m,n)^2) time ?
O(1) extra space
"""
class Solution1c:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1

        # Make sure m is the bigger integer.
        if n > m:
            m, n = n, m

        return int(functools.reduce(operator.mul, range(m, m+n-1), 1) /
            functools.reduce(operator.mul, range(2, n), 1))

        # return int(functools.reduce(lambda x, y: x*y, range(m, m+n-1), 1) /
        #     functools.reduce(lambda x, y: x*y, range(2, n), 1))

###############################################################################
"""
Solution 2: DP.

O(mn) time
O(mn) extra space for dp table.
"""
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        # Need cells in first row and first column to be initialized to 1.
        dp = [[1]*n for _ in range(m)] # m-by-n grid

        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]

        return dp[-1][-1]

###############################################################################
"""
Solution 3: recursion w/ memoization via @functools.lru_cache().

TLE w/ memoization.
"""
import functools
class Solution3:
    @functools.lru_cache(None)
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1

        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)

###############################################################################

if __name__ == "__main__":
    def test(m, n, comment=None):
        print("="*80)
        if comment:
            print(comment)
              
        print(f"\nm = {m}")
        print(f"n = {n}")

        res = sol.uniquePaths(m, n)

        print(f"\nres = {res}\n")


    sol = Solution() # use math.comb()
    sol = Solution1b() # use math.factorial()
    sol = Solution1c() # do multiplcations 
    
    #sol = Solution2() # DP
    #sol = Solution3() # memoization

    comment = "LC ex1; answer = 2"
    m = 3
    n = 2
    test(m, n, comment)
    
    comment = "LC ex2; answer = 28"
    m = 7
    n = 3
    test(m, n, comment)
    
    comment = "LC test case; answer = 28"
    m = 3
    n = 7
    test(m, n, comment)

    comment = "LC test case; TLE's simple recursion; answer = 193,536,720"
    m = 23
    n = 12
    test(m, n, comment)
