"""
1411. Number of Ways to Paint N × 3 Grid
Hard

You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colours: Red, Yellow or Green while making sure that no two adjacent cells have the same colour (i.e no two cells that share vertical or horizontal sides have the same colour).

You are given n the number of rows of the grid.

Return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 10^9 + 7.

Example 1:

Input: n = 1
Output: 12
Explanation: There are 12 possible way to paint the grid as shown:

Example 2:

Input: n = 2
Output: 54

Example 3:

Input: n = 3
Output: 246

Example 4:

Input: n = 7
Output: 106494

Example 5:

Input: n = 5000
Output: 30228214
 
Constraints:

n == grid.length
grid[i].length == 3
1 <= n <= 5000
"""

###############################################################################
"""
Solution: tabulation using 2 vars: the number of ways to paint the current
row with 2 colors, and same for 3 colors.

O(n) time
O(1) extra space

Each row uses 2 or 3 diff colors.

Start with 2 colors ABA, and use 2 colors for new row: 3 ways (2 to 2)
ABA orig
BAB
BCB
CAC

Start with 2 colors ABA, and use 3 colors for new row: 2 ways (2 to 3)
ABA orig
BAC
CAB

//

Start with 3 colors ABC, and use 2 colors for new row: 2 ways (3 to 2)
ABC orig
BAB 
BCB

Start with 3 colors ABC, and use 3 colors for new row: 2 ways (3 to 3)
ABC orig
BCA
CAB
These are the cyclic permutations of ABC.

Summary (num colors from old row to new row):
2 to 2: 3
2 to 3: 2
3 to 2: 2
3 to 3: 2

two(n+1) = 3*two(n) + 2*three(n)
three(n+1) = 2*two(n) + 2*three(n)

First row: 12 ways
2 colors: 6
3 colors: 6

"""
class Solution:
    def numOfWays(self, n: int) -> int:
        c2, c3 = 6, 6

        #for _ in range(2, n+1):
        for _ in range(1, n):
            c2, c3 = 3*c2 + 2*c3, 2*(c2 + c3)

        return (c2 + c3) % (10**9 + 7)

"""
Solution 1b: same, but simplify the recurrence relationsh a bit.

Let c = c2 + c3 be total number of ways to paint a given row.
c = c2 + c3 = 5*c2 + 4*c3 = 4*c + c2

c2 = 3*c2 + 2*c3 = 2*c + c2

c = 4*c + c2
c2 = 2*c + c2
"""
class Solution1b:
    def numOfWays(self, n: int) -> int:
        c, c2 = 12, 6

        #for _ in range(2, n+1):
        for _ in range(1, n):
            c, c2 = 4*c + c2, 2*c + c2

        return c % (10**9 + 7)

###############################################################################

if __name__ == "__main__":
    def test(n, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\nn = {n}")

        res = sol.numOfWays(n)

        print(f"\nres = {res}\n")


    sol = Solution()
    sol = Solution1b()

    comment = "LC ex1; answer = 12"
    n = 1
    test(n, comment)

    comment = "LC ex2; answer = 54"
    n = 2
    test(n, comment)

    comment = "LC ex3; answer = 246"
    n = 3
    test(n, comment)

    comment = "LC ex4; answer = 106494"
    n = 7
    test(n, comment)
    
    comment = "LC ex5; answer = 30228214"
    n = 5000
    test(n, comment)
    