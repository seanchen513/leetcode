"""
171. Excel Sheet Column Number
Easy

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...

Example 1:

Input: "A"
Output: 1

Example 2:

Input: "AB"
Output: 28

Example 3:

Input: "ZY"
Output: 701
"""

###############################################################################
"""
"""
class Solution:
    def titleToNumber(self, s: str) -> int:
        n = 0
        
        for ch in s:
            #n = n*26 + ord(ch) - ord('A') + 1
            n = n*26 + ord(ch) - 64 # ord('A') is 65
            
        return n

###############################################################################
"""
Solution 2: use functools.reduce().
"""
import functools
class Solution2:
    def titleToNumber(self, s: str) -> int:
        return functools.reduce(lambda x, y : x * 26 + y, [ord(ch) - 64 for ch in s])

###############################################################################

if __name__ == "__main__":
    def test(grid, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\ns = {s}")

        res = sol.titleToNumber(s)

        print(f"res = {res}\n")


    sol = Solution()
    #sol = Solution2() # use functools.reduce()
    
    comment = "LC ex1; answer = 1"
    s = "A"
    test(s, comment)

    comment = "LC ex2; answer = 28"
    s = "B"
    test(s, comment)

    comment = "LC ex3; answer = 701"
    s = "ZY"
    test(s, comment)
