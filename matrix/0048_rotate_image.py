"""
48. Rotate Image
Medium

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""

from typing import List

###############################################################################
"""
Solution 1: transpose matrix, then reverse each row.
Can also reverse each column, then transpose matrix.

(r, c) -> (c, r) -> (c, n-r-1)

Note: to rotate 90 degrees CCW, can do either:
(1) transpose matrix, then reverse each row, OR
(2) reverse each column, then transpose matrix.

O(n^2) time
O(1) extra space

Runtime: 20 ms, faster than 99.70% of Python3 online submissions
Memory Usage: 12.9 MB, less than 97.92% of Python3 online submissions
"""
class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(m)

        # transpose matrix
        for i in range(n):
            for j in range(i+1, n):
                m[i][j], m[j][i] = m[j][i], m[i][j]

        # reverse each row (of transposed matrix)
        n1 = n - 1
        for i in range(n):
            for j in range(n//2):
                m[i][j], m[i][n1-j] = m[i][n1-j], m[i][j]


"""
Solution 1b: reverse each column, then transpose matrix
"""
class Solution1b:
    def rotate(self, m: List[List[int]]) -> None:
        n = len(m)
        m.reverse() # ie, reverse each column

        # transpose matrix
        for i in range(n):
            for j in range(i+1, n):
                m[i][j], m[j][i] = m[j][i], m[i][j]

###############################################################################
"""
Solution 2: do series of 4-position swaps.  Ie, rotate 4 rectanges at a time.

0,0     0, n    n,n     n, 0
0,1     1, n    n,n-1   n-1, 0
0,2     2, n    n,n-2   n-2, 0

1,1     1,n-1   n-1,n-1     n-1,1
1,2     2,n-1   n-1,n-2     n-2,1

r,c     c,n-r   n-r,n-c     n-c,r

Example:
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]] 

First elements of each 4-cycle:
[
  [ 5, 1, 9,  ],
  [  , 4,  ,  ],
  [  ,  ,  ,  ],
  [  ,  ,  ,  ]] 

"""
class Solution2:
    def rotate(self, m: List[List[int]]) -> None:
        n = len(m)

        for r in range(n//2):
            c = r
            c2 = r2 = n - r - 1

            for c in range(r, r2):
                #print(f"r,c = {r},{c}")
                m[r][c], m[c][r2], m[r2][c2], m[c2][r], = m[c2][r], m[r][c], m[c][r2], m[r2][c2]
                c2 -= 1

###############################################################################
"""
Solution 3: concise, but not in-place...
"""
class Solution3:
    def rotate(self, m: List[List[int]]) -> None:
        return [list(row[::-1]) for row in zip(*m)]
        
###############################################################################

if __name__ == "__main__":
    def print_matrix(mat):
        print()
        for row in mat:
            for x in row:
                print(f"{x:3}", end = "")
            print()

    def test(mat, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print_matrix(mat)
        res = sol.rotate(mat) # return value used for the non in-place solution

        if res:
            print(f"\nres = {res}\n")
        else:
            print_matrix(mat)


    #sol = Solution() # transpose matrix, then reverse each row
    sol = Solution1b() # reverse each column, then transpose matrix

    #sol = Solution2() # series of 4-position swaps
    
    #sol = Solution3() # concise, but not in-place

    comment = "LC ex1"
    mat = [
        [1,2,3],
        [4,5,6],
        [7,8,9]]
    test(mat, comment)

    comment = "LC ex2"
    mat = [
        [5,1,9,11],
        [2,4,8,10],
        [13,3,6,7],
        [15,14,12,16]]
    test(mat, comment)

    comment = "Trivial matrix"
    mat = [[1]]
    test(mat, comment)
