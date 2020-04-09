"""
244. Shortest Word Distance II
Medium

Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters. 

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3

Input: word1 = "makes", word2 = "coding"
Output: 1

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""

from typing import List
import collections

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)

###############################################################################
"""
Solution: precalculate a dict that map each word to a list of indices that 
the word can be found at.

For shortest(), use two pointers to track indices for word1 and word2.
In each iteration, increment the smaller pointer.

O(n) time for __init__, where n = len(words)

O(cnt1 + cnt2) = O(n) time, where cnt1 and cnt2 are the number of times 
word1 and word2 appear in "words". Note O(cnt1) = O(cnt2) = O(n).

O(n) extra space: for dict

Runtime: 92 ms, faster than 94.36% of Python3 online submissions
Memory Usage: 21.3 MB, less than 50.00% of Python3 online submissions
"""
class WordDistance:
    def __init__(self, words: List[str]):
        self.d = collections.defaultdict(list)
        
        for i, w in enumerate(words):
            self.d[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        ind1 = self.d[word1] # indices in "word" where word1 can be found
        ind2 = self.d[word2] # indices in "word" where word2 can be found
        min_dist = float('inf') # min distance b/w word1 and word2

        i1 = 0 # index for ind1
        i2 = 0 # index for ind2

        while i1 < len(ind1) and i2 < len(ind2):
            k1 = ind1[i1] # index in "words"
            k2 = ind2[i2]

            min_dist = min(min_dist, abs(k1 - k2))

            if k1 < k2:
                i1 += 1
            else:
                i2 += 1
                
        return min_dist

###############################################################################
"""
Solution: precalculate a dict that map each word to a list of indices that 
the word can be found at.

For shortest(), use brute force to find min distance b/w word1 and word2.

O(n) time for __init__, where n = len(words)

O(cnt1 * cnt2) = O(n^2) time, where cnt1 and cnt2 are the number of times 
word1 and word2 appear in "words". Note O(cnt1) = O(cnt2) = O(n).

O(n) extra space: for dict

Runtime: 96 ms, faster than 85.11% of Python3 online submissions
Memory Usage: 21.5 MB, less than 50.00% of Python3 online submissions
"""
class WordDistance:
    def __init__(self, words: List[str]):
        self.d = collections.defaultdict(list)
        
        for i, w in enumerate(words):
            self.d[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        l1 = self.d[word1]
        l2 = self.d[word2]
        mn = float('inf')
        
        for i in l1:
            for j in l2:
                if abs(i-j) < mn:
                    mn = abs(i-j)
                if mn == 1: 
                    return 1
                
        return mn
        
        #return min(abs(i-j) for i in l1 for j in l2)
