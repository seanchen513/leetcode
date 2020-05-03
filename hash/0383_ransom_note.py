"""
383. Ransom Note
Easy

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""

import string
import collections

###############################################################################
"""
Solution: 

O(m+n) time, where m = len(ransomNote), n = len(magazine)
O(n) extra space: for dict for magazine
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = collections.Counter(magazine)
        
        for ch in ransomNote:
            if d[ch] <= 0: # no more ch's from magazine to select
                return False
            
            d[ch] -= 1
            
        return True

###############################################################################
"""
Solution: use 2 Counter()'s and subtract, which keeps only positive counts.

O(m+n) time
O(m+n) extra space
"""
class Solution2:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
        
###############################################################################
"""
Solution: use string.count().

SLOW

O(mn) time
"""
class Solution3:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return all(ransomNote.count(ch) <= magazine.count(ch) for ch in ransomNote)

"""
Same but loop over set(ransomNote).

O(26*(m+n)) time
O(m) extra space: for set
"""
class Solution3b:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s = set(ransomNote)
        return all(ransomNote.count(ch) <= magazine.count(ch) for ch in s)

"""
Same but loop over string.ascii_lowercase.

FAST

O(26*(m+n)) time
"""
class Solution3c:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return all(ransomNote.count(ch) <= magazine.count(ch) for ch in string.ascii_lowercase)

"""
Same but loop over string of all lowercase letters.

O(26*(m+n)) time
"""
class Solution3d:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        return all(ransomNote.count(ch) <= magazine.count(ch) for ch in letters)
