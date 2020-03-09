"""
168. Excel Sheet Column Title
Easy

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...

Example 1:

Input: 1
Output: "A"

Example 2:

Input: 28
Output: "AB"

Example 3:

Input: 701
Output: "ZY"
"""

###############################################################################
"""
Solution:

Want to use "% 26", so use (n-1) so that 'Z' <-> 25.

n   n-1 ch
1   0   'A'
2   1   'B'
...
26  25  'Z'

Note that:
ZY = 701 = 26^2 + 25 = (25+1)*26 + (24+1)
ZZ = 702 = 26^2 + 26 = (25+1)*26 + (25+1)
AAA = 703 = 26^2 + 26 + 1 = (0+1)*26^2 + (0+1)*26 + (0+1)

where A maps to 0+1, ..., Y to 24+1, and Z to 25+1.
"""
class Solution:
    def convertToTitle(self, n: int) -> str:
        s = []

        while n > 0:
            s.append( chr((n-1) % 26 + 65) ) # ord('A') is 65
            n = (n-1) // 26
            
        return ''.join(reversed(s))

###############################################################################
"""
Solution 2: use recursion.

Note: 0 maps to the empty string.

Get "RecursionError: maximum recursion depth exceeded" if don't include
'if n else ""'.
"""
class Solution2:
    def convertToTitle(self, n: int) -> str:
        return self.convertToTitle((n-1) // 26) + chr((n-1) % 26 + 65) if n else ""

###############################################################################

if __name__ == "__main__":
    def test(n, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\nn = {n}")

        res = sol.convertToTitle(n)

        print(f"res = {res}\n")


    sol = Solution()
    sol = Solution2() # use recursion
    
    comment = "LC ex1; answer = A"
    n = 1
    test(n, comment)

    comment = "LC ex2; answer = AB"
    n = 28
    test(n, comment)

    comment = "LC ex3; answer = ZY"
    n = 701
    test(n, comment)

    comment = "answer = AAA"
    n = 703
    test(n, comment)
