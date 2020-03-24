"""
3. Longest Substring Without Repeating Characters
Medium

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

import collections

###############################################################################
"""
Solution: use 2 pointers for sliding window and dict mapping char to index
it was last seen.

This is an optimized version of using sliding window with a "seen" set.

O(n) time: each char in string is visited at most once.
O(min(n,k)) extra space: for dict.

Runtime: 44 ms, faster than 97.42% of Python3 online submissions
Memory Usage: 13.1 MB, less than 98.47% of Python3 online submissions
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mx = 0
        start = 0
        d = {}

        for i, c in enumerate(s):
            if c in d and d[c] + 1 > start:
                start = d[c] + 1
            
            d[c] = i

            #print(f"i={i}, start={start}, mx={mx}")
            if i - start + 1 > mx:
                mx = i - start + 1

        return mx

"""
Solution 1b: same as sol 1, but optimized a bit.

Runtime: 36 ms, faster than 99.89% of Python3 online submissions
Memory Usage: 13 MB, less than 98.98% of Python3 online submissions
"""
class Solution1b:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if not s:
        #     return 0

        mx = -1 # so empty string returns 0
        start = 0
        d = {}

        for i, c in enumerate(s):
            if c in d and d[c] + 1 > start:
                start = d[c] + 1
            
            d[c] = i

            if i - start > mx:
                mx = i - start

        return mx + 1

###############################################################################
"""
Solution 2: use 2 pointers for sliding window and "seen" set.

O(n) time: each char in string is visited at most twice by i and j.
O(min(n,k)) extra space: for set.

Runtime: 52 ms, faster than 85.22% of Python3 online submissions
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        mx = 0
        i = j = 0
        seen = set()

        while i < n and j < n:
            if s[j] in seen:
                seen.remove(s[i])
                i += 1
            else:
                seen.add(s[j])
                j += 1

                if j - i > mx:
                    mx = j - i

        return mx

###############################################################################
"""
Solution 3: use deque containing running substring of unique chars.

Note: deque has at most 26 chars, if only lowercase chars are allowed.

O(n) time: we traverse string, and each char in string can be removed
from the deque at most once.

O(min(n,k)) extra space: for deque, where k is the size of the character set
or alphabet (eg, 26 for lowercase letters).

Runtime: 48 ms, faster than 93.13% of Python3 online submissions
Memory Usage: 13 MB, less than 99.49% of Python3 online submissions
"""
class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mx = 0
        t = collections.deque([])

        for c in s:
            if c in t:
                while t[0] != c:
                    t.popleft()

                t.popleft()

            t.append(c)

            if len(t) > mx:
                mx = len(t)

        return mx
        
###############################################################################
"""
Solution 4: use collections.OrderedDict().

Runtime: 64 ms, faster than 60.49% of Python3 online submissions
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions
"""
class Solution4:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mx = 0
        start = 0
        d = collections.OrderedDict()

        for i, c in enumerate(s):
            if c in d:
                n_del = d[c] - start + 1
                start = d[c] + 1
                for _ in range(n_del):
                    d.popitem(last=False)

            d[c] = i

            if i - start + 1 > mx:
                mx = i - start + 1

            # if len(d) > mx:
            #     mx = len(d)

        return mx

###############################################################################
"""
Solution 5: use dict mapping chars to index char was last seen, and delete
entries in dict as needed.

Runtime: 204 ms, faster than 21.44% of Python3 online submissions
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions
"""
class Solution5:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mx = 0
        start = 0
        d = {}        

        for i, c in enumerate(s):
            if c in d:
                start = d[c] + 1

                del_list = []
                for k, idx in d.items():
                    if idx < start: 
                        del_list.append(k)
                
                for k in del_list:
                    del d[k]
            
            curr_len = i - start + 1

            if curr_len > mx:
                mx = curr_len

            d[c] = i

        return mx

###############################################################################
"""
Solution 6: brute force

O(n^3) time
O(n) extra space

TLE
"""
class Solution6:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        k = n

        while k > 1:
            for i in range(n-k+1):
                t = s[i:i+k]

                d = collections.Counter(t)

                if all(cnt == 1 for cnt in d.values()):
                    return k

            k -= 1

        return 1

###############################################################################

if __name__ == "__main__":
    def test(s, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(s)

        res = sol.lengthOfLongestSubstring(s)

        print(f"\nres = {res}\n")

    sol = Solution() # optimized sliding window w/ dict
    #sol = Solution2() # sliding window with "seen" set
    #sol = Solution3() # use deque
    #sol = Solution4() # use OrderedDict()
    #sol = Solution5() # use dict
    #sol = Solution6() # brute force

    comment = "LC ex1; answer = 3"
    s = "abcabcbb"
    test(s, comment)

    comment = "LC ex2; answer = 1"
    s = "bbbbb"
    test(s, comment)

    comment = "LC ex3; answer = 3"
    s = "pwwkew"
    test(s, comment)

    comment = "LC test case; empty string; answer = 0"
    s = ""
    test(s, comment)

    comment = "LC test case; single space; answer = 1"
    s = " "
    test(s, comment)

    comment = "LC test case; answer = 2"
    s = "au"
    test(s, comment)

    comment = "LC test case; answer = 2"
    s = "aab"
    test(s, comment)

    comment = "LC test case; answer = 2"
    s = "abba"
    test(s, comment)

    comment = "LC test case; answer = 3"
    s = "abcabcbb"
    test(s, comment)

    comment = "Based on LC test case; answer = 94"
    s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    test(s, comment)

    # comment = "Based on LC test case; answer = 94"
    # s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"*100
    # test(s, comment)
