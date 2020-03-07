"""
13. Roman to Integer
Easy

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

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3

Example 2:

Input: "IV"
Output: 4

Example 3:

Input: "IX"
Output: 9

Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

import collections

###############################################################################
"""
Solution 1: use values dict with 7 Roman numeral symbols and check for
subtraction case.
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

        n = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and values[s[i]] < values[s[i+1]]: # subtract
                n += values[s[i+1]] - values[s[i]]
                i += 2
            else:
                n += values[s[i]]
                i += 1

        return n

"""
Solution 1b: use values dict with 13 unique symbols, some of length 1 and some
of length 2.  Check for symbols by length.
"""
class Solution1b:
    def romanToInt(self, s: str) -> int:
        values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1,
            'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4}

        n = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in values: # subtract
                n += values[s[i:i+2]]
                i += 2
            else:
                n += values[s[i]]
                i += 1

        return n

###############################################################################
"""
Solution 2: use values dict with 7 unique symbols.  Compare adjacent values.
"""
class Solution2:
    def romanToInt(self, s: str) -> int:
        values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

        n = values[s[-1]]
        i = 0

        for i in range(len(s)-1):
            if values[s[i]] < values[s[i+1]]:
                n -= values[s[i]]
            else:
                n += values[s[i]]

        return n

"""
Solution 2b: same as sol 2, but use map() and sum().
"""
class Solution2b:
    def romanToInt(self, s: str) -> int:
        values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

        m = list(map(lambda x: values[x], s))
        
        for i in range(len(m)-1):
            if m[i] < m[i+1]:
                m[i] *= - 1

        return sum(m)

###############################################################################
"""
Solution 3: straightforward.  Scan ahead by one char to check when current
char is C, X, or I.
"""
class Solution3:
    def romanToInt(self, s: str) -> int:
        len_s = len(s)
        n = 0
        i = 0

        while i < len_s:
            ch = s[i]

            if ch == 'M':
                n += 1000
            
            elif ch == 'D':
                n += 500

            elif ch == 'C':
                if i + 1 == len_s:
                    n += 100
                elif s[i+1] == 'M':
                    n += 900
                    i += 1
                elif s[i+1] == 'D':
                    n += 400
                    i += 1
                else:
                    n += 100
            
            elif ch == 'L':
                n += 50
            
            elif ch == 'X':
                if i + 1 == len_s:
                    n += 10
                elif s[i+1] == 'C':
                    n += 90
                    i += 1
                elif s[i+1] == 'L':
                    n += 40
                    i += 1
                else:
                    n += 10
            
            elif ch == 'V':
                n += 5
            
            elif ch == 'I':
                if i + 1 == len_s:
                    n += 1
                elif s[i+1] == 'X':
                    n += 9
                    i += 1
                elif s[i+1] == 'V':
                    n += 4
                    i += 1
                else:
                    n += 1

            i += 1

        return n

"""
Solution 3b: same as sol 1, but use ch2 = s[i:i+2] to scan one char ahead.
"""
class Solution3b:
    def romanToInt(self, s: str) -> int:
        len_s = len(s)
        n = 0
        i = 0

        while i < len_s:
            ch = s[i]

            if ch == 'M':
                n += 1000
            
            elif ch == 'D':
                n += 500

            elif ch == 'C':
                ch2 = s[i:i+2]
                if ch2 == 'CM':
                    n += 900
                    i += 1
                elif ch2 == 'CD':
                    n += 400
                    i += 1
                else:
                    n += 100
            
            elif ch == 'L':
                n += 50
            
            elif ch == 'X':
                ch2 = s[i:i+2]
                if ch2 == 'XC':
                    n += 90
                    i += 1
                elif ch2 == 'XL':
                    n += 40
                    i += 1
                else:
                    n += 10
            
            elif ch == 'V':
                n += 5
            
            elif ch == 'I':
                ch2 = s[i:i+2]
                if ch2 == 'IX':
                    n += 9
                    i += 1
                elif ch2 == 'IV':
                    n += 4
                    i += 1
                else:
                    n += 1

            i += 1

        return n

###############################################################################
"""
Solution 4: count chars and adjust.

Slow because of the linear searches for 'CM', etc.
"""
class Solution4:
    def romanToInt(self, s: str) -> int:
        n = 0
        
        d = collections.defaultdict(int)
        for ch in s:
            d[ch] += 1

        n = d['M']*1000 + d['D']*500 + d['C']*100 + d['L']*50 + d['X']*10 + d['V']*5 + d['I']

        if 'CM' in s:
            n -= 200 # from MC=1100 to CM=900

        if 'CD' in s:
            n -= 200 # from DC=600 to CD=400

        if 'XC' in s:
            n -= 20 # from CX=110 to XC=90

        if 'XL' in s:
            n -= 20 # from LX=60 to XL=40

        if 'IX' in s:
            n -= 2 # from XI=11 to IX=9

        if 'IV' in s:
            n -= 2 # from VI=6 to IV=4

        return n

###############################################################################

if __name__ == "__main__":
    def test(s, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\ns = {s}")
        
        res = sol.romanToInt(s)

        print(f"\nres = {res}\n")
        

    #sol = Solution() # use values dict with 7 symbols
    #sol = Solution1b() # use values dict with 13 symbols, some length 2
    
    sol = Solution2() # use values dict, compare adjacent values
    sol = Solution2b() # same, but use map() and sum()

    #sol = Solution3() # straightforward; scan ahead one char when needed
    #sol = Solution3b() # same, but scan ahead using s[i:i+2]

    #sol = Solution4() # count chars and adjust

    comment = "LC ex1; answer = 3"
    s = "III"
    test(s, comment)

    comment = "LC ex2; answer = 4"
    s = "IV"
    test(s, comment)

    comment = "LC ex3; answer = 9"
    s = "IX"
    test(s, comment)

    comment = "LC ex4; answer = 58"
    s = "LVIII"
    test(s, comment)

    comment = "LC ex5; answer = 1994"
    s = "MCMXCIV"
    test(s, comment)
