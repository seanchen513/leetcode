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
import math

###############################################################################
"""
Solution 1:

O(sqrt(n)) time
O(1) extra space

Runtime: 256 ms, faster than 100.00% of Python3 online submissions
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions
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
"""
Solution 2: same as sol 1, but more concise.

- Combined into single loop.
- Got rid of tracking minimum difference since loop is in increasing order,
so results with lower absolute difference will override earlier results.
"""
class Solution2:
    def closestDivisors(self, n: int) -> List[int]:
        res = [1, n + 1]

        n1, n2 = n + 1, n + 2
        end = int(n2**0.5) + 1

        for x in range(2, end): # possible divisors
            if n2 % x == 0:
                res = [x, n2 // x]

            if n1 % x == 0:
                res = [x, n1 // x]

        return res

###############################################################################
"""
Solution 3: same as sol 2, but loop in descending order and returns ASAP.

- math.sqrt(n) is faster than n**0.5
- "if not n % x" is faster than "if n % x == 0"

Runtime: 112 ms, faster than 100.00% of Python3 online submissions
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions
"""
class Solution3:
    def closestDivisors(self, n: int) -> List[int]:
        n1, n2 = n + 1, n + 2
        end = int(math.sqrt(n2)) # note: no +1 since we start with this value
        # Using +1 with "end" fails a small test case.

        for x in range(end, 0, -1): # possible divisors
            if not n1 % x: # comes first because of case [1, n+1] vs [1, n+2]
                return [x, n1 // x]

            if not n2 % x:
                return [x, n2 // x]

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
    sol = Solution2() # more concise, single loop
    sol = Solution3() # single loop descending; return ASAP

    comment = "LC ex1; answer = [3,3]"
    n = 8
    test(n, comment)

    comment = "LC ex2; answer = [5,25]"
    n = 123 
    test(n, comment)

    comment = "LC ex3; answer = [40,25]"
    n = 999
    test(n, comment)
    
    comment = "LC max input; answer = [23658, 42269]"
    n = 10**9
    test(n, comment)
