"""
269. Alien Dictionary
Hard

There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"

Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"

Example 3:

Input:
[
  "z",
  "x",
  "z"
] 

Output: "" 

Explanation: The order is invalid, so return "".

Note:

You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
"""

from typing import List
import collections

###############################################################################
"""
Solution: BFS using deque; front to end; track back links instead of in-degrees.

LeetCode Feb 10, 2020:
Runtime: 24 ms, faster than 97.48% of Python3 online submissions
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        ### Build graph.
        #letters = set([ch for w in words for ch in w])
        letters = set("".join(words))
        graph = {ch: set() for ch in letters}
        back = collections.defaultdict(set)

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            min_len = min(len(w1), len(w2))

            # Add edges b/w the first pair of different letters only!
            for j in range(min_len):
                if w1[j] != w2[j]:
                    graph[w1[j]].add( w2[j] )
                    back[w2[j]].add( w1[j] )
                    break

        ### Attempt topological sort.
        q = collections.deque([i for i in graph if not back[i]])
        res = []

        while q:
            node = q.popleft()
            res.append(node)

            for nbr in graph[node]:
                back[nbr].remove(node)

                if not back[nbr]:
                    q.append(nbr)

            back.pop(node) # back[node] is empty set

        #print(f"back = {back}")
        ## back is nonempty if graph has a cycle      
        return "" if back else "".join(res) 

###############################################################################

if __name__ == "__main__":
    def test(words, comment=None):
        print("="*80)
        if comment:
            print(comment)

        res = s.alienOrder(words)

        print(f"\n{words}")

        print(f"\nresult = {res}")


    s = Solution()

    comment = "LC ex; answer = wertf"
    words = ["wrt","wrf","er","ett","rftt"]
    test(words, comment)

    comment = "LC ex; answer = zx"
    words = ["z","x"]
    test(words, comment)

    comment = "LC ex; answer = (blank string)"
    words = ["z", "x", "z"]
    test(words, comment)

    comment = "LC test case; answer = z"
    words = ["z", "z"]
    test(words, comment)

    comment = "LC test case; answer = (b before d, eg, abcd)"
    words = ["ab", "adc"]
    test(words, comment)

    comment = "LC test case; answer = (z < c, and a < b; eg, abzc)"
    words = ["za", "zb", "ca", "cb"]
    test(words, comment)
