"""
340. Longest Substring with At Most K Distinct Characters
Hard

Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.

Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
"""

import collections

###############################################################################
"""
Solution: use 2 pointers for sliding window of substring, and dict that counts
chars. If get more than k distinct chars in substring, increment left pointer
and decrement counts until there are only k distinct chars.

O(n) time
O(k) extra space
"""
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        d = collections.defaultdict(int)
        start = 0
        mx = -1 # so empty string returns 0
        n = 0 # count of distinct chars

        for i, c in enumerate(s):
            if d[c] == 0:
                n += 1

            d[c] += 1

            # Move start (left ptr) until we have only k distinct chars
            # in substring from start index to current index.
            while n > k:
                d[s[start]] -= 1
                
                if d[s[start]] == 0:
                    n -= 1
                
                start += 1

            if i - start > mx:
                mx = i - start

        return mx + 1

###############################################################################
"""
Solution 2: use 2 pointers for sliding window of substring, and OrderedDict
dict that maps char to index it was last seen at. Using an OrderedDict
makes it easy to remove the entry with min last-seen index, rather than
using min().

O(n) time
O(k) extra space
"""
class Solution2:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        d = collections.OrderedDict()
        start = 0
        mx = -1 # so empty string returns 0
        k += 1 # to avoid repeated use of k + 1 when checking len(d)

        for i, c in enumerate(s):
            # If current char already in dict, delete it so that after
            # adding it to the dict, it becomes the most recent entry.
            if c in d:
                del d[c]
            d[c] = i
            
            if len(d) == k:
                _, m = d.popitem(last=False)    
                start = m + 1
                
            elif i - start > mx:
                mx = i - start

        return mx + 1

###############################################################################
"""
Solution 3: use 2 pointers for sliding window of substring, and dict that maps
char to index it was last seen at.

Optimized version of sol 1b.

O(nk) time: since it takes O(k) time to find min in dict.
The worst case happens when string contains n distinct chars.
This isn't important unless n is large, in which case the size of the alphabet
would also be large.

O(k) extra space
"""
class Solution3:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        d = {}
        start = 0
        mx = -1 # so empty string returns 0
        k += 1 # to avoid repeated use of k + 1 when checking len(d)

        for i, c in enumerate(s):
            #print(f"\ni={i}, start={start}, d={d}")
            d[c] = i
            
            if len(d) == k:
                # 1 + index of char with smaller last-seen index
                start = min(d.values()) + 1
                del d[s[start - 1]]
            elif i - start > mx:
                mx = i - start

        return mx + 1

"""
Solution 3b: use 2 pointers for sliding window of substring, and dict that maps
char to index it was last seen at.

O(nk) time
O(k) extra space
"""
class Solution3b:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        d = {}
        start = 0
        mx = -1 # so empty string returns 0

        for i, c in enumerate(s):
            #print(f"\ni={i}, start={start}, d={d}")
            d[c] = i

            if len(d) == k + 1:
                # index of char with smaller last-seen index
                m = min(d.values())
                del d[s[m]]
                start = m + 1

            # Note: this doesn't need to be checked if c not in d and
            # len(d) == 2.
            if i - start > mx:
                mx = i - start

        return mx + 1

###############################################################################

if __name__ == "__main__":
    def test(s, k, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(s)

        res = sol.lengthOfLongestSubstringKDistinct(s, k)

        print(f"\nres = {res}\n")

    sol = Solution() # use dict that counts chars
    sol = Solution2() # use OrderedDict()
    #sol = Solution3() # use dict that maps chars to index last seen
    #sol = Solution3b() #

    comment = "LC ex1; answer = 3"
    s = "eceba"
    k = 2
    test(s, k, comment)

    comment = "LC ex2; answer = 2"
    s = "aa"
    k = 1
    test(s, k, comment)

    comment = "LC test case; answer = 4"
    s = "abaccc"
    k = 2
    test(s, k, comment)
