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

import collections
import itertools

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

Runtime: 44 ms, faster than 97.35% of Python3 online submissions
Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions
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

Runtime: 40 ms, faster than 98.63% of Python3 online submissions
Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions
"""
class Solution1b:
    def numOfWays(self, n: int) -> int:
        c, c2 = 12, 6
        mod = 10**9 + 7

        for _ in range(1, n):
            c, c2 = (4*c + c2) % mod, (2*c + c2) % mod

        return c % mod

###############################################################################
"""
Solution 2: DP tabulation. Count each possible combination of colors explicitly.

dp[row n][coloring] = number of ways to color grid up to row n so that 
row n has given coloring.

Precalculate the possible colorings for a row given the coloring of the 
previous row. This is a symmetric relation.

Runtime: 600 ms, faster than 26.10% of Python3 online submissions
Memory Usage: 18.7 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
    def numOfWays(self, n: int) -> int:
        colors = [1, 2, 3]
        m = 3 # number of cells per row of grid
        mod = 10**9 + 7

        """ Create list of all possible colorings of a row of size m. """
        combos = []
        for p in itertools.product(colors, repeat=m):
            if all(x != y for x, y in zip(p, p[1:])):
            #if all(p[i] != p[i-1] for i in range(1, m)):
                combos.append(p)

        """
        Precalculate possible colorings for a row given the coloring
        of the previous row. This is a symmetric relation.
        """
        poss = collections.defaultdict(set)
        for p0 in combos:
            # for p in combos:
            #     if all(p[i] != p0[i] for i in range(m)):
            #         poss[p].add(p0)

            #poss[p0] = {p for p in combos if all(p[i] != p0[i] for i in range(m))}
            poss[p0] = {p for p in combos if all(x != x0 for x, x0 in zip(p, p0))}

        """ Row index starts at 0. """
        dp = [{p: 0 for p in combos} for _ in range(n)]
        dp[0] = {p: 1 for p in combos}

        # for row in range(1, n):
        #     for p0, cnt in dp[row-1].items():
        #         for p in poss[p0]:
        #             dp[row][p] += cnt % mod

        for row in range(1, n):
            dp0 = dp[row-1]

            for p in combos:
                dp[row][p] = sum(dp0[p0] for p0 in poss[p]) % mod

        return sum(dp[-1].values()) % mod

"""
Solution 2b: same, but only keep track of previous and current row.

Runtime: 628 ms, faster than 25.91% of Python3 online submissions
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions

If use this expression: dp[p] = sum(dp0[p0] for p0 in poss[p]) % mod
Runtime: 544 ms, faster than 26.40% of Python3 online submissions
Memory Usage: 14 MB, less than 100.00% of Python3 online submissions
"""
class Solution2b:
    def numOfWays(self, n: int) -> int:
        colors = [1, 2, 3]
        m = 3 # number of cells per row of grid
        mod = 10**9 + 7

        """ Create list of all possible colorings of a row of size m. """
        combos = []
        for p in itertools.product(colors, repeat=m):
            if all(x != y for x, y in zip(p, p[1:])):
            #if all(p[i] != p[i-1] for i in range(1, m)):
                combos.append(p)

        """
        Precalculate possible colorings for a row given the coloring
        of the previous row. This is a symmetric relation.
        """
        poss = collections.defaultdict(set)
        for p0 in combos:
            # for p in combos:
            #     if all(p[i] != p0[i] for i in range(m)):
            #         poss[p].add(p0)

            #poss[p0] = {p for p in combos if all(p[i] != p0[i] for i in range(m))}
            poss[p0] = {p for p in combos if all(x != x0 for x, x0 in zip(p, p0))}

        """ Counts for first row. """
        dp = {p: 1 for p in combos}

        # for _ in range(1, n):
        #     dp0 = dp

        #     # dp.collections.Counter() # SLOW
        #     # dp = collections.defaultdict(int) # a bit slow
        #     dp = {p: 0 for p in combos} # fastest

        #     for p0, cnt in dp0.items():
        #         for p in poss[p0]:
        #             dp[p] += cnt % mod

        for _ in range(1, n):
            dp0 = dp
            dp = {}
        
            for p in combos:
                #dp[p] = sum(dp0[p0] % mod for p0 in poss[p]) % mod
                dp[p] = sum(dp0[p0] for p0 in poss[p]) % mod # faster

        return sum(dp.values()) % mod

"""
Solution 2c: don't precalculate to see how much slower it is.

Runtime: 5164 ms, faster than 5.99% of Python3 online submissions
Memory Usage: 19.3 MB, less than 100.00% of Python3 online submissions
"""
class Solution2c:
    def numOfWays(self, n: int) -> int:
        colors = [1, 2, 3]
        m = 3 # number of cells per row of grid
        mod = 10**9 + 7

        """ Create list of all possible colorings of a row of size m. """
        combos = []
        for p in itertools.product(colors, repeat=m):
            if all(x != y for x, y in zip(p, p[1:])):
            #if all(p[i] != p[i-1] for i in range(1, m)):
                combos.append(p)

        """ Row index starts at 0. """
        dp = [{p: 0 for p in combos} for _ in range(n)]
        dp[0] = {p: 1 for p in combos}

        for row in range(1, n):
            for p0, cnt in dp[row-1].items():
                for p in combos:
                    #if all(p[col] != p0[col] for col in range(m)):
                    if all(x != x0 for x, x0 in zip(p, p0)):
                        dp[row][p] += cnt % mod

        return sum(dp[-1].values()) % mod

###############################################################################
"""
Solution 3: use matrix exponentiation.

O(log n) time
O() extra space

###

c2 = 3 2 * c2
c3   2 2   c3

c(i+1) = A * c(i)
c(i+2) = A^2 c(i)

c(1) = (6, 6)
c(2) = A * c(1)
c(3) = A^2 * c(1)
c(5) = A^4 * c(1)
c(9) = A^8 * c(1)

A = [[a,b], [c,d]]
A^2 =  [[aa+bc, b(a+d)], [c(a+d), bc+dd]]

17 = 16 + 1 = 0b1_0001
17->16: A
16->8: A + A^2
8: A^4
4: A^8
2: A16

*** Passes on LC, but locally doesn't give the correct answer for:
n = 5000
answer = 30228214

Runtime: 80 ms, faster than 73.60% of Python3 online submissions
Memory Usage: 29.3 MB, less than 100.00% of Python3 online submissions
"""
class Solution3:
    def numOfWays(self, n: int) -> int:
        import numpy as np
       
        A = np.matrix([[3,2], [2,2]])
        res = [6, 6]
        
        n -= 1
        mod = 10**9 + 7

        while n:
            if n & 1:
                res = (res * A) % mod

            A = (A * A) % mod
            n //= 2

        return np.sum(res) % mod

"""
Solution 3b: use np.linalg.matrix_power().

Overflows since we don't take intermediate modulos.

*** Does not give the correct answer for:
n = 5000
answer = 30228214
"""
class Solution3b:
    def numOfWays(self, n: int) -> int:
        import numpy as np
        from numpy.linalg import matrix_power

        res = [6, 6]
        
        #A = np.matrix([[3,2], [2,2]])
        A = np.matrix('3 2; 2 2')

        A = matrix_power(A, n-1)

        #return np.sum(np.matmul(A, res)) % (10**9 + 7)
        #return np.sum(np.matmul(res, A)) % (10**9 + 7)
        return np.sum(res @ A) % (10**9 + 7)

"""
Solution 3c:

*** doesn't give correct answer for n = 7...
*** NEED TO FIX

"""
class Solution3c:
    def numOfWays(self, n: int) -> int:
        def sq(a, b, c, d):
            return a*a+b*c, b*(a+d), c*(a+d), b*c+d*d

        #def power(n, a, b, c, d):
        def power(n):
            if n == 1:
                return a, b, c, d

            if n % 2 == 1: #if n & 1:
                #x, y, z, w = power(n-1, a, b, c, d)
                x, y, z, w = power(n-1)
                return a + x, b + y, c + z, d + w

            #x, y, z, w = power(n//2, a, b, c, d)
            x, y, z, w = power(n//2)

            return sq(x, y, z, w)
            #return x*x+y*z, y*(x+w), z*(x+w), y*z+w*w

        c2, c3 = 6, 6

        if n == 1:
            return c2 + c3

        a, b, c, d = 3, 2, 2, 2

        #a, b, c, d = power(n-1, 3, 2, 2, 2)
        a, b, c, d = power(n-1)

        c2, c3 = a * c2 + b * c3, c * c2 + d * c3

        return (c2 + c3) % (10**9 + 7)

###############################################################################

if __name__ == "__main__":
    def test(n, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\nn = {n}")

        res = sol.numOfWays(n)

        print(f"\nres = {res}\n")


    sol = Solution() # count w/ c2 and c3
    sol = Solution1b() # count w/ c and c2

    sol = Solution2() # DP tabulation; enumerate and count 
    #sol = Solution2b() # same, but track only previous and current row
    #sol = Solution2c() # same, but don't precalculate compatible colorings

    #sol = Solution3() # matrix exponentiation w/ mod
    #sol = Solution3b() # use np.linalg.matrix_power(); overflows
    #sol = Solution3c() # 

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
    