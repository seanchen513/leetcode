"""
1446. Consecutive Characters
Easy

Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.

Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.

Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

Example 3:

Input: s = "triplepillooooow"
Output: 5

Example 4:

Input: s = "hooraaaaaaaaaaay"
Output: 11

Example 5:

Input: s = "tourist"
Output: 1 

Constraints:

1 <= s.length <= 500
s contains only lowercase English letters.
"""

import itertools

###############################################################################
"""
Solution: 

O(n) time
O(1) extra space
"""
class Solution:
    def maxPower(self, s: str) -> int:
        n = len(s)
        res = 1
        length = 1
        
        for i in range(1, n):
            if s[i] == s[i-1]:
                length += 1
                if length > res:
                    res = length
                
            else:
                length = 1
            
        return res
        
###############################################################################
"""
Solution 2: use itertools.groupby()

LC ex4; answer = 11

s = "hooraaaaaaaaaaay"

key     group (as list)
h   ['h']
o   ['o', 'o']
r   ['r']
a   ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
y   ['y']

"""
class Solution2:
    def maxPower(self, s: str) -> int:
        # print()
        # for key, group in itertools.groupby(s):
        #     print(key, list(group))
        
        return max(len(list(group)) for _, group in itertools.groupby(s))

###############################################################################

if __name__ == "__main__":
    def test(s, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\ns = {s}")

        res = sol.maxPower(s)

        print(f"\nres = {res}\n")


    sol = Solution()
    sol = Solution2() # use itertools.groupby()

    comment = "LC ex1; answer = 2"
    s = "leetcode"
    test(s, comment)

    comment = "LC ex2; answer = 5"
    s = "abbcccddddeeeeedcba"
    test(s, comment)

    comment = "LC ex3; answer = 5"
    s = "triplepillooooow"
    test(s, comment)

    comment = "LC ex4; answer = 11"
    s = "hooraaaaaaaaaaay"
    test(s, comment)

    comment = "LC ex5; answer = 1"
    s = "tourist"
    test(s, comment)
