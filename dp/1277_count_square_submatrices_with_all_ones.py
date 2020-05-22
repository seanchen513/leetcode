"""
1277. Count Square Submatrices with All Ones
Medium

Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15

Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7

Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 
Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
"""

from typing import List

###############################################################################
"""
Solution 1: DP tabulation using 2d table.

Can use separate 2d table, modify input matrix to use as 2d table, or
use 1d table. Here we modify the input matrix.

dp[r][c] = number of submatrices with all 1's that end at cell (r,c).
= 0 if mat[r][c] == 0
= 1 + min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) if mat[r][c] == 1

O(mn) time

O(1) extra space: if modify input
O(mn) extra space: if don't modify input

"""
class Solution:
    def countSquares(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        res = 0

        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    continue

                if r == 0 or c == 0:
                    res += 1
                else:
                    mat[r][c] += min(mat[r-1][c], mat[r][c-1], mat[r-1][c-1])
                    res += mat[r][c]
        
        return res

"""
Solution 1b: same, but do the sum across the matrix entries separately.
This avoids the "if r == 0 or c == 0" statement.
"""
class Solution1b:
    def countSquares(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        for i in range(1, m):
            for j in range(1, n):
                if mat[i][j] > 0: # ie, == 1
                    mat[i][j] += min(mat[i-1][j], mat[i][j-1], mat[i-1][j-1])
        
        # res = 0
        #
        # for i in range(m):
        #     for j in range(n):
        #         res += mat[i][j]
        # return res

        return sum(map(sum, mat))

"""
Solution 1c: same, but use *= to avoid using "if" statement.

If mat[i][j] is 0, then it remains 0 no matter what.

If mat[i][j] is 1 and min(*) is 0, then mat[i][j] becomes 1.

If mat[i][j] is 1 and min(*) > 0, then mat[i][j] becomes min(*) + 1.

"""
class Solution1c:
    def countSquares(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        for i in range(1, m):
            for j in range(1, n):
                mat[i][j] *= min(mat[i-1][j], mat[i][j-1], mat[i-1][j-1]) + 1

        return sum(map(sum, mat))

###############################################################################
"""
Solution 2: precalc prefix block sums. Then loop over r, c, and k. Use prefix
sums to calculate number of 1s, and check vs k*k. Break early from k loop
when possible.

sum of submatrix of size k at (r,c)

other end at (r+k-1, c+k-1)
r+k-1 < m, ie, k < m - r + 1
c+k-1 < n, ie, k < n - c + 1
k < min(m-r, n-c) + 1

s(r+k-1, c+k-1) - s(r+k-1, c-1) - s(r-1, c+k-1) + s(r-1, c-1)
r-1 >= 0 else...
c-1 >= 0 else...

O(mnk) time, where k = min(m,n)
O(mn) extra space: for matrix of prefix block sums

"""
class Solution2:
    def countSquares(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = mat[0][0]

        for c in range(1, n):
            dp[0][c] = dp[0][c-1] + mat[0][c]

        for r in range(1, m):
            s = 0
            for c in range(n):
                s += mat[r][c]                
                dp[r][c] = dp[r-1][c] + s

        res = dp[-1][-1]

        for r in range(m):
            for c in range(n):
                if mat[r][c] != 1:
                    continue

                end_k = min(m-r, n-c) + 1

                for k in range(2, end_k):
                    r2 = r + k - 1
                    c2 = c + k - 1
                    count = dp[r2][c2]

                    if c > 0:
                        count -= dp[r2][c-1]

                    if r > 0:
                        count -= dp[r-1][c2]
                        if c > 0:
                            count += dp[r-1][c-1]

                    if count == k * k:
                        res += 1
                    else:
                        break

        return res

"""
Solution 2b: same, but use dummy first row and dummy first column for dp matrix.
"""
class Solution2b:
    def countSquares(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        dp = [[0] * (n+1) for _ in range(m+1)]

        for r in range(m):
            s = 0
            for c in range(n):
                s += mat[r][c]                
                dp[r+1][c+1] = dp[r][c+1] + s

        res = dp[-1][-1]
        max_k = int(res**0.5)

        for r in range(m-1):
            for c in range(n-1):
                if mat[r][c] != 1:
                    continue

                end_k = min(m-r, n-c, max_k) + 1

                for k in range(2, end_k):
                    r2 = r + k
                    c2 = c + k

                    if dp[r2][c2] - dp[r2][c] - dp[r][c2] + dp[r][c] == k*k:
                        res += 1
                    else:
                        break

        return res

"""
Solution 2c: same, but loop through k first.
"""
class Solution2c:
    def countSquares(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        dp = [[0] * (n+1) for _ in range(m+1)]

        for r in range(m):
            s = 0
            for c in range(n):
                s += mat[r][c]                
                dp[r+1][c+1] = dp[r][c+1] + s

        res = dp[-1][-1]
        end_k = min(m, n, int(res**0.5)) + 1

        for k in range(2, end_k):
            k2 = k*k
            end_r = m - k + 1
            end_c = n - k + 1
            old_res = res
            
            #for r in range(m-k+1):
            for r in range(end_r):
                #r2 = r + k
                
                dpr2 = dp[r+k]
                dpr = dp[r]
                
                #for c in range(n-k+1):
                for c in range(end_c):
                    #if mat[r][c] != 1:
                    #    continue

                    if dpr2[c+k] - dpr2[c] - dpr[c+k] + dpr[c] == k2:
                        res += 1

            if res == old_res:
                break

        return res

###############################################################################

if __name__ == "__main__":
    def test(mat, comment=None):
        print("="*80)
        if comment:
            print(comment, "\n")

        for row in mat:
            for x in row:
                print(x, end=' ')
            print()
        
        res = sol.countSquares(mat)

        print(f"\nresult: {res}\n")


    sol = Solution() # DP tabulation; O(mn)
    #sol = Solution1b() # same, but do the sum across the matrix entries separately
    #sol = Solution1c() # same, but use *= to avoid using "if" statement

    #sol = Solution2() # use prefix block sums; O(mnk)
    #sol = Solution2b() # same, but use dummy first row/col for dp matrix
    #sol = Solution2c() # same, but loop through k first

    comment = "LC ex1; answer = 15"
    mat = [
        [0,1,1,1],
        [1,1,1,1],
        [0,1,1,1]]    
    test(mat, comment)

    comment = "LC ex2; answer = 7"
    mat = [
        [1,0,1],
        [1,1,0],
        [1,1,0]]
    test(mat, comment)
