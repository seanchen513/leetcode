"""
1347. Minimum Number of Steps to Make Two Strings Anagram
Medium

Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

Example 1:

Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

Example 2:

Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.

Example 3:

Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams. 

Example 4:

Input: s = "xxyyzz", t = "xxyyzz"
Output: 0

Example 5:

Input: s = "friend", t = "family"
Output: 4
 
Constraints:

1 <= s.length <= 50000
s.length == t.length
s and t contain lower-case English letters only.
"""

from typing import List
import collections

###############################################################################

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d = collections.defaultdict(int)

        for ch in t:
            d[ch] += 1

        for ch in s:
            if ch in d and d[ch] != 0:
                d[ch] -= 1

        return sum(d.values())

###############################################################################

if __name__ == "__main__":
    def test(s, t, comment):
        res = sol.minSteps(s, t)

        print("="*80)
        if comment:
            print(comment)

        print(f"\n{s}, {t}")
        print(f"\nresult = {res}")


    sol = Solution()

    comment = "LC ex1; answer = 1"
    s = "bab"
    t = "aba"
    test(s, t, comment)

    comment = "LC ex2; answer = 5"
    s = "leetcode"
    t = "practice"
    test(s, t, comment)

    comment = "LC ex3; answer = 0"
    s = "anagram"
    t = "mangaar"
    test(s, t, comment)

    comment = "LC ex4; answer = 0"
    s = "xxyyzz"
    t = "xxyyzz"
    test(s, t, comment)

    comment = "LC ex5; answer = 4"
    s = "friend"
    t = "family"
    test(s, t, comment)
