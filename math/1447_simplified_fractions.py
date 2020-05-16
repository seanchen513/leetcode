"""
1447. Simplified Fractions
Medium

Given an integer n, return a list of all simplified fractions between 0 and 1 (exclusive) such that the denominator is less-than-or-equal-to n. The fractions can be in any order.

Example 1:

Input: n = 2
Output: ["1/2"]
Explanation: "1/2" is the only unique fraction with a denominator less-than-or-equal-to 2.

Example 2:

Input: n = 3
Output: ["1/2","1/3","2/3"]

Example 3:

Input: n = 4
Output: ["1/2","1/3","1/4","2/3","3/4"]
Explanation: "2/4" is not a simplified fraction because it can be simplified to "1/2".

Example 4:

Input: n = 1
Output: []

Constraints:

1 <= n <= 100
"""

from typing import List
import math

###############################################################################
"""
Solution: check gcd of numerators and denominators. Fraction can't be 
simplified if gcd = 1.

O(n^2 log n) time: since calculating gcd() is O(log n).

"""
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(x, y):
            while y: # (4, 10) -> (10, 4) -> (4, 2) -> (2, 0)
                x, y = y, x % y

            return x

        res = []

        for d in range(2, n+1): # denominator
            for num in range(1, d): # numerator
                if gcd(d, num) == 1:
                #if math.gcd(d, num) == 1:
                    #res.append(str(num) + "/" + str(d))
                    res.append(f"{num}/{d}")

        return res

###############################################################################
"""
Solution 2: use seen set to store decimal version of fraction.

O(n^2) time
O() extra space: for set (not counting output list)
"""
class Solution2:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        seen = set()

        for d in range(2, n+1): # denominator
            for num in range(1, d): # numerator
                x = num / d
                #x = round(num / d, 15)

                if x not in seen:
                    #res.append(str(num) + "/" + str(d))
                    res.append(f"{num}/{d}")
                    
                    seen.add(x)
                    
        return res

###############################################################################

if __name__ == "__main__":
    def test(n, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\nn = {n}")

        res = sol.simplifiedFractions(n)

        print(f"\nres = {res}\n")


    sol = Solution() # use gcd
    sol = Solution2() # use set

    comment = "LC ex1; answer = 1/2"
    n = 2
    test(n, comment)

    comment = "LC ex2; answer = 1/2, 1/3, 2/3"
    n = 3
    test(n, comment)

    comment = "LC ex3; answer = 1/2, 1/3, 1/4, 2/3, 3/4"
    n = 4
    test(n, comment)

    comment = "LC ex4; answer = []"
    n = 1
    test(n, comment)

    comment = "; answer = "
    n = 5
    test(n, comment)

    # ["1/2","1/3","1/4","1/5","1/6","2/3","2/5","3/4","3/5","4/5","5/6"]
    comment = "LC TC; answer = "
    n = 6
    test(n, comment)
