"""
12. Integer to Roman
Medium

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"

Example 2:

Input: 4
Output: "IV"

Example 3:

Input: 9
Output: "IX"

Example 4:

Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

###############################################################################
"""
Solution 1: straightforward.
"""
class Solution:
    def intToRoman(self, n: int) -> str:
        values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

        s = []

        while n >= 1000:
            n -= 1000
            s.append('M')

        if n >= 900:
            n -= 900
            s.append('CM')
        
        if n >= 500:
            n -= 500
            s.append('D')

        if n >= 400:
            n -= 400
            s.append('CD')

        while n >= 100:
            n -= 100
            s.append('C')

        if n >= 90:
            n -= 90
            s.append('XC')

        if n >= 50:
            n -= 50
            s.append('L')

        if n >= 40:
            n -= 40
            s.append('XL')

        while n >= 10:
            n -= 10
            s.append('X')

        if n >= 9:
            n -= 9
            s.append('IX')

        if n >= 5:
            n -= 5
            s.append('V')

        if n >= 4:
            n -= 4
            s.append('IV')

        while n >= 1:
            n -= 1
            s.append('I')

        return ''.join(s)

"""
Solution 1b: same as sol 1, but use values list of tuples.
"""
class Solution1b:
    def intToRoman(self, n: int) -> str:
        values = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
            (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

        s = []

        for v, symbol in values:
            while n >= v:
                n -= v
                s.append(symbol)

        return ''.join(s)

"""
Solution 1c: same as sol 1b, but use // and *
"""
class Solution1c:
    def intToRoman(self, n: int) -> str:
        values = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
            (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

        s = []

        for v, symbol in values:
            s.append( symbol * int(n//v) )
            n %= v

        return ''.join(s)

###############################################################################
"""
Solution 2: use lookup lists of all possibilities for each decimal position.

https://leetcode.com/problems/integer-to-roman/discuss/6274/Simple-Solution
"""
class Solution2:
    def intToRoman(self, n: int) -> str:
        M = ['', 'M', 'MM', 'MMM']
        C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

        return M[n // 1000] + C[(n % 1000) // 100] + X[(n % 100) // 10] + I[n % 10]

###############################################################################

if __name__ == "__main__":
    def test(n, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\nn = {n}")
        
        res = sol.intToRoman(n)

        print(f"\nres = {res}\n")
        

    sol = Solution()
    sol = Solution1b()
    sol = Solution1c()

    sol = Solution2()
    
    comment = "LC ex1; answer = III"
    n = 3
    test(n, comment)

    comment = "LC ex2; answer = IV"
    n = 4
    test(n, comment)

    comment = "LC ex3; answer = IX"
    n = 9
    test(n, comment)

    comment = "LC ex4; answer = LVIII"
    n = 58
    test(n, comment)

    comment = "LC ex5; answer = MCMXCIV"
    n = 1994
    test(n, comment)
