"""
91. Decode Ways
Medium

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""

###############################################################################
"""
Solution:

O(n) time
O(1) extra space

Runtime: 24 ms, faster than 95.78% of Python3 online submissions
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        n = len(s)

        # Currently, res = 1 is number of ways to decode string of length 1.
        # Let prev start at 1 so calculation for string beginning "10", ..., "26",
        # res += prev, results in res = 1 + 1 = 2.
        prev, res = 1, 1

        for i in range(1, n):
            temp = res

            # Number of ways if take current digit by itself.
            # If digit is 1, ..., 9, then res is same as previous res.
            # If digit is 0, then reset res since 0 doesn't represent a letter.
            if s[i] == "0":
                res = 0

            # Add number of ways if take previous and current char together.
            k = int(s[i-1:i+1])
            if 10 <= k <= 26:
                res += prev

            # This early return part is optional.
            elif k % 10 == 0: # 00, 30, 40, 50, 60, 70, 80, 90
                return 0

            prev = temp

        return res

"""
Solution1b: rewrite of sol 1.

O(n) time
O(1) extra space
"""
class Solution1b:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        n = len(s)
        prev, res = 1, 1

        for i in range(1, n):
            k = int(s[i-1:i+1])

            if k == 10 or k == 20: 
                # res = prev: ignore previous res since we have to combine the
                # current "0" with the previous digit.
                prev, res = res, prev
            elif k % 10 == 0: # 00, 30, 40, 50, 60, 70, 80, 90
                return 0
            elif 11 <= k <= 26:
                prev, res = res, prev + res
            else: # k is 01, ..., 09, 27, 28, ..., 99
                prev, res = res, res

        return res

"""
Solution 1c: same as sol 1b, but track current and previous characters instead
of converting to integer.
"""
class Solution1c:
    def numDecodings(self, s: str) -> int:
        prev_ch = s[0]
        if prev_ch == "0":
            return 0

        n = len(s)
        prev, res = 1, 1

        for i in range(1, n):
            ch = s[i]

            if ch == "0":
                if prev_ch == "1" or prev_ch == "2":
                    prev, res = res, prev
                else:
                    return 0
            
            elif (prev_ch == "1") or (prev_ch == "2" and 1 <= int(ch) <= 6):
                prev, res = res, prev + res
            else:
                prev, res = res, res

            prev_ch = ch

        return res

###############################################################################
"""
Solution 2: recursion w/ memoization via @functools.lru_cache().

O(n) time
O(n) extra space: for cache and for recursion stack

TLE w/o memoization
"""
import functools
class Solution2:
    def numDecodings(self, s: str) -> int:
        @functools.lru_cache(None)
        def rec(i):
            if i >= n:
                return 1

            if s[i] == "0":
                return 0

            # at last char and it's not 0
            if i == n - 1:
                return 1

            if int(s[i:i+2]) <= 26:
                return rec(i+1) + rec(i+2)

            return rec(i+1)

        if s[0] == "0":
            return 0

        n = len(s)

        return rec(0)

"""
Solution 2b: recursion w/ memoization.

O(n) time
O(n) extra space: for cache and for recursion stack
"""
class Solution2b:
    def numDecodings(self, s: str) -> int:
        def rec(i):
            if i >= n:
                return 1

            if s[i] == "0":
                return 0

            # at last char and it's not 0
            if i == n - 1:
                return 1

            if i in memo:
                return memo[i]

            memo[i] = rec(i+1)

            if int(s[i:i+2]) <= 26:
                memo[i] += rec(i+2)

            return memo[i]

        if s[0] == "0":
            return 0

        n = len(s)
        memo = {}

        return rec(0)

###############################################################################

if __name__ == "__main__":
    def test(s, comment=None):
        print("="*80)
        if comment:
            print(comment)
        
        print(f"\nstring = {s}")

        res = sol.numDecodings(s)

        print(f"\nres = {res}\n")


    sol = Solution() # tabulation
    sol = Solution()
    sol = Solution()

    sol = Solution2() # memoization via @functools.lru_cache()
    sol = Solution2b() # memoization

    comment = "LC ex1; answer = 2"
    s = "12"
    test(s, comment)

    comment = "LC ex1; answer = 3"
    s = "226"
    test(s, comment)

    comment = "LC test case; answer = 0"
    s = "0"
    test(s, comment)

    comment = "test case; answer = 0"
    s = "00"
    test(s, comment)

    comment = "LC test case; answer = 1"
    s = "10"
    test(s, comment)

    comment = "LC test case; answer = 0"
    s = "100"
    test(s, comment)

    comment = "LC test case; answer = 1"
    s = "110"
    test(s, comment)

    comment = "LC test case; answer = 0"
    s = "230"
    test(s, comment)

    comment = "LC test case; answer = 3"
    s = "12120"
    test(s, comment)

    comment = "answer = 3"
    s = "111"
    test(s, comment)

    comment = "answer = 5"
    s = "1111"
    test(s, comment)

    comment = "answer = 8"
    s = "11111"
    test(s, comment)
