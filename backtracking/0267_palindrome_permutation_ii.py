"""
267. Palindrome Permutation II
Medium

Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

Example 1:

Input: "aabb"
Output: ["abba", "baab"]

Example 2:

Input: "abc"
Output: []
"""

from typing import List
import collections
import itertools

###############################################################################
"""
Solution 1: Use dict or collections.Counter() to count chars.  Return []
early if string has no permutation that is a palindrome.  Otherwise, use
backtracking to generate all palindromes from dict.

This version builds up palindromes as the recursion returns back up,
returning a list of partially built-up palindromes.  The base case
is [""] for even-length strings and a list of the single char with odd count
for odd-length strings.

Runtime: 20 ms, faster than 99.72% of Python3 online submissions
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        def palindromes(num_chars_left):
            #print(d)
            if num_chars_left <= 1:
                return odds
            
            lst = []

            for ch in d:
                if d[ch] > 1: # skip chars with 0 or 1 count                    
                    d[ch] -= 2
                    
                    # smaller_lst = palindromes(d, num_chars_left - 2)
                    # for t in smaller_lst:
                    #     lst.append( ch + t + ch )

                    lst.extend([ch + t + ch for t in palindromes(num_chars_left - 2)])

                    d[ch] += 2

            return lst

        d = collections.Counter(s)

        # List of characters with odd count.
        # This can be optimized to do an early return.
        odds = [ch for ch, count in d.items() if count & 1]

        if len(odds) > 1: # cannot be palindrome
            return []

        n = len(s)

        if not odds: # for even length string, odds was []
            odds = [""] # for use in base case of helper function
   
        return palindromes(n)

"""
Solution 1b: same as sol 1, but only build up half of each palindrome
during the recursion.  Afterwards, build out the rest of each palindrome.
"""
class Solution1b:
    def generatePalindromes(self, s: str) -> List[str]:
        def palindromes(num_chars_left):
            #print(d)
            if num_chars_left <= 1:
                return odds
            
            lst = []

            for ch in d:
                if d[ch] > 1: # skip chars with 0 or 1 count                    
                    d[ch] -= 2
                    
                    # smaller_lst = palindromes(d, num_chars_left - 2)
                    # for t in smaller_lst:
                    #     lst.append( ch + t + ch )

                    lst.extend([ch + t for t in palindromes(num_chars_left - 2)])

                    d[ch] += 2

            return lst

        d = collections.Counter(s)

        # List of characters with odd count.
        # This can be optimized to do an early return.
        odds = [ch for ch, count in d.items() if count % 2]

        if len(odds) > 1: # cannot be palindrome
            return []

        n = len(s)

        if not odds: # for even length string, odds was []
            odds = [""] # for use in base case of helper function
   
        res = palindromes(n)

        if n % 2 == 0:
            return [p + p[::-1] for p in res]
        elif n > 1:
            k = n//2 - 1 # omit the char with odd count for p[k::-1]
            return [p + p[k::-1] for p in res]
            #return [p[:-1] + p[::-1] for p in res]

###############################################################################
"""
Solution 2: Use dict or collections.Counter() to count chars.  Return []
early if string has no permutation that is a palindrome.  Otherwise, use
backtracking to generate all palindromes from dict.

This version builds up the palindrome as the recursion gets deeper, passing the
string along.  Then appends the final palindrome to a list as the base case.

https://leetcode.com/problems/palindrome-permutation-ii/discuss/120631/Short-Python-Solution-with-backtracking
"""
class Solution2:
    def generatePalindromes(self, s: str) -> List[str]:
        def helper(t):
            #print(d)
            if len(t) == n:
                res.append(t)
                return
            
            for ch in d:
                if d[ch] > 0:
                    d[ch] -= 2
                    helper(ch + t + ch)
                    d[ch] += 2

        d = collections.Counter(s)

        # List of characters with odd count.
        # This can be optimized to do an early return.
        odds = [ch for ch, count in d.items() if count & 1]

        if len(odds) > 1: # cannot be palindrome
            return []
        
        n = len(s)
        res = []
        
        if len(odds) == 1: # odd length string that can be palindrome
            d[odds[0]] -= 1
            helper(odds[0])
        else: # even length string that can be palindrome
            helper('')

        return res

###############################################################################
"""
Solution 3: brute force using itertools.permutations() and is_palindrome().

TLE
"""
class Solution3:
    def generatePalindromes(self, s: str) -> List[str]:
        def is_palindrome(s):
            # len 4 -> check 0,1; end=2
            # len 5 -> check 0,1; end=2
            for i in range(len(s)//2):
                if s[i] != s[~i]:
                    return False
            return True

        # res = set()
        # for p in itertools.permutations(s):
        #     if is_palindrome(p):
        #         res.add(''.join(p))

        #return list(res)

        return list(set(''.join(p) for p in itertools.permutations(s) if is_palindrome(p)))

###############################################################################

if __name__ == "__main__":
    def test(s, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\ns = {s}")
        
        res = sol.generatePalindromes(s)

        print(f"\nres = {res}\n")
        

    sol = Solution() # backtacking, build list of palindromes on way up
    sol = Solution1b() # same, but build half of each palindrome during recursion

    #sol = Solution2() # backtracking, build palindromes on way down

    #sol = Solution3() # brute force using itertools.permutations()

    comment = "LC ex1; answer = ['abba', 'baab']"
    s = "aabb"
    test(s, comment)

    comment = "LC ex1; answer = []"
    s = "abc"
    test(s, comment)

    comment = "LC test case; answer = ['a']"
    s = "a"
    test(s, comment)
    
    comment = ""
    s = "aabbcc"
    test(s, comment)

    comment = "LC test case; answer = ['aaa']"
    s = "aaa"
    test(s, comment)

    comment = "LC test case; answer = ['aba']"
    s = "aab"
    test(s, comment)

    # comment = 'LC test case; TLE\'s brute force; answer '
    # s = "aabbhijkkjih"
    # test(s, comment)
