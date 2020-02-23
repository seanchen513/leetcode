"""
1362. Closest Divisors
Medium

Given an integer num, find the closest two integers in absolute difference whose product equals num + 1 or num + 2.

Return the two integers in any order.

Example 1:

Input: num = 8
Output: [3,3]
Explanation: For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 = 10, the closest divisors are 2 & 5, hence 3 & 3 is chosen.

Example 2:

Input: num = 123
Output: [5,25]

Example 3:

Input: num = 999
Output: [40,25]

Constraints:

1 <= num <= 10^9
"""

from typing import List
import collections

###############################################################################
"""
Solution:

O(sqrt(n)) time
O(1) extra space
"""
class Solution:
    def closestDivisors(self, n: int) -> List[int]:
        # trivial cases
        # 1, n+1 : diff = n
        # 1, n+2 : diff = n+1
        min_diff = n
        res = [1, n+1]

        for m in (n+1, n+2):
            end = int(m**0.5) + 1

            for x in range(2, end): # possible divisors
                if m % x == 0:
                    y = m // x # other divisor
                    diff = abs(y - x)
                    
                    if diff < min_diff:
                        min_diff = diff
                        res = [x, y]

        return res

###############################################################################

if __name__ == "__main__":
    def test(n, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(f"n = {n}")

        res = sol.closestDivisors(n)

        print(f"\nres = {res}")


    sol = Solution()

    comment = "LC ex1; answer = [3,3]"
    n = 8
    test(n, comment)

    comment = "LC ex2; answer = [5,25]"
    n = 123 
    test(n, comment)

    comment = "LC ex3; answer = [40,25]"
    n = 999
    test(n, comment)
    
    comment = "LC max input; answer = "
    n = 10**9
    test(n, comment)
