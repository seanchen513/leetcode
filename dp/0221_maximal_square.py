"""
221. Maximal Square
Medium

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""

from typing import List

###############################################################################
"""
Solution 1: recursion w/ memoization via @functools.lru_cache().
Start with last cell.

TLE w/o memoization

Runtime: 228 ms, faster than 37.22% of Python3 online submissions
Memory Usage: 22.9 MB, less than 9.09% of Python3 online submissions
"""
import functools
class Solution:
    def maximalSquare(self, mat: List[List[str]]) -> int:
        @functools.lru_cache(None)
        def rec(r, c):
            nonlocal mx
            
            if r < 0 or c < 0:
                return 0
            
            # Calculate this even if mat[r][c] == '0' in order to traverse
            # all cells of the matrix.
            length = min(rec(r-1, c), rec(r, c-1), rec(r-1, c-1)) + 1
            
            if mat[r][c] == '1':        
                mx = max(mx, length)
                return length
            
            return 0
        
        if not mat:
            return 0
        
        m = len(mat)
        n = len(mat[0])
        mx = 0
        
        rec(m-1, n-1)
        
        return mx * mx
             
"""
Solution 1b: recursion w/ memoization via @functools.lru_cache().
Start with first cell.

TLE w/o memoization
"""
import functools
class Solution1b:
    def maximalSquare(self, mat: List[List[str]]) -> int:
        @functools.lru_cache(None)
        def rec(r, c):
            nonlocal mx
            
            if r >= m or c >= n:
                return 0
            
            length = min(rec(r+1, c), rec(r, c+1), rec(r+1, c+1)) + 1
            
            if mat[r][c] == '1':        
                mx = max(mx, length)
                return length
            
            return 0
        
        if not mat:
            return 0
        
        m = len(mat)
        n = len(mat[0])
        mx = 0
        
        rec(0, 0)
        
        return mx * mx

"""
Solution 1c: rewrite.
Recursion w/ memoization via @functools.lru_cache().
Start with first cell.

TLE w/o memoization
"""
import functools
class Solution1c:
    def maximalSquare(self, mat: List[List[str]]) -> int:
        @functools.lru_cache(None)
        def rec(r, c):
            nonlocal max_width

            if r > 0:
                left = rec(r-1, c)
            if c > 0:
                up = rec(r, c-1)

            if r == 0 or c == 0:
                w = int(mat[r][c] == '1')
            elif mat[r][c] == '0':
                return 0
            else:
                w = min(left, up, rec(r-1, c-1)) + 1

            max_width = max(max_width, w)
            return w

        if not mat:
            return 0

        m = len(mat)
        n = len(mat[0])
        max_width = 0

        rec(m-1, n-1)

        return max_width * max_width

"""
Solution 1d: rewrite.
Recursion w/ memoization via @functools.lru_cache().
Start with first cell.

TLE w/o memoization

Runtime: 232 ms, faster than 34.83% of Python3 online submissions
Memory Usage: 22.6 MB, less than 9.09% of Python3 online submissions
"""
import functools
class Solution1d:
    def maximalSquare(self, mat: List[List[str]]) -> int:
        @functools.lru_cache(None)
        def rec(r, c):
            nonlocal max_width

            if r < m - 1:
                right = rec(r+1, c)

            if c < n - 1:
                down = rec(r, c+1)

            if r == m - 1 or c == n - 1:
                w = int(mat[r][c] == '1')
            elif mat[r][c] == '0':
                return 0
            else:
                w = min(right, down, rec(r+1, c+1)) + 1

            max_width = max(max_width, w)

            return w
                
        if not mat:
            return 0

        m = len(mat)
        n = len(mat[0])
        max_width = 0

        rec(0, 0)

        return max_width * max_width

###############################################################################
"""
Solution 2: DP tabulation w/ 1d table, padded.  Iterate row by row from start.

dp[i] = max length of square of 1s *ending* at cell (i,j) for j...

O(mn) time
O(n) extra space: for dp array
"""
class Solution2:
    def maximalSquare(self, mat: List[List[str]]) -> int:
        if not mat:
            return 0

        m = len(mat)
        n = len(mat[0])
        max_d = 0

        # dp[0] always 0 to serve as dummy value when evaluating j=1 in
        # loop below (for first column of matrix).
        # Also, dp all 0s initially to act as dummy values when evaluating
        # i = 0 in loop below (first row of matrix).
        dp = [0] * (n+1) 
        prev = 0

        for i in range(m):
            for j in range(1, n+1):
                temp = dp[j]

                if mat[i][j-1] == '1':
                    dp[j] = min(dp[j], dp[j-1], prev) + 1
                    max_d = max(max_d, dp[j])
                else:
                    dp[j] = 0

                prev = temp

        return max_d * max_d

###############################################################################
"""
Solution 2b: DP tabulation w/ 2d table.  Iterate row by row from start.

dp[i][j] = max length of square of 1s *ending* at cell (i,j)

O(mn) time
O(mn) extra space: for dp table, if don't want to modify given matrix

Runtime: 188 ms, faster than 94.56% of Python3 online submissions
Memory Usage: 14 MB, less than 31.82% of Python3 online submissions

With some minor optimizations (assign variables to dp[i] and dp[i-1] and
replace max() with "if" statement):
Runtime: 176 ms, faster than 99.56% of Python3 online submissions
Memory Usage: 13.9 MB, less than 81.82% of Python3 online submissions
"""
class Solution2b:
    def maximalSquare(self, mat: List[List[str]]) -> int:
        if not mat:
            return 0

        m = len(mat)
        n = len(mat[0])
        max_d = 0

        dp = [[0]*n for _ in range(m)]

        for i in range(m):
            if mat[i][0] == '1':
                dp[i][0] = 1 
                max_d = 1

        for j in range(n):
            if mat[0][j] == '1':
                dp[0][j] = 1
                max_d = 1

        for i in range(1, m):
            for j in range(1, n):
                if mat[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_d = max(max_d, dp[i][j])

        # print()
        # for row in dp:
        #     print(row)

        return max_d * max_d

"""
Solution 2c: DP tabulation w/ 2d table.  Iterate row by row in reverse from end.

dp[i][j] = max length of square of 1s *starting* at cell (i,j)

O(mn) time
O(mn) extra space: for dp table, if don't want to modify given matrix

Runtime: 192 ms, faster than 90.15% of Python3 online submissions
Memory Usage: 14 MB, less than 31.82% of Python3 online submissions
"""
class Solution2c:
    def maximalSquare(self, mat: List[List[str]]) -> int:
        if not mat:
            return 0

        m = len(mat)
        n = len(mat[0])
        max_d = 0

        dp = [[0]*n for _ in range(m)]

        for i in range(m):
            if mat[i][n-1] == '1':
                dp[i][n-1] = 1 
                max_d = 1

        for j in range(n):
            if mat[m-1][j] == '1':
                dp[m-1][j] = 1
                max_d = 1

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                if mat[i][j] == '1':
                    dp[i][j] = min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1]) + 1
                    max_d = max(max_d, dp[i][j])

        # for row in dp:
        #     print(row)

        return max_d * max_d

###############################################################################
"""
Solution: iteration over widths from 2 to min(n,m), passing over matrix
each iteration.

dp[i][j] = max length of square of 1s *starting* at cell (i,j)

SLOW

Runtime: 528 ms, faster than 5.83% of Python3 online submissions
Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions
"""
class Solution3:
    def maximalSquare(self, mat: List[List[str]]) -> int:
        if not mat:
            return 0

        m = len(mat)
        n = len(mat[0])
        max_d = 0

        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == '1':
                    dp[i][j] = 1
                    max_d = 1

        if max_d == 0:
            return 0

        for d in range(2, min(n,m) + 1):
            d1 = d - 1
            for i in range(m-d+1):
                for j in range(n-d+1):
                    if dp[i][j] == d1 and dp[i+1][j] == d1 and dp[i][j+1] == d1 and dp[i+1][j+1] == d1:
                        dp[i][j] = d
                        max_d = d
                        #print(f"max_d = {max_d}")

        return max_d * max_d

###############################################################################
"""
Solution 4: brute force iteration.  Check each cell one at a time.

Runtime: 388 ms, faster than 11.38% of Python3 online submissions
Memory Usage: 14 MB, less than 22.73% of Python3 online submissions
"""
class Solution4:
    def maximalSquare(self, mat: List[List[str]]) -> int:
        def max_square_width(r, c):
            d = 1 # loop pre: d is width of known square of 1s.

            while r + d < m and c + d < n:
                # Test column just outside known square of 1s.
                if any(mat[i][c+d] == '0' for i in range(r, r+d+1)):
                    return d

                # Test row just outside known square of 1s.
                if any(mat[r+d][j] == '0' for j in range(c, c+d)):
                    return d

                d += 1

            return d

        if not mat:
            return 0

        m = len(mat)
        n = len(mat[0])
        max_w = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] == '1' and i + max_w < m and j + max_w < n:
                    max_w = max(max_w, max_square_width(i, j))

        return max_w * max_w

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

        ### Convert grid values to strings.
        for i in range(len(grid)):
            grid[i] = list(map(str, grid[i]))

        res = sol.maximalSquare(grid)

        print(f"\nres = {res}\n")


    sol = Solution() # recursion w/ memoization, start with last cell
    sol = Solution1b() # recursion w/ memoization, start with first cell
    sol = Solution1c() # rewrite, start with last cell
    sol = Solution1d() # rewrite, start with first cell

    sol = Solution2() # improved tabulation w/ dp array
    #sol = Solution2b() # tabulation; iterate row by row from start
    #sol = Solution2c() # tabulation; iterate in reverse row by row from end

    #sol = Solution3() # iterate over widths, passing over matrix each time
    #sol = Solution4() # brute force iteration

    comment = "LC example; answer = 4"
    grid = [
        [1,0,1,0,0],
        [1,0,1,1,1],
        [1,1,1,1,1],
        [1,0,0,1,0]]
    test(grid, comment)

    comment = "LC test case; answer = 0"
    grid = []
    test(grid, comment)

    comment = "LC test case; answer = 0"
    grid = [['0']]
    test(grid, comment)

    comment = "LC test case; answer = 1"
    grid = [['1']]
    test(grid, comment)

    comment = "LC test case; answer = 0"
    grid = [
        ['0','0']]
    test(grid, comment)

    comment = "LC test case; answer = 1"
    grid = [
        ['0','1']]
    test(grid, comment)

    comment = "column matrix; answer = 1"
    grid = [
        ['0'],
        ['1'],
        ['0']
        ]
    test(grid, comment)

    comment = "LC test case; answer = 1"
    grid = [
        ['1','0'],
        ['1','0']]
    test(grid, comment)

    comment = "LC test case; answer = 4"
    grid = [
        ['1','1'],
        ['1','1']]
    test(grid, comment)

    comment = "LC test case; answer = 16"
    grid = [
        ["1","1","1","0","0"],
        ["1","1","1","0","0"],
        ["1","1","1","1","1"],
        ["0","1","1","1","1"],
        ["0","1","1","1","1"],
        ["0","1","1","1","1"]]
    test(grid, comment)
