"""
1417. Reformat The String
Easy

Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string.

Example 1:

Input: s = "a0b1c2"
Output: "0a1b2c"
Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.

Example 2:

Input: s = "leetcode"
Output: ""
Explanation: "leetcode" has only characters so we cannot separate them by digits.

Example 3:

Input: s = "1229857369"
Output: ""
Explanation: "1229857369" has only digits so we cannot separate them by characters.

Example 4:

Input: s = "covid2019"
Output: "c2o0v1i9d"

Example 5:

Input: s = "ab123"
Output: "1a2b3"
 
Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters and/or digits.
"""

###############################################################################
"""
Solution: use stacks for digits and letters. Make sure that the lengths of
the stacks are within 1. Start building with the type that there are more of.

O(n) time
O(n) extra space
"""
class Solution:
    def reformat(self, s: str) -> str:
        digits = []
        letters = []
        t = ""

        for ch in s:
            #if ch in "0123456789":
            if ord(ch) < 97: # ord('a') is 97; ord() of 0 and 9 are 48 and 57
                digits.append(ch)
            else:
                letters.append(ch)

        if len(digits) - len(letters) not in (-1, 0, 1):
            return ""
        
        if len(digits) > len(letters):
            t += digits.pop()

        while digits and letters:
            t += letters.pop() + digits.pop()

        if letters:
            t += letters.pop()
            
        return t

###############################################################################
"""
Solution 2: same, but use indices for digits and letters lists, rather than
treating them as stacks. Also, build output using list.

O(n) time
O(n) extra space
"""
class Solution2:
    def reformat(self, s: str) -> str:
        digits = []
        letters = []
        t = []

        for ch in s:
            #if ch in "0123456789":
            if ord(ch) < 97: # ord('a') is 97; ord() of 0 and 9 are 48 and 57
                digits.append(ch)
            else:
                letters.append(ch)

        if len(digits) - len(letters) not in (-1, 0, 1):
            return ""
        
        i = 0 # index for digits
        j = 0 # index for letters

        if len(digits) > len(letters):
            t.append(digits[i])
            i += 1

        while i < len(digits) and j < len(letters):
            t.extend([letters[j], digits[i]])
            i += 1
            j += 1

        if j < len(letters):
            t.append(letters[j])
            
        return ''.join(t)

###############################################################################

if __name__ == "__main__":
    def test(s, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\ns={s}")

        res = sol.reformat(s)

        print(f"\nres = {res}\n")


    sol = Solution()

    comment = "LC ex1; answer = "
    s = "a0b1c2"
    test(s, comment)

    comment = "LC ex2; answer = (empty string)"
    s = "leetcode"
    test(s, comment)

    comment = "LC ex3; answer = (empty string)"
    s = "1229857369"
    test(s, comment)

    comment = "LC ex4; answer = "
    s = "covid2019"
    test(s, comment)

    comment = "LC ex5; answer = "
    s = "ab123"
    test(s, comment)
