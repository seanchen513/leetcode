"""
266. Palindrome Permutation
Easy

Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false

Example 2:

Input: "aab"
Output: true

Example 3:

Input: "carerac"
Output: true
"""

import collections

###############################################################################
"""
Solution 1: use dict or collections.Counter() to count chars.

If len(s) is even, then s is a palindrome if and only if character has a twin,
ie, if the count of every character is even.

If len(s) is odd, then s is a palindrome if and only if one character has an
odd count, and all other characters have an even count.

O(n) time
O(1) extra space
"""
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # d = collections.defaultdict(int)
        # for ch in s:
        #     d[ch] += 1

        d = collections.Counter(s)

        if len(s) % 2 == 0:
            return all(count % 2 == 0 for count in d.values())
        else:
            return sum(count % 2 for count in d.values()) == 1

        ### This works, but doesn't exit early when len(s) is even.
        #return len(s) % 2 == sum(count % 2 for count in d.values())
        
###############################################################################
"""
Solution 2: use set.

O(n) time
O(1) extra space
"""
class Solution2:
    def canPermutePalindrome(self, s: str) -> bool:
        chars = set()

        for ch in s:
            if ch in chars:
                chars.remove(ch)
            else:
                chars.add(ch)

        return len(s) % 2 == len(chars)

###############################################################################

if __name__ == "__main__":
    def test(s, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\ns = {s}")
        
        res = sol.canPermutePalindrome(s)

        print(f"\nres = {res}\n")
        

    sol = Solution() # use dict or collections.Counter()
    sol = Solution2() # use set

    comment = "LC ex1; answer = False"
    s = "code"
    test(s, comment)

    comment = "LC ex2; answer = True"
    s = "aab"
    test(s, comment)

    comment = "LC ex3; answer = True"
    s = "carerac"
    test(s, comment)
