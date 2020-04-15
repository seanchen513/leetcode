"""
1408. String Matching in an Array
Easy

Given an array of string words. Return all strings in words which is substring of another word in any order. 

String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].

Example 1:

Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.

Example 2:

Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".

Example 3:

Input: words = ["blue","green","bu"]
Output: []
 
Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 30
words[i] contains only lowercase English letters.
It's guaranteed that words[i] will be unique.
"""

from typing import List
import collections

###############################################################################
"""
Solution: brute force

O(n^2 * s) time, where n = num strings, and s = max length of any word
O(n * s) extra space: for output
"""
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        
        for i, w in enumerate(words):
            for j, w2 in enumerate(words):
                if i == j:
                    continue
                    
                if w2.find(w) != -1:
                    res.append(w)
                    break
                    
        return res

###############################################################################
"""
Solution 2: functional.
"""
class Solution2:
    def stringMatching(self, words: List[str]) -> List[str]:

        f = lambda w: any(w2 != w and w2.find(w) != -1 for w2 in words)
        #return list(filter(f, words))
        return [w for w in words if f(w)]

        #return list(filter(lambda w: any(w2 != w and w2.find(w) != -1 for w2 in words), words))

###############################################################################
"""
Solution 3: use suffix trie

https://leetcode.com/problems/string-matching-in-an-array/discuss/575147/Clean-Python-3-suffix-trie-O(NlogN-%2B-N-*-S2)

O(n log n + n * s^2) time, where n = num strings, and s = max length of any word

This is better than brute force's O(n^2 s) if n >> s.

O(n * s^2) space: for suffix trie
O(n * s) space: for output
"""
class Solution3:
    def stringMatching(self, words: List[str]) -> List[str]:
        def add(word):
            node = trie
            for c in word:
                #node = node.setdefault(c, {})
                if c not in node:
                    node[c] = {}
                node = node[c]

        def get(word) -> bool:
            node = trie
            for c in word:
                #if (node := node.get(c)) is None:
                if c not in node:
                    return False
                node = node[c]

            return True

        trie = {}
        res = []
        words.sort(key=len, reverse=True)

        for w in words:
            if get(w):
                res.append(w)

            for i in range(len(w)):
                add(w[i:])

        return res

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\narr = {arr}")

        res = sol.stringMatching(arr)

        print(f"\nres = {res}\n")


    sol = Solution()
    #sol = Solution2() # functional
    sol = Solution3() # use suffix trie

    comment = 'LC ex1; answer = ["as","hero"]'
    arr = ["mass","as","hero","superhero"]
    test(arr, comment)

    comment = 'LC ex2; answer = ["et","code"]'
    arr = ["leetcode","et","code"]
    test(arr, comment)

    comment = 'LC ex3; answer = []'
    arr = ["blue","green","bu"]
    test(arr, comment)
