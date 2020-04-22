"""
205. Isomorphic Strings
Easy

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true

Note:
You may assume both s and t have the same length.
"""

from typing import List

###############################################################################
"""
Solution 1: check that forward and reverse maps are well-defined (same letter
never maps to different letters).

O(n) time, where n is length of each string
O(n) extra space: for dicts
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ds = {}
        dt = {}
        
        for i, ch in enumerate(s):
            if ch in ds:
                if ds[ch] != t[i]: # same char in s cannot map to two diff chars in t
                    return False
            else:
                ds[ch] = t[i]

            if t[i] in dt:
                if dt[t[i]] != ch: # two diff chars in s cannot map to same char in t
                    return False
            else:
                dt[t[i]] = ch

        return True

"""
Solution: rewrite
"""
class Solution1b:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ds = {}
        dt = {}
        
        for a, b in zip(s, t): # corresponding letters in s and t
            # same char in s cannot map to two diff chars in t
            if a in ds and ds[a] != b:
                return False

            # two diff chars in s cannot map to same char in t
            if b in dt and dt[b] != a: 
                return False

            ds[a] = b
            dt[b] = a

        return True

###############################################################################
"""
Solution 3: check that map is well-defined, and that domain and range have
same size.
"""
class Solution2:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}

        for ch, ch2 in zip(s, t):
            if ch in d:
                if d[ch] != ch2:
                    return False
            else:
                d[ch] = ch2

        return len(set(s)) == len(set(t))

###############################################################################
"""
Solution 3: check that domain and range have same size, and that size is
also equal to the number of unique ordered tuples formed by s and t.
"""
class Solution3:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))
