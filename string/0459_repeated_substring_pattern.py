"""
459. Repeated Substring Pattern
Easy

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Example 2:

Input: "aba"
Output: False

Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""

import collections

###############################################################################
"""
Solution: 

Strings s and t are rotations of each other if s is substring of t + t.
A string is periodic if it is equal to some non-trivial rotation of itself.

The non-trivial rotations of s are s rotated by i chars, where i = 1, ..., len(s)-1.

https://leetcode.com/problems/repeated-substring-pattern/discuss/94334/Easy-python-solution-with-explaination

O(n) time: for string matching
O(n) extra space: for string copying and slicing

###
Example:
catcat

Non-trivial rotations of s:
atcatc      at-cat-c
tcatca      t-cat-ca

s+s:
catcatcatcat
catcat          # trivial rotation by i = 0
 atcatc         # rotation by i = 1
  tcatca        # rotation by i = 2
   catcat       # rotation by i = 3
    atcatc      # rotation by i = 4
     tcatca     # rotation by i = 5
      catcat    # trivial rotation by i = len(s) = 6

(s+s)[1:-1]
atcatcatca      at-catcat-ca

###
Example of non-periodic string:
abc

Non-trivial rotations of s:
bca
cab

s+s:
abcabc  # s is contained in s twice: for 2 trivial rotations
abc     # trivial rotation by i = 0
 bca    # rotation by i = 1
  cab   # rotation by i = 2
   abc  # trivial rotation by i = len(s) = 3

(s+s)[1:-1]
bcab    # removes the two trivial rotations

"""
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s * 2)[1:-1]

###############################################################################
"""
Solution 2: brute force, check repeat numbers equal to non-1 divisors of len(s).
Use string slicing.
 
O(n^1.5) time: loop has ~sqrt(n) iterations, and string slicing is O(n).
O(n) extra space: for string slicing
"""
class Solution3:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n == 1:
            return False

        # Do this case m = 1 outside loop so don't have to keep checking
        # if m > 1 inside loop
        if s[0] * n == s:
            return True

        end = int(n**0.5) + 1

        for m in range(2, end):
            if s[:m] * (n // m) == s or s[:n//m] * m == s:
                #print(f"n = {n}, m = {m}")
                return True

        return False

"""
Solution 2b: brute force, check repeat numbers equal to non-1 divisors of len(s).
Check char-by-char rather than use string slicing.

O(n^1.5) time: outer loop has ~sqrt(n) iterations, and each check() is O(n)
O(1) extra space
"""
class Solution3b:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def check(m): # m is size of substring to check
            for i in range(m): # index in initial substring
                ch = s[i] # letter in initial substring

                for j in range(n // m): # index of copies of substring
                    if s[i + j * m] != ch:
                        return False

            return True

        n = len(s)
        if n == 1:
            return False

        # Do this case m = 1 outside loop so don't have to keep checking
        # if m > 1 inside loop
        if check(1): # ie, all the letters are the same
            return True

        end = int(n**0.5) + 1

        for m in range(2, end): # size of substring
            if n % m == 0:
                if check(m) or check(n // m):
                    return True
                        
        return False
        
###############################################################################
"""
Solution 3:

If substring is repeated k times to form s, then the count of each letter 
in s is a multiple of k.
Therefore the gcd of letter counts is a multiple of k.
Therefore the repeat number k must be a divisor of gcd of letter counts.

Example:
aabaab
a:4
b:2
gcd = 2
repeat = 2

Example:
aabaabaab
a:6
b:3
gcd = 3
repeat = 3

Example:
aaabbcaaabbc
a:6
b:4
c:2
gcd = 2
repeat = 2

Example:
a:40
b:60
n = 100
gcd = 20; non-trivial divisors: 2, 4, 5, 10
repeat = 2
m = 50

"""
class Solution2:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            
            return a

        n = len(s)
        d = collections.Counter(s)

        g = n # gcd of all counts
        for cnt in d.values():
            g = gcd(g, cnt)

        #print(f"\nd = {d}")
        #print(f"gcd = {g}")

        if g == 1:
            return False

        # Check repeat number that is gcd.
        if s[:n//g] * g == s:
            return True

        # Check repeat numbers that are non-one divisors of gcd.
        end = int(g**0.5) + 1

        for m in range(2, end):
            if n % m == 0:
                if s[:m] * (n//m) == s or s[:n//m] * m == s:
                    return True

        return False

###############################################################################

if __name__ == "__main__":
    def test(s, comment=None):       
        print("="*80)
        if comment:
            print(comment)

        print(f"\ns = {s}")
        
        res = sol.repeatedSubstringPattern(s)

        print(f"\nresult = {res}\n")


    sol = Solution() # check if s is nontrivial rotation of itself

    # brute force, check repeat numbers equal to non-1 divisors of len(s)
    #sol = Solution2() # use string slicing
    #sol = Solution2b() # char-by-char comparisons

    # count chars and look at gcd of counts; 
    # check repeat numbers equal to non-one divisors of gcd
    sol = Solution3() 

    comment = "LC ex1; answer = True"
    s = "abab"
    test(s, comment)
   
    comment = "LC ex2; answer = False"
    s = "aba"
    test(s, comment)

    comment = "LC ex3; answer = True"
    s = "abcabcabcabc"
    test(s, comment)

    comment = "LC TC; answer = False"
    s = "a"
    test(s, comment)

    comment = "LC TC; answer = True"
    s = "bb"
    test(s, comment)

    comment = "LC TC; answer = True"
    s = "abcabc"
    test(s, comment)

    comment = "LC TC; answer = True"
    s = "babbaaabbbbabbaaabbbbabbaaabbbbabbaaabbbbabbaaabbbbabbaaabbbbabbaaabbbbabbaaabbbbabbaaabbbbabbaaabbb"
    test(s, comment)
