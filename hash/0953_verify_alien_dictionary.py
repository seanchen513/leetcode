"""
953. Verifying an Alien Dictionary
Easy

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info). 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""

from typing import List

###############################################################################
"""
Solution 1: use dict that maps each char in alien alphabet to its order/index.
Compare consecutive words by finding first difference. If found, use
dict to compare order of letters in alien alphabet. If no difference found,
then one word is a substring of the other word; compare lengths of the words.

O(sum of lengths of all words) time
O(n) = O(1) extra space, where n = size of alien alphabet.
"""
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {ch: i for i, ch in enumerate(order)}

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            end = min(len(w1), len(w2))
            for j in range(end):
                if w1[j] != w2[j]: # first difference
                    if d[w1[j]] > d[w2[j]]: # check order of letters in alien alphabet
                        return False
                    break # break out of inner "for" loop
            else:
                # If we didn't find a difference, then the words are like
                # "apple" and "app".
                if len(w1) > len(w2):
                    return False

        return True

"""
Solution 1b: rewrite using zip().
"""
class Solution1b:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {ch: i for i, ch in enumerate(order)}

        for w1, w2 in zip(words, words[1:]):

            for a1, a2 in zip(w1, w2): # corresponding letters in each word
                if a1 != a2: # first difference
                    if d[a1] > d[a2]: # check order of letters in alien alphabet
                        return False
                
                    break # break out of inner "for" loop
        
            else:
                # If we didn't find a difference, then the words are like
                # "apple" and "app".
                if len(w1) > len(w2):
                    return False

        return True

###############################################################################
"""
Solution 2: use dict that maps each char in alien alphabet to its order/index.
Use this dict to compare consecutive words char-by-char.

Essentially the same as sol 1.

O(sum of lengths of all words) time
O(n) = O(1) extra space, where n = size of alien alphabet.
"""
class Solution2:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {ch: i for i, ch in enumerate(order)}

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            j = 0
            while j < len(w1) and j < len(w2):
                k1 = d[w1[j]]
                k2 = d[w2[j]]

                if k1 > k2:
                    return False
                elif k1 < k2:
                    break
                j += 1

            if len(w1) > len(w2) and w2 == w1[:len(w2)]:
                return False

        return True

"""
Solution 2b: rewrite using zip().
"""
class Solution2b:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {ch: i for i, ch in enumerate(order)}

        for w1, w2 in zip(words, words[1:]):
            for a1, a2 in zip(w1, w2): # corresponding letters in each word
                k1 = d[a1]
                k2 = d[a2]

                if k1 > k2:
                    return False
                elif k1 < k2:
                    break

            if len(w1) > len(w2) and w2 == w1[:len(w2)]:
                return False

        return True

###############################################################################
"""
Solution 3: use dict that maps each char in alien alphabet to its order/index.
Transform each word to a list by mapping each letter using dict.

https://leetcode.com/problems/verifying-an-alien-dictionary/discuss/203185/JavaC%2B%2BPython-Mapping-to-Normal-Order

"""
class Solution3:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {ch: i for i, ch in enumerate(order)}

        # transform each word to a list by mapping each letter using d
        words = [[d[ch] for ch in w] for w in words]

        return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))

###############################################################################
"""
Solution 4: sort words with key fn that transforms each word by mapping 
letters using "order" and list.index().

https://leetcode.com/problems/verifying-an-alien-dictionary/discuss/203185/JavaC%2B%2BPython-Mapping-to-Normal-Order

"""
class Solution4:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        return words == sorted(words, key=lambda w: list(map(order.index, w)))
