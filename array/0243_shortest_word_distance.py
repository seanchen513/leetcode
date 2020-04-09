"""
243. Shortest Word Distance
Easy

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

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

###############################################################################
"""
Solution: keep track of most recent indices word1 and word2 were found at.

O(n) time
O(1) extra space
"""
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        mn = n = len(words)
        i1 = -1 # most recent index for word1
        i2 = -1 # most recent index for word2

        for i in range(n):
            if words[i] == word1:
                i1 = i
            elif words[i] == word2:
                i2 = i

            if i1 != -1 and i2 != -1:
                mn = min(mn, abs(i1 - i2))

        return mn

###############################################################################
"""
Solution: brute force. Find all indices that word1 and word2 are at, then 
find min abs diff between the two lists of indices.
"""
class Solution2:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        n = len(words)
        ind1 = [] # indices where word1 can be found
        ind2 = [] # indices where word2 can be found
        
        for i in range(n):
            if words[i] == word1:
                ind1.append(i)
            elif words[i] == word2:
                ind2.append(i)

        # reuse n as min word distance
        for i in ind1:
            for j in ind2:
                if abs(i-j) < n:
                    n = abs(i-j)
                    if n == 1: return 1

        return n

        #return min(abs(i-j) for i in ind1 for j in ind2)
        