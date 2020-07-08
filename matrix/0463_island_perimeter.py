"""
463. Island Perimeter
Easy

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:

"""

from typing import List

###############################################################################
"""
Solution: simple, brute-force counting cell-by-cell. 
Check each square to see if it is a 1 (land), then check if its neighbors 
are off the grid or 0 (water).

O(mn) time
O(1) extra space

"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        perim = 0
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    if r == 0 or grid[r-1][c] == 0:
                        perim += 1
                    if c == 0 or grid[r][c-1] == 0:
                        perim += 1
                    if r == m-1 or grid[r+1][c] == 0:
                        perim += 1
                    if c == n-1 or grid[r][c+1] == 0:
                        perim += 1

        return perim

###############################################################################
"""
Solution 2: Count 1's on border of grid (corners are counted twice), and 
count transitions 0->1 and 1->0 within grid.

O(mn) time
O(1) extra space

"""
class Solution2:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # count 1's on border of grid (corners counted twice)
        perim = sum(grid[0]) + sum(grid[m-1]) + sum(row[0] + row[n-1] for row in grid)

        # count vertical transitions
        for r in range(m-1):
            for c in range(n):
                if grid[r][c] != grid[r+1][c]:
                    perim += 1

        # count horizontal transitions
        for r in range(m):
            for c in range(n-1):
                if grid[r][c] != grid[r][c+1]:
                    perim += 1

        return perim

###############################################################################
"""
Solution 3: traverse grid from left to right, and from top to bottom.
For each land cell, add 4 to total perimeter. Check if neighbors to left
and above are also land cells; if so, subtract 2 for each.

Same time and space complexities, but slightly more efficient since only
check 2 neighbors for each cell, rather than 4.

O(mn) time
O(1) extra space

"""
class Solution3:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        perim = 0
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    perim += 4

                    if r > 0 and grid[r-1][c] == 1:
                        perim -= 2
                    if c > 0 and grid[r][c-1] == 1:
                        perim -= 2

        return perim

###############################################################################

if __name__ == "__main__":
    def test(grid, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        for r in grid:
            for c in r:
                print(f"{c:2}", end="")
            print()

        res = sol.islandPerimeter(grid)

        print(f"\nresult = {res}\n")


    sol = Solution()  # check each cell's 4 neighbors
    sol = Solution2() # count 1's on border and transitions within grid
    sol = Solution3() # more efficient counting

    comment = "LC example; answer = 16"
    grid = [
        [0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]
    test(grid, comment)

    comment = "dcp392 example; answer = 14"
    grid = [
        [0,1,1,0],
        [1,1,1,0],
        [0,1,1,0],
        [0,0,1,0]]
    test(grid, comment)
