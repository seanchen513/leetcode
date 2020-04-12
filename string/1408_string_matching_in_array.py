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

O(n^2) time
O(n) extra space: for output
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
Solution: functional.
"""
class Solution2:
    def stringMatching(self, words: List[str]) -> List[str]:

        f = lambda w: any(w2 != w and w2.find(w) != -1 for w2 in words)
        #return list(filter(f, words))
        return [w for w in words if f(w)]

        #return list(filter(lambda w: any(w2 != w and w2.find(w) != -1 for w2 in words), words))

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

    comment = 'LC ex1; answer = ["as","hero"]'
    arr = ["mass","as","hero","superhero"]
    test(arr, comment)

    comment = 'LC ex2; answer = ["et","code"]'
    arr = ["leetcode","et","code"]
    test(arr, comment)

    comment = 'LC ex3; answer = []'
    arr = ["blue","green","bu"]
    test(arr, comment)
