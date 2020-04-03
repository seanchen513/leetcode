"""
316. Remove Duplicate Letters
Hard

Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: "bcabc"
Output: "abc"

Example 2:

Input: "cbacdcbc"
Output: "acdb"
Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
"""

"""
1081. Smallest Subsequence of Distinct Characters
Medium

Return the lexicographically smallest subsequence of text that contains all the distinct characters of text exactly once.

Example 1:

Input: "cdadabcc"
Output: "adbc"

Example 2:

Input: "abcd"
Output: "abcd"

Example 3:

Input: "ecbacba"
Output: "eacb"

Example 4:

Input: "leetcode"
Output: "letcod"
 
Constraints:

1 <= text.length <= 1000
text consists of lowercase English letters.
Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/
"""

import collections

###############################################################################
"""
Solution: greedy, using stack, "seen" set, and last occurence dict.

The stack is a variation of an increasing stack, with the added condition
that we have to use all unique letters exactly once, so we can't pop chars
that are the last duplicate of that char in the string.

Basic idea: for each char, pop chars from stack that are bigger if there
are more available later in the string.

O(n) time: inner loop is bounded by number of elts added to stack.

O(1) extra space: "seen" set contains only unique elts, so is bounded by 26.
Can only add to stack if elt has not been seen, so stack also contains
unique elts.

Note: since len(stack) bounded by 26, we don't really need a "seen" set.
"""
class Solution:
    def removeDuplicateLetters(self, s: str) -> str: # LC316       
    #def smallestSubsequence(self, s: str) -> str: #LC1081
        stack = []
        seen = set()
        last_occ = {c: i for i, c in enumerate(s)}

        for i, ch in enumerate(s):
            if ch not in seen:
                # If the last letter in the solution so far:
                # 1. exists
                # 2. is greater than current char ch, so removing it will
                # make the string lexico. smaller
                # 3. is not the last occurence of that letter
                # then we remove it from the solution to keep the sol optimal.
                while stack and ch < stack[-1] and i < last_occ[stack[-1]]:
                    seen.discard(stack.pop())
                
                seen.add(ch)
                stack.append(ch)

        return ''.join(stack)

"""
Solution 1b: same as sol 1, but don't use "seen" set.
"""
class Solution1b:
    def removeDuplicateLetters(self, s: str) -> str: # LC316       
    #def smallestSubsequence(self, s: str) -> str: #LC1081
        stack = []
        last_occ = {c: i for i, c in enumerate(s)}

        for i, ch in enumerate(s):
            if ch not in stack:
                while stack and ch < stack[-1] and i < last_occ[stack[-1]]:
                    stack.pop()
                
                stack.append(ch)

        return ''.join(stack)

"""
LC316 ex2, LC1081 ex1; answer = adbc

01234567
cdadabcc
  a a
     b
c     cc
 d d 

last_occ:
    a: 4
    b: 5
    c: 7
    d: 3

i = 0, ch = c, stack = []
0   c   []
1   d   [c]
2   a   [c,d]       pop c,d since c and d available later in string
3   d   [a]
4   a   [a,d]       a in seen, so continue
5   b   [a,d]       no later d's in s, so can't pop d from stack
6   c   [a,d,b]
7   c   [a,d,b,c]   c in seen, so continue

"""

###############################################################################
"""
Solution 2: greedy. 

Greedily choose the smallest letter s[i] such that suffix s[i:] contains all 
the unique letters in s. When there are more than one of these duplicate
letters, choose the leftmost one. Repeat with substring s[pos:] starting at the
index pos of the chosen letter, with duplicates of the chosen letter removed.

https://leetcode.com/problems/remove-duplicate-letters/solution/

https://leetcode.com/problems/remove-duplicate-letters/discuss/76768/A-short-O(n)-recursive-greedy-solution

O(n) time: at most 26 recursive calls, and each call is O(n), for the loops
and for string.replace().

O(n) extra space: for dict and string copies

Relatively slow runtime on LC.
"""
class Solution2:
    def removeDuplicateLetters(self, s: str) -> str: # LC316       
    #def smallestSubsequence(self, s: str) -> str: #LC1081
        if not s:
            return ""
        
        d = collections.defaultdict(int)
        for ch in s:
            d[ch] += 1

        # Find pos, the index of the leftmost letter in the solution.
        # The iteration ends when we have a suffix that doesn't have at
        # least one every unique letter in the input string.
        # Then pos is the index of the smallest char found before this happens.

        pos = 0

        for i, ch in enumerate(s):
            if ch < s[pos]:
                pos = i
            
            d[ch] -= 1

            if d[ch] == 0:
                break
        
        # Answer is the leftmost letter found, plus the recursive call on the
        # remainder of the string. TO avoid duplicates of the letter found,
        # we remove it from the rest of the string.

        return s[pos] + self.removeDuplicateLetters(s[pos+1:].replace(s[pos], '')) 

"""
Solution 2b: concise version of sol 2.

https://leetcode.com/problems/remove-duplicate-letters/discuss/76787/Some-Python-solutions
"""
class Solution2b:
    def removeDuplicateLetters(self, s: str) -> str: # LC316       
    #def smallestSubsequence(self, s: str) -> str: #LC1081
        for ch in sorted(set(s)):
            suffix = s[s.index(ch):]
            
            #if set(suffix) == set(s):
            if len(set(suffix)) == len(set(s)): # faster; avoids elementwise comparison
                return ch + self.removeDuplicateLetters(suffix.replace(ch, ''))

        return ''

             
"""
LC316 ex2, LC1081 ex1; answer = adbc

01234567
cdadabcc
  a a
     b
c     cc
 d d 

unique letters: a,b,c,d
last index i such that s[i:] has all the unique letters: 3 (d)
smallest char found before i at: pos = 2 (a)
answer so far = "a"
s[pos+1:] = s[3:] = "dabcc"
substring with duplicate of chosen letter removed = dbcc
"""

###############################################################################
"""
Solution 3: greedy. Build dict that maps chars to list of their indices in
given text/string. Try to take smaller chars first, and among those, try to
take smaller indices first. Check if all other chars not taken yet can be
found after the index of this trial char.

Original attempt.

O() time
O() extra space

"""
class Solution3:
    def removeDuplicateLetters(self, text: str) -> str: # LC316        
    #def smallestSubsequence(self, text: str) -> str: #LC1081
        def ok(ch0):
            nonlocal min_index
            #print(f"ch0 = {ch0}, d = {sorted(d.items())}")

            for i in d[ch0]:
                if i < min_index:
                    continue
                
                for ch, lst in sorted(d.items()):
                    if ch != ch0 and lst and lst[-1] < i:
                        return False

                min_index = i
                return True

            return False

        res = ""
        min_index = -1

        d = collections.defaultdict(list)
        for i, ch in enumerate(text):
            d[ch].append(i)

        n = len(d)

        for _ in range(n):
            for ch in sorted(d):
                if d[ch] and ok(ch):
                    res += ch
                    del d[ch]
                    break

        return res

"""
LC1081 ex1; answer = adbc

01234567
cdadabcc
  a a
     b
c     cc
 d d 

a: 2,4
b: 5
c: 0,6,7
d: 1,3

a 00101000
b 00000100
c 10000011
d 01010000

"""

"""
LC1081 ex3; answer = eacb
ecbacba
   a  a
  b  b
 c  c
e

LC1081 ex4; answer = letcod:
01234567
leetcode
    c
      d
 ee    e
l
     o
   t

c: 4
d: 6
e: 1,2,7
l: 0
o: 5
t: 3

"""

###############################################################################

if __name__ == "__main__":
    def test(s, comment=None):
        print("="*80)
        if comment:
            print(comment)
        
        print(f"\nstring = {s}")

        #res = sol.smallestSubsequence(s) # LC316
        res = sol.removeDuplicateLetters(s) # LC1081

        print(f"\nres = {res}\n")


    sol = Solution() # greedy, using stack (variant of increasing stack)
    sol = Solution1b() # same, but don't use "seen" set

    #sol = Solution2() # greedy, choose smallest s[i] st s[i:] has all the unique letters
    #sol = Solution2b() # concise version
    
    #sol = Solution3() # greedy; 1st attempt

    comment = "LC316 ex1; answer = abc"
    s = "bcabc"
    test(s, comment)

    comment = "LC316 ex2, LC1081 ex1; answer = adbc"
    s = "cdadabcc"
    test(s, comment)

    comment = "LC1081 ex2; answer = abcd"
    s = "abcd"
    test(s, comment)

    comment = "LC1081 ex3; answer = eacb"
    s = "ecbacba"
    test(s, comment)

    comment = "LC1081 ex4; answer = leetcod"
    s = "leetcode"
    test(s, comment)
