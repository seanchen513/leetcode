"""
451. Sort Characters By Frequency
Medium

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""

import collections

###############################################################################
"""
Solution: use dict to count chars, sort keys, and use to build output string.

O(n + k log k) time overall, where k is size of alphabet (number of keys)
- O(n) time for counting chars for dict, and for building output string
- O(k log k) time for sorting keys

O(n) extra space for output string
O(52) extra space for dict and "keys"
"""
class Solution:
    def frequencySort(self, s: str) -> str:
        d = collections.Counter(s)        
        keys = sorted(d, key=lambda x: d[x], reverse=True)
        
#         res = []
#         for k in keys:
#             res.append(k * d[k])
#         return ''.join(res)
    
        return ''.join([k * d[k] for k in keys])

###############################################################################
"""
Solution 2: same as sol 1, but use bucket sort.

O(n) time
O(n) extra space
"""
class Solution2:
    def frequencySort(self, s: str) -> str:
        if not s:
            return ""

        # count chars
        d = collections.Counter(s)
        max_freq = max(d.values())

        # bucket sort
        buckets = [[] for _ in range(max_freq + 1)]
        for ch, cnt in d.items():
            buckets[cnt].append(ch)

        # build output string
        res = []
        for cnt in range(max_freq, 0, -1): # max_freq == len(buckets) - 1
            #for ch in buckets[cnt]:
            #    res.append(ch * cnt)

            if buckets[cnt]: # ie, not empty list
                res.extend([ch * cnt for ch in buckets[cnt]])

        return ''.join(res)

"""
Solution 2b: same, but use defaultdict of lists for "buckets".

This avoids potentially creating lots of empty, unused lists in "buckets".
"""
class Solution2b:
    def frequencySort(self, s: str) -> str:
        if not s:
            return ""
        
        # count chars
        d = collections.Counter(s)
        max_freq = max(d.values())

        # bucket sort
        buckets = collections.defaultdict(list)
        for ch, cnt in d.items():
            buckets[cnt].append(ch)

        # build output string
        res = []
        for cnt in range(max_freq, 0, -1):
            if cnt in buckets: # to avoid creating empty lists in defaultdict
                #for ch in buckets[cnt]:
                #    res.append(ch * cnt)
                res.extend([ch * cnt for ch in buckets[cnt]])

        return ''.join(res)
