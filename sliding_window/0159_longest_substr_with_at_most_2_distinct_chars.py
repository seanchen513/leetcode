"""
159. Longest Substring with At Most Two Distinct Characters
Medium

Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.

Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
"""

###############################################################################
"""
Solution: use 2 pointers for sliding window of substring, and dict that maps
char to index it was last seen at.

Optimized version of sol 1b.

O(n) time
O(1) extra space

Runtime: 28 ms, faster than 100.00% of Python3 online submissions
Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        d = {}
        start = 0
        mx = -1 # so empty string returns 0

        for i, c in enumerate(s):
            #print(f"\ni={i}, start={start}, d={d}")
            d[c] = i
            
            if len(d) == 3:
                # 1 + index of char with smaller last-seen index
                start = min(d.values()) + 1
                del d[s[start - 1]]
            elif i - start > mx:
                mx = i - start

        return mx + 1

"""
Solution 1b: use 2 pointers for sliding window of substring, and dict that maps
char to index it was last seen at.

O(n) time
O(1) extra space

Runtime: 36 ms, faster than 99.84% of Python3 online submissions
Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions
"""
class Solution1b:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        d = {}
        start = 0
        mx = -1 # so empty string returns 0

        for i, c in enumerate(s):
            #print(f"\ni={i}, start={start}, d={d}")
            d[c] = i

            if len(d) == 3:
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
    def test(s, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(s)

        res = sol.lengthOfLongestSubstringTwoDistinct(s)

        print(f"\nres = {res}\n")

    sol = Solution() #
    #sol = Solution1b() #

    comment = "LC ex1; answer = 3"
    s = "eceba"
    test(s, comment)

    comment = "LC ex2; answer = 5"
    s = "ccaabbb"
    test(s, comment)

    comment = "LC test case; answer = 3"
    s = "cdaba"
    test(s, comment)

    comment = "LC test case; answer = 4"
    s = "abaccc"
    test(s, comment)

    comment = "LC test case; answer = 0"
    s = ""
    test(s, comment)
