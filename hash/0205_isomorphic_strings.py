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
Solution 1: use 2 dicts, one to map chars from s to t, and one to map chars
from t to s.

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
class Solution:
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
