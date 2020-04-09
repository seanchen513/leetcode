"""
914. X of a Kind in a Deck of Cards
Easy

In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.
 
Example 1:

Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].

Example 2:

Input: deck = [1,1,1,2,2,2,3,3]
Output: false´
Explanation: No possible partition.

Example 3:

Input: deck = [1]
Output: false
Explanation: No possible partition.

Example 4:

Input: deck = [1,1]
Output: true
Explanation: Possible partition [1,1].

Example 5:

Input: deck = [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2].
 
Constraints:

1 <= deck.length <= 10^4
0 <= deck[i] < 10^4
"""

from typing import List
import collections
import itertools
import functools

###############################################################################
"""
Solution: count deck, then calculate gcd of the counts. If gcd ever reaches
1, return False.

O() time
O(n) extra space: for dict to count with

Runtime: 132 ms, faster than 96.69% of Python3 online submissions
Memory Usage: 14 MB, less than 11.11% of Python3 online submissions
"""
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(x, y):
            while y: # 4, 10 -> 10, 4 -> 4, 2 -> 2, 0
                x, y = y, x % y

            return x

        d = collections.Counter(deck)
        g = d[deck[0]]

        for cnt in d.values():
            g = gcd(g, cnt)
            if g == 1:
                return False

        return True

"""
Solution 1b: same idea, but use fractions.gcd() and reduce().
"""
class Solution1b:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        #from fractions import gcd
        from math import gcd

        return functools.reduce(gcd, collections.Counter(deck).values()) > 1

###############################################################################
"""
Solution: brute force. Count deck, then try group sizes from 2 to n.

O() time
O(n) extra space: for dict to count with
"""
class Solution2:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        d = collections.Counter(deck)

        if any(cnt == 1 for cnt in d.values()):
            return False

        if all(cnt % 2 == 0 for cnt in d.values()):
            return True

        for sz in range(3, len(deck) + 1, 2):
            if all(cnt % sz == 0 for cnt in d.values()):
                return True

        return False

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\narr = {arr}")

        res = sol.hasGroupsSizeX(arr)

        print(f"\nres = {res}\n")


    sol = Solution() # count deck, then check gcd of counts
    sol = Solution1b() # same, but use fractions.gcd() and reduce()

    #sol = Solution2() # brute force; count deck, then try group sizes from 2 to n

    comment = "LC ex1; answer = True"
    arr = [1,2,3,4,4,3,2,1]
    test(arr, comment)

    comment = "LC ex2; answer = False"
    arr = [1,1,1,2,2,2,3,3]
    test(arr, comment)

    comment = "LC ex3; answer = False"
    arr = [1]
    test(arr, comment)

    comment = "LC ex4; answer = True"
    arr = [1,1]
    test(arr, comment)

    comment = "LC TC; answer = True"
    arr = [1,1,2,2,2,2]
    test(arr, comment)

    comment = "LC TC; answer = True"
    arr =[1,1,1,1,2,2,2,2,2,2]
    test(arr, comment)
 