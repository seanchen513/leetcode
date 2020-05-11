"""
1314. Matrix Block Sum
Medium

Given a m * n matrix mat and an integer K, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for i - K <= r <= i + K, j - K <= c <= j + K, and (r, c) is a valid position in the matrix.
 
Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]

Example 2:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]
 
Constraints:

m == mat.length
n == mat[i].length
1 <= m, n, K <= 100
1 <= mat[i][j] <= 100
"""

from typing import List

###############################################################################
"""
Solution: use prefix block sums.

Technique of integral image, aka, summed-area table.

References:
https://leetcode.com/problems/matrix-block-sum/discuss/482730/Python-O(-m*n-)-sol.-by-integral-image-technique.-90%2B-with-Explanation
https://en.wikipedia.org/wiki/Summed-area_table

O(mn) time
O(mn) extra space: for prefix sums

"""
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        # if k >= m-1 and k >= n-1:
        #     s = sum(sum(row) for row in mat)
        #     return [[s] * n for _ in range(m)]
        
        # Calculate prefix sums.
        # Dummy first row of 0's, and dummy first column of 0's.
        # Uses shifted indices.
        p = [[0] * (n+1) for _ in range(m+1)] 
        
        """
        for r in range(1, m+1):
            for c in range(1, n+1):
                p[r][c] = p[r-1][c] + p[r][c-1] - p[r-1][c-1] + mat[r-1][c-1]
        """

        for r in range(1, m+1):
            s = 0

            for c in range(1, n+1):
                s += mat[r-1][c-1]
                p[r][c] = s + p[r-1][c]

                # if r > 1:
                #     p[r][c] += p[r-1][c]

        res = [[0] * n for _ in range(m)]
        
        # r, c = actual indices for use with mat and res
        # r2, c2 = shifted indices for use with p
        
        for r in range(m): # actual index
            
            #r1 = max(-1, r-k-1) + 1
            #r2 = min(m-1, r+k) + 1
            
            r1 = max(0, r-k)
            r2 = min(m, r+k+1)
            
            pr1 = p[r1]
            pr2 = p[r2]
            
            for c in range(n):
                # c1 = max(-1, c-k-1) + 1
                # c2 = min(n-1, c+k) + 1

                c1 = max(0, c-k)
                c2 = min(n, c+k+1)
  
                # unshifted indices:
                # res[r][c] = p[r+k][c+k] - p[r+k][c-k-1] - p[r-k][c+k] + p[r-k-1][c-k-1]
        
                #res[r][c] = p[r2][c2] - p[r2][c1] - p[r1][c2] + p[r1][c1]
                
                res[r][c] = pr2[c2] - pr2[c1] - pr1[c2] + pr1[c1]
                
        return res
    
###############################################################################
"""
Solution 2: same, but don't use dummy row and column for matrix of prefix sums.
Use "if" statements instead.

"""
class Solution2:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        # if k >= m-1 and k >= n-1:
        #     s = sum(sum(row) for row in mat)
        #     return [[s] * n for _ in range(m)]
        
        # Calculate prefix sums.
        p = [[0] * n for _ in range(m)] 
        
        for r in range(m):
            s = 0

            for c in range(n):
                s += mat[r][c]
                p[r][c] = s

                if r > 0:
                    p[r][c] += p[r-1][c]

        res = [[0] * n for _ in range(m)]
        
        for r in range(m):
            r1 = r-k-1
            r2 = min(m-1, r+k)
            
            for c in range(n):
                c1 = c-k-1
                c2 = min(n-1, c+k)
  
                res[r][c] = p[r2][c2]

                if r1 >= 0:
                    res[r][c] -= p[r1][c2]

                if c1 >= 0:
                    res[r][c] -= p[r2][c1]

                if r1 >= 0 and c1 >= 0:
                    res[r][c] += p[r1][c1]

        return res
