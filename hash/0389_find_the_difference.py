"""
389. Find the Difference
Easy

Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
"""

import collections

###############################################################################
"""
Solution: use dict that counts chars in "s".

O(n) time
O(1) extra space
"""
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = collections.defaultdict(int)
        for c in s:
            d[c] += 1

        for c in t:
            if d[c] == 0:
                return c
            d[c] -= 1

###############################################################################
"""
Solution 2: use xor.

O(n) time
O(1) extra space
"""
import functools
class Solution2:
    def findTheDifference(self, s: str, t: str) -> str:
        x = 0
        for c in s:
            x ^= ord(c)
        for c in t:
            x ^= ord(c)
        return chr(x)

###############################################################################
"""
Solution 3: use sorting

O(n log n) time
O(n) extra space
"""
class Solution3:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)

        for c1, c2 in zip(s, t):
            if c1 != c2:
                return c2

        return t[-1]

###############################################################################

if __name__ == "__main__":
    def test(s, t, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print("s = {s}")
        print("t = {t}")
        
        res = sol.findTheDifference(s, t)

        print(f"\nres = {res}\n")


    sol = Solution() # use dict that counts chars in "s"
    sol = Solution2() # use xor
    sol = Solution3() # use sorting

    comment = "LC ex1; answer = 3"
    s = "abcd"
    t = "abcde"
    test(s, t, comment)
