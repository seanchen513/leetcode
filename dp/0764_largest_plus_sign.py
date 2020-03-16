"""
764. Largest Plus Sign
Medium

In a 2D grid from (0, 0) to (N-1, N-1), every cell contains a 1, except those cells in the given list mines which are 0. What is the largest axis-aligned plus sign of 1s contained in the grid? Return the order of the plus sign. If there is none, return 0.

An "axis-aligned plus sign of 1s of order k" has some center grid[x][y] = 1 along with 4 arms of length k-1 going up, down, left, and right, and made of 1s. This is demonstrated in the diagrams below. Note that there could be 0s or 1s beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1s.

Examples of Axis-Aligned Plus Signs of Order k:

Order 1:
000
010
000

Order 2:
00000
00100
01110
00100
00000

Order 3:
0000000
0001000
0001000
0111110
0001000
0001000
0000000

Example 1:

Input: N = 5, mines = [[4, 2]]
Output: 2
Explanation:
11111
11111
11111
11111
11011
In the above grid, the largest plus sign can only be order 2.  One of them is marked in bold.

Example 2:

Input: N = 2, mines = []
Output: 1
Explanation:
There is no plus sign of order 2, but there is of order 1.

Example 3:

Input: N = 1, mines = [[0, 0]]
Output: 0
Explanation:
There is no plus sign, so return 0.

Note:

N will be an integer in the range [1, 500].
mines will have length at most 5000.
mines[i] will be length 2 and consist of integers in the range [0, N-1].
(Additionally, programs submitted in C, C++, or C# will be judged with a slightly smaller time limit.)
"""

from typing import List

"""
Note: there are solutions that run faster on LeetCode, eg,

https://leetcode.com/problems/largest-plus-sign/discuss/113319/Python-250ms-solution

but seem to have worse worst-case time complexity.
"""

###############################################################################
"""
Solution:

Optimization: use single dp matrix rather than 4 separate direction matrices.
The dp matrix is used to store the running mins for each cell, rather than
calculating the mins across the direction matrices at the end.

To do this, we convert mines to a set of tuples.

O(n^2) time
O(n^2) extra space: for dp matrix.

Based on approach 2 here:
https://leetcode.com/problems/largest-plus-sign/solution/

Runtime: 1856 ms, faster than 90.10% of Python3 online submissions
Memory Usage: 16.7 MB, less than 66.67% of Python3 online submissions

If assign dpi = dp[i] in two of the inner loops:
Runtime: 1752 ms, faster than 94.79% of Python3 online submissions
Memory Usage: 16.7 MB, less than 66.67% of Python3 online submissions
"""
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        mines = {tuple(m) for m in mines}
        dp = [[0]*n for _ in range(n)] # stores size of plus sign for each cell
        res = 0 # max across dp matrix

        for j in range(n):
            count = 0
            for i in range(n):
                count = 0 if (i,j) in mines else count + 1
                dp[i][j] = count

            count = 0
            for i in range(n-1, -1, -1):
                count = 0 if (i,j) in mines else count + 1
                if count < dp[i][j]:
                    dp[i][j] = count

        for i in range(n):
            count = 0
            for j in range(n):
                count = 0 if (i,j) in mines else count + 1
                if count < dp[i][j]:
                    dp[i][j] = count

            count = 0
            for j in range(n-1, -1, -1):
                count = 0 if (i,j) in mines else count + 1
                if count < dp[i][j]:
                    dp[i][j] = count
                if dp[i][j] > res:
                    res = dp[i][j]

        return res

###############################################################################
"""
Solution 2: for each direction, eg left, find left[r][c] = number of 1s you will
see walking left before hitting a 0.  The largest plus sign at (r,c) is the 
max of left[r][c], right[r][c], up[r][c], and down[r][c].

This variation initializes the values in direction amtrices to 1, except
for mines, which are initialized to 0.

O(n^2) time
O(n^2) extra space

Runtime: 2928 ms, faster than 68.23% of Python3 online submissions
Memory Usage: 29.4 MB, less than 50.00% of Python3 online submissions
"""
class Solution2:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        up = [[1]*n for _ in range(n)]
        left = [[1]*n for _ in range(n)]
        down = [[1]*n for _ in range(n)]
        right = [[1]*n for _ in range(n)]

        for i, j in mines:
            up[i][j] = 0
            down[i][j] = 0
            left[i][j] = 0
            right[i][j] = 0

        for j in range(n):
            for i in range(1, n):
                if up[i][j] != 0:
                    up[i][j] = up[i-1][j] + 1

            for i in range(n-2, -1, -1):
                if down[i][j] != 0:
                    down[i][j] = down[i+1][j] + 1

        for i in range(n):
            for j in range(1, n):
                if left[i][j] != 0:
                    left[i][j] = left[i][j-1] + 1

            for j in range(n-2, -1, -1):
                if right[i][j] != 0:
                    right[i][j] = right[i][j+1] + 1

        mx = -1

        for i in range(n):
            for j in range(n):
                mx = max(mx, min(up[i][j], down[i][j], left[i][j], right[i][j]) )

        return mx

"""
Solution 2b: same as sol 2, but optimize by using "count" variable.

Runtime: 2648 ms, faster than 72.92% of Python3 online submissions
Memory Usage: 29.2 MB, less than 50.00% of Python3 online submissions
"""
class Solution2b:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        up = [[1]*n for _ in range(n)]
        left = [[1]*n for _ in range(n)]
        down = [[1]*n for _ in range(n)]
        right = [[1]*n for _ in range(n)]

        for i, j in mines:
            up[i][j] = 0
            down[i][j] = 0
            left[i][j] = 0
            right[i][j] = 0

        for j in range(n):
            count = 0
            for i in range(n):
                count = 0 if up[i][j] == 0 else count + 1
                up[i][j] = count

            count = 0
            for i in range(n-1, -1, -1):
                count = 0 if down[i][j] == 0 else count + 1
                down[i][j] = count

        for i in range(n):
            count = 0
            for j in range(n):
                count = 0 if left[i][j] == 0 else count + 1
                left[i][j] = count

            count = 0
            for j in range(n-1, -1, -1):
                count = 0 if right[i][j] == 0 else count + 1
                right[i][j] = count

        mx = -1

        for i in range(n):
            for j in range(n):
                mx = max(mx, min(up[i][j], down[i][j], left[i][j], right[i][j]) )


        return mx

###############################################################################
"""
Solution 3:

This variation initializes the values of direction matrices to 0, and 
converts the mines list to a set to use for checking.
"""
class Solution3:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        mines = {tuple(m) for m in mines}

        up = [[0]*n for _ in range(n)]
        left = [[0]*n for _ in range(n)]
        down = [[0]*n for _ in range(n)]
        right = [[0]*n for _ in range(n)]

        for j in range(n):
            up[0][j] = 0 if (0, j) in mines else 1
            down[n-1][j] = 0 if (n-1, j) in mines else 1

        for j in range(n):
            for i in range(1, n):
                if (i, j) not in mines:
                    up[i][j] = up[i-1][j] + 1

            for i in range(n-2, -1, -1):
                if (i, j) not in mines:
                    down[i][j] = down[i+1][j] + 1

        for i in range(n):
            left[i][0] = 0 if (i, 0) in mines else 1
            right[i][n-1] = 0 if (i, n-1) in mines else 1

        for i in range(n):
            for j in range(1, n):
                if (i, j) not in mines:
                    left[i][j] = left[i][j-1] + 1

            for j in range(n-2, -1, -1):
                if (i, j) not in mines:
                    right[i][j] = right[i][j+1] + 1

        print("\nup:")
        for row in up:
            print(row)

        print("\ndown:")
        for row in down:
            print(row)

        print("\nleft:")
        for row in left:
            print(row)

        print("\nright:")
        for row in right:
            print(row)

        mx = -1

        for i in range(n):
            for j in range(n):
                mx = max(mx, min(up[i][j], down[i][j], left[i][j], right[i][j]) )

        return mx

###############################################################################
"""
Solution 4: brute force

O(n^3) time
O(len(mines)) extra space

TLE
"""
class Solution4:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        mines = {tuple(m) for m in mines}
        res = 0

        for r in range(n):
            for c in range(n):
                k = 0

                while (k <= r < n-k and k <= c < n-k
                    and (r-k, c) not in mines and (r+k, c) not in mines
                    and (r, c-k) not in mines and (r, c+k) not in mines):
                        k += 1
                
                res = max(res, k)

        return res

###############################################################################

if __name__ == "__main__":
    def test(n, mines, comment=None):
        print("="*80)
        if comment:
            print(comment)
              
        # print()
        # for i in range(n):
        #     for j in range(n):
        #         if [i, j] in mines:
        #             print("0 ", end="")
        #         else:
        #             print("1 ", end="")
        #     print()

        print(f"\nn = {n}")
        print(f"mines = {mines}")

        res = sol.orderOfLargestPlusSign(n, mines)

        print(f"\nres = {res}\n")


    sol = Solution()
    #sol = Solution4() # brute force

    comment = "LC ex1; answer = 2"
    n = 5
    mines = [[4, 2]]
    test(n, mines, comment)

    comment = "LC ex2; answer = 1"
    n = 2
    mines = []
    test(n, mines, comment)

    comment = "LC ex3; answer = 0"
    n = 1
    mines = [[0, 0]]
    test(n, mines, comment)

    comment = "LC test case; answer = 2"
    n = 3
    mines = [[0, 0]]
    test(n, mines, comment)

    comment = "LC test case; answer = 1"
    n = 5
    mines = [[0,1],[0,2],[0,3],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0],[2,1],[2,3],[2,4],[3,1],[3,2],[3,3],[3,4],[4,0],[4,1],[4,2],[4,3],[4,4]]
    test(n, mines, comment)
