"""
290. Word Pattern
Easy

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false

Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false

Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
"""

###############################################################################
"""
Solution: check that forward and reverse dicts are well-defined (not 1-to-many).
Split string into words using str.split(), and check that number of words
is the same as number of letters in pattern.

O(n) time
O(n) extra space: for dicts, and for words array.
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(words) != len(pattern):
            return False
        
        d = {} # maps letters in pattern to words in str
        d2 = {} # reverse map
        
        for p, w in zip(pattern, words):
            if p in d:
                if d[p] != w:
                    return False
            else:
                d[p] = w
                
            if w in d2:
                if d2[w] != p:
                    return False
            else:
                d2[w] = p
                
        return True
        
###############################################################################
"""
Solution 2: check that forward map is well-defined (not 1-to-many)
and injective (1-to-1, which follows from checking it's not many-to-1).

O(n) time
O(n) extra space: for dict and words array.
"""
class Solution2:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        # Along with injectivity, this ensures that map is surjective.
        if len(words) != len(pattern):
            return False
        
        d = {} # maps letters in pattern to words in str
        
        # Check that map is well-defined (ie, not 1-to-many).
        # This implies len(set(d.keys())) <= len(set(d.values())).

        for p, w in zip(pattern, words):
            if p in d:
                if d[p] != w:
                    return False
            else:
                d[p] = w

        # Check that map is injective.
        
        #if len(set(d.keys())) != len(set(d.values())): # map not injective
        if len(set(pattern)) != len(set(words)):
            return False

        return True

###############################################################################
"""
Solution 3: check that forward map is well-defined (not 1-to-many)
and injective (1-to-1, which follows from checking it's not many-to-1).

Suppose of we have a mapping from letters to words.

Together with injectivity, implies surjectivity:
len(words) == len(pattern)

Checks injectivity:
len(set(pattern)) == len(set(words))

Checks that map is well-defined:
len(set(zip(pattern, words))) == ...

The left expression is the number of unique pattern to word mappings.

O(n) time
O(n) extra space: for words array and sets.
"""
class Solution3:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        # Along with injectivity, this ensures that map is surjective.
        if len(words) != len(pattern):
            return False

        return len(set(pattern)) == len(set(words)) == len(set(zip(pattern, words)))

###############################################################################

if __name__ == "__main__":
    def test(pat, s, comment=None):       
        print("="*80)
        if comment:
            print(comment)

        print(f"\npat = {pat}")
        print(f"s = {s}")
        
        res = sol.wordPattern(pat, s)

        print(f"\nresult = {res}\n")


    sol = Solution()
  
    comment = "LC ex1; answer = True"
    pat = "abba"
    s = "dog cat cat dog"
    test(pat, s, comment)

    comment = "LC ex2; answer = False"
    pat = "abba"
    s = "dog cat cat fish"
    test(pat, s, comment)
     
    comment = "LC ex3; answer = False"
    pat = "aaaa"
    s = "dog cat cat dog"
    test(pat, s, comment)
     
    comment = "LC ex4; answer = False"
    pat = "abba"
    s = "dog dog dog dog"
    test(pat, s, comment)
     
    comment = "LC TC; answer = False"
    pat = "abba"
    s = "dog dog dog dog"
    test(pat, s, comment)

    comment = "LC TC; answer = False"
    pat = "aaa"
    s = "aa aa aa aa"
    test(pat, s, comment)
    