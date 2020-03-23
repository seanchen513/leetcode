"""
917. Reverse Only Letters
Easy

Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

Example 1:

Input: "ab-cd"
Output: "dc-ba"

Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

Note:

S.length <= 100
33 <= S[i].ASCIIcode <= 122 
S doesn't contain \ or "
"""

"""
ord('A') = 65
ord('Z') = 90
ord('a') = 97
ord('z') = 122
"""

###############################################################################
"""
Solution: convert string to list.  Use two pointers to traverse forward
and backward until letters are found, then swap the letters.
"""
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        res = list(map(str, s))
        
        while i < j:
            while i < j and not ('A' <= s[i] <= 'Z' or 'a' <= s[i] <= 'z'):
                i += 1

            while i < j and not ('A' <= s[j] <= 'Z' or 'a' <= s[j] <= 'z'):
                j -= 1

            res[i], res[j] = res[j], res[i]
            i += 1
            j -= 1

        return ''.join(res)

###############################################################################
"""
Solution 2: use stack of letters from "s".

https://leetcode.com/problems/reverse-only-letters/solution/
"""
class Solution2:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = [ch for ch in s if ch.isalpha()]
        res = []

        for ch in s:
            if ch.isalpha():
                res.append(letters.pop())
            else:
                res.append(ch)

        return ''.join(res)

###############################################################################
"""
Solution 3: use two pointers and append to list.

https://leetcode.com/problems/reverse-only-letters/solution/
"""
class Solution3:
    def reverseOnlyLetters(self, s: str) -> str:
        res = []
        j = len(s) - 1

        for i, ch in enumerate(s):
            if ch.isalpha():
                while not s[j].isalpha():
                    j -= 1

                res.append(s[j])
                j -= 1
            else:
                res.append(ch)
        
        return ''.join(res)
