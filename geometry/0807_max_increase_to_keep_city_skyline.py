"""
807. Max Increase to Keep City Skyline
Medium

In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well. 

At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.

What is the maximum total sum that the height of the buildings can be increased?

Example:
Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
Output: 35

Explanation: 
The grid is:
[ [3, 0, 8, 4], 
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]

The skyline viewed from top or bottom is: [9, 4, 8, 7]
The skyline viewed from left or right is: [8, 7, 9, 3]

The grid after increasing the height of buildings without affecting skylines is:

gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]

Notes:

1 < grid.length = grid[0].length <= 50.
All heights grid[i][j] are in the range [0, 100].
All buildings in grid[i][j] occupy the entire grid cell: that is, they are a 1 x 1 x grid[i][j] rectangular prism.
"""

from typing import List

###############################################################################
"""
Solution: calculate row and column maxes. The building at (i, j) can be
increased up to the min of the row max or col max for (i, j) without
affecting any of the skylines.

O(n^2) time
O(n) extra space
"""
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        row_maxes = [0] * m # left and right views
        col_maxes = [0] * n # top and bottom views

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                col_maxes[j] = max(col_maxes[j], grid[i][j])
                row_maxes[i] = max(row_maxes[i], grid[i][j])

        res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += min(row_maxes[i], col_maxes[j]) - grid[i][j]
                
        return res
        
"""
Solution: Pythonic version
"""
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_maxes = [max(row) for row in grid] # left and right views
        col_maxes = [max(col) for col in zip(*grid)] # top and bottom views
        
        return sum(min(row_maxes[r], col_maxes[c]) - val
            for r, row in enumerate(grid)
            for c, val in enumerate(row))        
        