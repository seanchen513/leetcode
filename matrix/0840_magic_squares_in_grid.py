"""
840. Magic Squares In Grid
Easy

A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1

Explanation: 
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
0 <= grid[i][j] <= 15
"""

from typing import List

###############################################################################
"""
Solution:

Sum of a magic square is:
1 + 2 + .. + 9 = (1 + 9)*9 / 2 = 45.

So each row, column, and diagonal must have sum 15.

Optional: the middle square x must be 5.
Proof: there are 4 lines that cross the center and sum up to the sum of the
entire grid plus 3 extra copies of the center.  That is,
4*15 = 45 + 3*x.
Solving gives x = 5.

### Not used in code here:

The even numbers must be in the corners, and the odds (other than 5)
must be on the non-corners.

The sequence of numbers along the edges must follow the
cycle (29438167), clockwise or CCW.

Example:
2 9 4
7 5 3
6 1 8

"""
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def check(r, c):
            if s9 != set(grid[i][j] for i in range(r,r+3) for j in range(c,c+3)):
                return 0

            #if 15 != grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2]:
            if 10 != grid[r][c] + grid[r+2][c+2]:
                return 0

            #if 15 != grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c]:
            if 10 != grid[r][c+2] + grid[r+2][c]:
                return 0

            ### Check rows
            for i in range(r, r+3):
                #if 15 != sum(grid[i][c:c+3]):
                if 15 != sum(grid[i][j] for j in range(c, c+3)):
                    return False
            
            ### Check columns
            for j in range(c, c+3):
                if 15 != sum(grid[i][j] for i in range(r, r+3)):
                    return 0
            
            return 1
            
        count = 0
        m = len(grid)
        n = len(grid[0])
        s9 = set(range(1,10))

        for r in range(m-2):
            for c in range(n-2):
                # optional check for center square.
                if grid[r+1][c+1] == 5:
                    count += check(r, c)
                    
        return count
