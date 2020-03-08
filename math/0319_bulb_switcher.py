"""
319. Bulb Switcher
Medium

There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the i-th round, you toggle every i bulb. For the n-th round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

Example:

Input: 3
Output: 1 
Explanation: 
At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off]. 

So you should return 1, because there is only one bulb is on.
"""

"""
Example: n = 6

1: all on
2: odds on: 1, 3, 5
3: flip 3 and 6; on: 1, 5, 6
4: flip 4; on: 1, 4, 5, 6
5: flip 5; on: 1, 4, 6
6: flip 6; on: 1, 4

divisors
1: 1
2: 1, 2
3: 1, 3
4: 1, 2, 4
5: 1, 5
6: 1, 2, 3, 6
"""

"""
Example: n = 12

divisors:
...
7: 1, 7 (even)
8: 1, 2, 4, 8 (even)
9: 1, 3, 9 (odd)
10: 1, 2, 5, 10 (even)
11: 1, 11 (even)
12: 1, 2, 3, 4, 6, 12 (even)

odd number of divisors: 1, 4, 9
"""

import math

###############################################################################
"""
Solution 1: use math.

The light bulbs that are on at the end are the ones that are flipped an
odd number of times.  This is the same as the integer having an odd number
of divisors, which is the same as being a (perfect) square.

So bulbs 1, 4, 9, 16, ... (up to n) are on at the end.  The count of these
is the same as floor(sqrt(n)).
"""
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))

###############################################################################
"""
Solution 2: brute force.

TLE
"""
class Solution2:
    def bulbSwitch(self, n: int) -> int:
        status = [0] * (n+1)

        for i in range(1, n+1):
            for j in range(i, n+1, i):
                status[j] = 1 - status[j]

        return sum(status)

###############################################################################

if __name__ == "__main__":
    def test(n, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\nn = {n}")
        
        res = sol.bulbSwitch(n)

        print(f"\nres = {res}")


    sol = Solution()

    comment = "LC example; answer = 1"
    n = 3
    test(n, comment)
    