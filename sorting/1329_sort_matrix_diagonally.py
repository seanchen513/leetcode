"""
1329. Sort the Matrix Diagonally
Medium

Given a m * n matrix mat of integers, sort it diagonally in ascending order from the top-left to the bottom-right then return the sorted array.

Example 1:

Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100
"""

from typing import List
import collections

###############################################################################
"""
Solution: copy each diagonal into an array, sort array, then copy sorted
array into new matrix along same diagonal.

Example:
m = 3
n = 4

0,0 0,1 0,2 0,3
1,0 1,1 1,2 1,3
2,0 2,1 2,2 2,3

upper diagonals, including main diagonal based at 0,0:
diff = c - r >= 0
diff = 0, 1, ..., n-1
r = 0..m-1, but stop early if c = r + diff >= n

lower diagonals, excluding main diagonal:
diff = r - c >= 0
diff = 1, 2, ..., m-1
c = 0..n-1, but stop early if r = c + diff >= m

###
Longest diagonal has length min(m, n).

O((m+n) log min(m,n)) time
O(min(m,n)) extra space, excluding output
O(mn) extra space for output, if don't modify input matrix

"""
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        s = [[0] * n for _ in range(m)] # sorted matrix

        # upper diagonals
        for diff in range(n):
            arr = []
            
            for r in range(m):
                c = r + diff
                if c >= n:
                    break
                arr.append(mat[r][c])

            arr.sort()

            # copy sorted values into diagonal of sorted matrix
            for r in range(m):
                c = r + diff
                if c >= n:
                    break
                s[r][c] = arr[r]

        # lower diagonals
        for diff in range(1, m):
            arr = []
            
            for c in range(n):
                r = c + diff
                if r >= m:
                    break
                arr.append(mat[r][c])

            arr.sort()

            # copy sorted values into diagonal of sorted matrix
            for c in range(n):
                r = c + diff
                if r >= m:
                    break
                s[r][c] = arr[c]

        return s

###############################################################################
"""
Solution 2: use dict that maps difference c - r to list holding values for
the diagonal with that difference. Then sort each list in dict. Then use
dict to fill in sorted matrix.

O(mn) time
O(mn) extra space: for dict and for output
"""
class Solution2:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        s = [[0] * n for _ in range(m)] # sorted matrix

        d = collections.defaultdict(list)

        for r in range(m):
            for c in range(n):
                d[c - r].append(mat[r][c])

        for k in d:
            d[k].sort()

        for r in range(m):
            for c in range(n):
                diff = c - r
                if diff >= 0:
                    # Elements in each upper diagonal indexed by row number.
                    s[r][c] = d[diff][r]

                else:
                    # Elements in each lower diagonal indexed by column number.
                    s[r][c] = d[diff][c]

        return s

###############################################################################
"""
Solution 3:

https://leetcode.com/problems/sort-the-matrix-diagonally/discuss/489846/Several-Python-solutions

"""
class Solution3:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        def sort(i, j):
            arr = []

            while i < m and j < n:
                arr.append(mat[i][j])
                i += 1
                j += 1

            arr.sort()

            while i and j:
                i -= 1
                j -= 1
                s[i][j] = arr.pop()

        m = len(mat)
        n = len(mat[0])

        s = [[0] * n for _ in range(m)] # sorted matrix

        # lower diagonals
        for i in range(m):
            sort(i, 0)

        # upper diagonals
        for j in range(n):
            sort(0, j)

        return s
