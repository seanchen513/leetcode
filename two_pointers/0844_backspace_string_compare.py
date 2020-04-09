"""
844. Backspace String Compare
Easy

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.

Follow up:

Can you solve it in O(N) time and O(1) space?
"""

import itertools

###############################################################################
"""
Solution: traverse both strings in reverse at the same time and backspace as 
much as possible.

O(n) time
O(1) extra space

"""
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1
        bs = 0 # count for #'s seen and unused so far in traversing s
        bt = 0 # count for #'s seen and unused so far in traversing t

        while i >= 0 and j >= 0:
            if s[i] != '#' and t[j] != '#':
                if s[i] != t[j]:
                    return False
                i -= 1
                j -= 1

            # Backspace in s as much as possible.
            # After loop, i < 0 or (s[i] != '#' and bs == 0).
            while i >= 0 and (s[i] == '#' or bs > 0):
                if s[i] == '#':
                    bs += 1
                elif bs > 0:
                    bs -= 1

                i -= 1

            # Backspace in t as much as possible.
            while j >= 0 and (t[j] == '#' or bt > 0):
                if t[j] == '#':
                    bt += 1
                elif bt > 0:
                    bt -= 1

                j -= 1

        if i >= 0 or j >= 0:
            return False

        return True

"""
Solution 1b: same idea, but use generator function.
"""
class Solution1b:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def f(s):
            skip = 0
            for ch in reversed(s):
                if ch == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else: # ch != '#' and skip == 0
                    yield ch

        return all(x == y for x, y in itertools.zip_longest(f(s), f(t)))

###############################################################################
"""
Solution 2: use stack to convert strings.

O(m+n) time
O(m+n) extra space: for stacks and new strings
"""
class Solution2:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspace(s):
            stack = []

            for ch in s:
                if ch != '#':
                    stack.append(ch)
                elif stack:
                    stack.pop()                

            return ''.join(stack)

        return backspace(s) == backspace(t)

###############################################################################

if __name__ == "__main__":
    def test(s, t, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\ns = {s}")
        print(f"t = {t}")

        res = sol.backspaceCompare(s, t)

        print(f"\nres = {res}\n")


    sol = Solution() # use 2 ptrs and traverse strings in reverse at same time
    sol = Solution1b() # use generator fn

    #sol = Solution2() # use stack to convert strings

    comment = "LC ex1; answer = True"
    s = "ab#c"
    t = "ad#c"
    test(s, t, comment)

    comment = "LC ex2; answer = True"
    s = "ab##"
    t = "c#d#"
    test(s, t, comment)
    
    comment = "LC ex3; answer = True"
    s = "a##c"
    t = "#a#c"
    test(s, t, comment)
    
    comment = "LC ex4; answer = False"
    s = "a#c"
    t = "b"
    test(s, t, comment)
    
    comment = "LC TC showing we need to check after loop; answer = False"
    s = "bxj##tw" # after loop: i = 0, s[i] = 'b'
    t = "bxj###tw" # after loop: j = -1
    test(s, t, comment)
