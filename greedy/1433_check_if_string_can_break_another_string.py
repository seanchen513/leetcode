"""
1433. Check If a String Can Break Another String
Medium

Given two strings: s1 and s2 with the same size, check if some permutation of string s1 can break some permutation of string s2 or vice-versa (in other words s2 can break s1).

A string x can break string y (both of size n) if x[i] >= y[i] (in alphabetical order) for all i between 0 and n-1.

Example 1:

Input: s1 = "abc", s2 = "xya"
Output: true
Explanation: "ayx" is a permutation of s2="xya" which can break to string "abc" which is a permutation of s1="abc".

Example 2:

Input: s1 = "abe", s2 = "acd"
Output: false 
Explanation: All permutations for s1="abe" are: "abe", "aeb", "bae", "bea", "eab" and "eba" and all permutation for s2="acd" are: "acd", "adc", "cad", "cda", "dac" and "dca". However, there is not any permutation from s1 which can break some permutation from s2 and vice-versa.

Example 3:

Input: s1 = "leetcodee", s2 = "interview"
Output: true

Constraints:

s1.length == n
s2.length == n
1 <= n <= 10^5
All strings consist of lowercase English letters.
"""

import collections
import string

###############################################################################
"""
Solution: use dicts to count chars in each string.

s1[i] <= s2[i] for all i (in lex order)
iff the running difference in counts is always >= 0 (in lex order)

O(n + 26) = O(n) time
O(26) = O(1) extra space: for dicts
"""
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        def check(d1, d2):
            s= 0

            for ch in string.ascii_lowercase:
                s += d1[ch] - d2[ch]
                if s < 0:
                    return False

            return True

        d1 = collections.Counter(s1)
        d2 = collections.Counter(s2)

        return check(d1, d2) or check(d2, d1)

###############################################################################
"""
Solution 2: greedily pair lex smaller chars in each string, and check if there
is a consistent comparison (<= or >=) that can be made across all pairs.

O(n log n) time: for sorting each string, where n = len(s1) = len(s2)
O(n) extra space: for sorted strings

LC ex3:
leetcodee
interview

cdeeeelot
eeiinrtvw

True
"""
class Solution2:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        n = len(s1)
        x1 = sorted(s1)
        x2 = sorted(s2)
        
        if all(x1[i] <= x2[i] for i in range(n)):
            return True
        if all(x2[i] <= x1[i] for i in range(n)):
            return True
            
        return False        

###############################################################################

if __name__ == "__main__":
    def test(s1, s2, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\ns1 = {s1}")
        print(f"s2 = {s2}")

        res = sol.checkIfCanBreak(s1, s2)

        print(f"\nres = {res}\n")


    sol = Solution() # use dicts to count chars
    sol = Solution2() # use sorting

    comment = "LC ex1; answer = True"
    s1 = "abc"
    s2 = "xya"
    test(s1, s2, comment)

    comment = "LC ex2; answer = False"
    s1 = "abe"
    s2 = "acd"
    test(s1, s2, comment)

    comment = "LC ex3; answer = True"
    s1 = "leetcodee"
    s2 = "interview"
    test(s1, s2, comment)
