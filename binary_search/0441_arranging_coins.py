"""
441. Arranging Coins
Easy

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.

Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
"""

###############################################################################
"""
Solution: use math.

Triangular numbers
1 3 6 10 15 21 28 36 45 55 66 78 91 105 ...

Want largest k such that k(k+1)/2 < n.

k^2 + k < 2n
k^2 + k - 2n < 0

D = 1 + 8n > 0
k = (-1 +/- sqrt(1+8n)) / 2

Take positive root:
k = (sqrt(1+8n) - 1) / 2

Largest k that satisfies inequality is floor((sqrt(1+8n) - 1) / 2).
"""
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((1 + 8*n)**0.5 - 1) // 2 # this works despite "// 2" outside

###############################################################################
"""
Solution: binary search on value space

Triangular numbers
1 3 6 10 15 21 28 36 45 55 66 78 91 105 ...

Want largest k such that k(k+1)/2 < n.

"""
class Solution:
    def arrangeCoins(self, n: int) -> int:
        lo = 1
        hi = n
        m = 2 * n

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if mid * (mid + 1) < m:
                lo = mid + 1
            else:
                hi = mid

        if lo * (lo + 1) == m:
            return lo

        # target value 2*n not found in value space, so lo == hi is
        # the next index. We want the prior index.

        return lo - 1
