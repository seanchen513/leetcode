"""
892. Surface Area of 3D Shapes
Easy

On a N * N grid, we place some 1 * 1 * 1 cubes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Return the total surface area of the resulting shapes.

Example 1:

Input: [[2]]
Output: 10

Example 2:

Input: [[1,2],[3,4]]
Output: 34

Example 3:

Input: [[1,0],[0,2]]
Output: 16

Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32

Example 5:

Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46
 
Note:

1 <= N <= 50
0 <= grid[i][j] <= 50
"""

from typing import List

###############################################################################
"""
Solution 1: surface area for top and bottom are easy; for others, look at
absolute difference of heights horizontally and vertically.
"""
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        s = 2 * sum(1 for i in range(m) for j in range(n) if grid[i][j] > 0)
        
        for i in range(m):
            s += grid[i][0] + grid[i][-1]
            
            for j in range(1, n):
                s += abs(grid[i][j] - grid[i][j-1])
                
        for j in range(m):
            s += grid[0][j] + grid[-1][j]
            
            for i in range(1, m):
                s += abs(grid[i][j] - grid[i-1][j])
                
        return s
        
###############################################################################
"""
Solution 2: for each cell, look at 4 neighboring cells and take diff of heights
if neighboring cell has lower height.

https://leetcode.com/problems/surface-area-of-3d-shapes/solution/

"""
class Solution2:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        s = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    s += 2 # for top and bottom sides

                    # for each neighboring cell
                    for nr, nc in ((r-1,c), (r+1,c), (r,c-1), (r,c+1)):
                        if 0 <= nr < m and 0 <= nc < n:
                            n_val = grid[nr][nc]
                        else:
                            n_val = 0

                        s += max(grid[r][c] - n_val, 0)

        return s
