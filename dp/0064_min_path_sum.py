"""
64. Minimum Path Sum
Medium

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

from typing import List

###############################################################################
"""
Solution 1: tabulation.

Create dp table with same size as input grid rather than modifying input grid.

O(mn) time: single traversal of matrix.
O(mn) extra space: for dp matrix.  O(1) if in-place.

It's possible to use a 1-d dp table.

Runtime: 100 ms, faster than 77.40% of Python3 online submissions
Memory Usage: 14.4 MB, less than 70.18% of Python3 online submissions
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])
        INF = float('inf')
        dp = [[INF] * n_cols for _ in range(n_rows)]
        
        # No choice for first cell.
        dp[0][0] = grid[0][0]

        # Initialize first column.
        for i in range(1, n_rows):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        # Initialize first row.
        for j in range(1, n_cols):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        # Calculate all other cells.
        for i in range(1, n_rows):
            for j in range(1, n_cols):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[-1][-1]

"""
Solution 1b: same as sol #1, but in-place.

Runtime: 92 ms, faster than 96.85% of Python3 online submissions
Memory Usage: 14.5 MB, less than 66.67% of Python3 online submissions
"""
class Solution1b:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])
        
        # Initialize first column.
        for i in range(1, n_rows):
            grid[i][0] = grid[i-1][0] + grid[i][0]

        # Initialize first row.
        for j in range(1, n_cols):
            grid[0][j] = grid[0][j-1] + grid[0][j]

        # Calculate all other cells.
        for i in range(1, n_rows):
            for j in range(1, n_cols):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]

        return grid[-1][-1]

"""
Solution 1c: tabulation with 1-d DP table.

Runtime: 92 ms, faster than 96.85% of Python3 online submissions
Memory Usage: 13.4 MB, less than 94.74% of Python3 online submissions
"""
class Solution1c:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])

        dp = grid[0]

        for j in range(1, n_cols):
            dp[j] = dp[j-1] + grid[0][j]
        
        for i in range(1, n_rows):
            dp[0] = dp[0] + grid[i][0]

            for j in range(1, n_cols):
                dp[j] = min(dp[j-1], dp[j]) + grid[i][j]

        return dp[-1]

###############################################################################
"""
Solution 2: recursion w/ memoization via @functools.lru_cache(None).

O(2^(m+n)) time w/o memo: for most cell, there are 2 moves.
O(m+n) extra space: for recursion.

Runtime: 108 ms, faster than 42.48% of Python3 online submissions
Memory Usage: 18.4 MB, less than 17.54% of Python3 online submissions
"""
import functools
class Solution2:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def rec(r, c): # returns min path sum ending at (r, c)
            if r == 0 and c == 0:
                return grid[0][0]

            if r == 0: # c != 0
                return rec(0, c-1) + grid[r][c]
            
            if c == 0: # r != 0
                return rec(r-1, 0) + grid[r][c]

            # r != 0 and c != 0
            return min(rec(r-1, c), rec(r, c-1)) + grid[r][c]

        # start with cell at end of path, ie, bottom right corner
        return rec(len(grid)-1, len(grid[0])-1) 

"""
Solution 2b: recursion w/ memo, recursing in other direction.
"""
import functools
class Solution2b:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def rec(r, c): # returns min path sum starting at (r, c)
            if r == last_r and c == last_c:
                return grid[r][c]

            if r == last_r: # c != last_c
                return rec(r, c+1) + grid[r][c]
            
            if c == last_c: # r != last_r
                return rec(r+1, c) + grid[r][c]

            # r != last_r and c != last_c
            return min(rec(r, c+1), rec(r+1, c)) + grid[r][c]

        last_r = len(grid) - 1
        last_c = len(grid[0]) - 1

        return rec(0, 0) 

###############################################################################

if __name__ == "__main__":
    def test(grid, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        for row in grid:
            print(row)

        res = sol.minPathSum(grid)
        print(f"\nres = {res}")


    sol = Solution() # tabulation using created dp table
    sol = Solution1b() # tabulation, in-place
    sol = Solution1c() # tabulation with 1-d DP table
    #sol = Solution2() # memo, starting at end
    sol = Solution2b() # memo, starting at beginning

    comment = "LC example; answer = 7"
    grid = [
        [1,3,1],
        [1,5,1],
        [4,2,1]]
    test(grid, comment)

    comment = "LC test case; answer = 85"
    grid = [
        [7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],
        [9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],
        [8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],
        [6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],
        [7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],
        [9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],
        [1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],
        [3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],
        [1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],
        [5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],
        [2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],
        [0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]
    test(grid, comment)
