"""
500. Keyboard Row
Easy

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
 
Note:

You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""

from typing import List

###############################################################################
"""
Solution:
"""
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1 = set('qwertyuiop')
        r2 = set('asdfghjkl')
        r3 = set('zxcvbnm')
        # r1 = set('qwertyuiopQWERTYUIOP')
        # r2 = set('asdfghjklASDFGHJKL')
        # r3 = set('zxcvbnmZXCVBNM')
        
        res = []
        
        for w in words:
            for r in (r1, r2, r3):
                if all(ch in r for ch in w.lower()):
                #if all(ch in r for ch in w):
                    res.append(w)
                
        return res

"""
Solution: same idea, but convert each word to set and check using 
subset operator <=.
"""
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1 = set('qwertyuiop')
        r2 = set('asdfghjkl')
        r3 = set('zxcvbnm')
        # r1 = set('qwertyuiopQWERTYUIOP')
        # r2 = set('asdfghjklASDFGHJKL')
        # r3 = set('zxcvbnmZXCVBNM')
        
        res = []
        
        for w in words:
            s = set(w.lower())
            #s = set(w)

            if s <= r1 or s <= r2 or s <= r3:
                res.append(w)
                
        return res
        