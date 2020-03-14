"""
49. Group Anagrams
Medium

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:
All inputs will be in lowercase.
The order of your output does not matter.
"""

from typing import List
import collections
import math

###############################################################################
"""
Solution #: use dict where keys are tuples that count letters.

O(nk) time, where n = len(strs) and k = max len of any string.
O(nk) extra space: for output

Runtime: 108 ms, faster than 43.73% of Python3 online submissions
Memory Usage: 18.6 MB, less than 11.32% of Python3 online submissions
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        
        for s in strs:
            counter = [0]*26
            for ch in s:
                counter[ord(ch) - 97] += 1 # ord('a') = 97
            
            res[tuple(counter)].append(s)
            
        return res.values()

"""
Solution: use dict where keys are sorted strings.

Note: can use counting sort to get O(nk) time and extra space, but this
is essentially the same as the other solution.

O(nk log k) time, where n = len(strs) and k = max len of any string.
O(nk) extra space: for output

Runtime: 84 ms, faster than 99.77% of Python3 online submissions
Memory Usage: 16.8 MB, less than 41.51% of Python3 online submissions
"""
class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)

        for s in strs:
            #res[str(sorted(s))].append(s) # slower
            res[tuple(sorted(s))].append(s) # faster

        return res.values()

###############################################################################
"""
Solution 3: hash each string by assigning primes to each letter and
multiplying primes together.

O(nk) time, where n = len(strs) and k = max len of any string.
O(nk) extra space: for output

Runtime: 96 ms, faster than 87.21% of Python3 online submissions
Memory Usage: 16.1 MB, less than 54.72% of Python3 online submissions
"""
class Solution3:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        primes = {
            'a': 2, 
            'b': 3, 
            'c': 5, 
            'd': 7, 
            'e': 11, 
            'f': 13,
            'g': 17,
            'h': 19,
            'i': 23,
            'j': 29,
            'k': 31,
            'l': 37,
            'm': 41,
            'n': 43,
            'o': 47,
            'p': 53,
            'q': 59,
            'r': 61,
            's': 67, 
            't': 71,
            'u': 73,
            'v': 79,
            'w': 83,
            'x': 89,
            'y': 97,
            'z': 101
        }
        res = collections.defaultdict(list)

        for s in strs:
            # p = 1
            # for ch in s:
            #     p *= primes[ch]

            p = math.prod(primes[ch] for ch in s)
            res[p].append(s)

        return res.values()

###############################################################################

if __name__ == "__main__":
    def test(strs, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(strs)

        res = sol.groupAnagrams(strs)

        print(f"\nres = {res}\n")


    sol = Solution() # use dict where keys are tuples counting letters
    sol = Solution2() # use dict where keys are sorted strings 
    sol = Solution3() # hash strings by assigning primes to letters and multiplying

    comment = "LC example"
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    test(strs, comment)
