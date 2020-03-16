"""
63. Unique Paths II
Medium

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2

Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""

from typing import List

###############################################################################
"""
Solution: tabulation.

O(mn) time
O(mn) extra space if don't want to modify input matrix: for dp matrix
O(1) extra space if use input matrix as dp matrix
"""
class Solution:
    #def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0]*n for _ in range(m)]

        for i in range(m):
            if grid[i][0] == 1: # obstacle
                break
            dp[i][0] = 1

        for j in range(n):
            if grid[0][j] == 1: # obstacle
                break
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] != 1: # obstacle
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # print()
        # for row in dp:
        #     print(row)

        return dp[-1][-1]

"""
Solution 1b: same as sol 1, but use slightly larger dp table to combine
loops into one, avoiding initialization for first row and first column.
The extra row and extra column in the dp table acts as dummy 0 values when
doing calculations.
"""
class Solution1b:
    #def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0]*(n+1) for _ in range(m+1)]
        if grid[0][0] == 1: # obstacle at entrance
            return 0 
        else:
            dp[0][1] = 1 # seed value

        for i in range(1, m+1):
            for j in range(1, n+1):
                if grid[i-1][j-1] != 1: # obstacle
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        print()
        for row in dp:
            print(row)

        return dp[-1][-1]

"""
Solution 1c: use dp array instead of matrix.

O(mn) time
O(m) extra space: for dp array
"""
class Solution1c:
    #def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [1] + [0] * (n-1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: # obstacle
                    dp[j] = 0
                elif j > 0: # dp[0] stays at 1 unless an obstacle sets it to 0
                    dp[j] += dp[j-1]

        return dp[-1]

###############################################################################
"""
Solution: recursion w/ memoization via @functools.lru_cache().

TLE w/o memoization.
"""
import functools
class Solution2:
    #def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def rec(r, c):
            if grid[r][c] == 1: # obstacle
                return 0

            if r == 0 and c == 0:
                return 1

            if r == 0:
                return rec(r, c-1)

            if c == 0:
                return rec(r-1, c)

            return rec(r-1, c) + rec(r, c-1)

        m = len(grid)
        n = len(grid[0])

        return rec(m-1, n-1)

###############################################################################

if __name__ == "__main__":
    def test(grid, comment=None):
        print("="*80)
        if comment:
            print(comment)
              
        print()
        for row in grid:
            for x in row:
                print(f"{x:3}", end="")
            print()

        res = sol.uniquePathsWithObstacles(grid)

        print(f"\nres = {res}\n")

    sol = Solution() # tabulation
    sol = Solution1b() # tabulation; use slightly larger dp table
    sol = Solution1c() # tabulation: use dp array

    #sol = Solution2() # memoization

    comment = "LC example; answer = 2"
    grid = [
        [0,0,0],
        [0,1,0],
        [0,0,0]]
    test(grid, comment)

    comment = "answer = 0"
    grid = [
        [1,0,0],
        [0,0,0],
        [0,0,0]]
    test(grid, comment)
