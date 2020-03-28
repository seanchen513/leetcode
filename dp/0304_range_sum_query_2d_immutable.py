"""
304. Range Sum Query 2D - Immutable
Medium

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12

Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
"""

from typing import List

###############################################################################
"""
Solution: precalculate and store prefix sums for rectangles.

O(1) time for queries
O(mn) time to precalculate prefix sums

O(mn) extra space
"""
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            #self.sums = None
            return
            
        self.sums = [[0] * (len(matrix[0]) + 1)]

        for i in range(len(matrix)):
            s = 0
            lst = [0]

            for j in range(len(matrix[0])):
                s += matrix[i][j]
                lst.append(s + self.sums[i][j+1])

            self.sums.append(lst)

        print (self.sums)
            
    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        #if not self.sums:
        #    return 0
        
        return ( self.sums[r2+1][c2+1] + self.sums[r1][c1] 
            - self.sums[r2+1][c1] - self.sums[r1][c2+1] )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

###############################################################################
"""
Solution 2: precalculate and store prefix sums for rectangles.

Same as sol 1, but calculate the prefix sums differently.

O(1) time for queries
O(mn) time to precalculate prefix sums

O(mn) extra space
"""
class NumMatrix2:
    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            #self.sums = None
            return

        m = len(matrix)
        n = len(matrix[0])

        self.sums = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                self.sums[i+1][j+1] = ( self.sums[i+1][j] + self.sums[i][j+1]
                    - self.sums[i][j] + matrix[i][j] )

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        #if not self.sums:
        #    return 0
        
        return ( self.sums[r2+1][c2+1] + self.sums[r1][c1] 
            - self.sums[r2+1][c1] - self.sums[r1][c2+1] )
