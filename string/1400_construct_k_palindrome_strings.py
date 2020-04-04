"""
1400. Construct K Palindrome Strings
Medium

Given a string s and an integer k. You should construct k non-empty palindrome strings using all the characters in s.

Return True if you can use all the characters in s to construct k palindrome strings or False otherwise.

Example 1:

Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"

Example 2:

Input: s = "leetcode", k = 3
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s.

Example 3:

Input: s = "true", k = 4
Output: true
Explanation: The only possible solution is to put each character in a separate string.

Example 4:

Input: s = "yzyzyzyzyzyzyzy", k = 2
Output: true
Explanation: Simply you can put all z's in one string and all y's in the other string. Both strings will be palindrome.

Example 5:

Input: s = "cr", k = 7
Output: false
Explanation: We don't have enough characters in s to construct 7 palindromes.
 
Constraints:
1 <= s.length <= 10^5
All characters in s are lower-case English letters.
1 <= k <= 10^5
"""

import collections

###############################################################################
"""
Solution: greedy. Count frequency of each char in s.

Two conditions:
1. len(s) >= k in order to have enough chars to create k palindromes.
2. A palindrome can have at most one char with an odd count.
If there are too many chars with an odd count, then k is too small.

O(n) time
O(1) extra space: dict has at most 26 entries.

"""
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        d = collections.defaultdict(int)
        for ch in s:
            d[ch] += 1

        count = 0
        for cnt in d.values():
            if cnt % 2 == 1:
                count += 1

        return count <= k

"""
Solution 1b: concise version of sol 1.
"""
class Solution1b:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        
        d = collections.Counter(s)

        return sum(cnt & 1 for cnt in d.values()) <= k


"""
Solution 1c: even more concise.
"""
class Solution1c:
    def canConstruct(self, s: str, k: int) -> bool:
        #return len(s) >= k and sum(cnt & 1 for cnt in collections.Counter(s).values()) <= k
        return len(s) >= k >= sum(cnt & 1 for cnt in collections.Counter(s).values())

"""
ex1, k=2, True
a2
n2
b1
e2
l2
num 1s = 1

ex2, k=3, False
l1
e2
t1
c1
o1
d1
e1
num 1s = 6

ex3, k=4, True
t1
r1
u1
e1
num1 1s = 4

ex4, k=2, True
y #
z #
num chars w/ odd count = ?

ex5, k=7, False--too few chars in s
c1
r1
num 1s = 2

"""

###############################################################################

if __name__ == "__main__":
    def test(s, k, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\nstring = {s}")

        res = sol.canConstruct(s, k)

        print(f"\nres = {res}\n")


    sol = Solution()
    #sol = Solution1b() # more concise
    #sol = Solution1c() # even more concise

    comment = "LC ex1; answer = True"
    s = "annabelle"
    k = 2
    test(s, k, comment)

    comment = "LC ex2; answer = False"
    s = "leetcode"
    k = 3
    test(s, k, comment)

    comment = "LC ex3; answer = True"
    s = "true"
    k = 4
    test(s, k, comment)

    comment = "LC ex4; answer = True"
    s = "yzyzyzyzyzyzyzy"
    k = 2
    test(s, k, comment)

    comment = "LC TC; answer = False"
    s = "cxayrgpcctwlfupgzirmazszgfiusitvzsnngmivctprcotcuutfxdpbrdlqukhxkrmpwqqwdxxrptaftpnilfzcmknqljgbfkzuhksxzplpoozablefndimqnffrqfwgaixsovmmilicjwhppikryerkdidupvzdmoejzczkbdpfqkgpbxcrxphhnxfazovxbvaxyxhgqxcxirjsryqxtreptusvupsstylpjniezyfokbowpbgxbtsemzsvqzkbrhkvzyogkuztgfmrprz"
    k = 5
    test(s, k, comment)
