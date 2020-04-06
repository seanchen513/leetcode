"""
1017. Convert to Base -2
Medium

Given a number N, return a string consisting of "0"s and "1"s that represents its value in base -2 (negative two).

The returned string must have no leading zeroes, unless the string is "0".

Example 1:

Input: 2
Output: "110"
Explantion: (-2) ^ 2 + (-2) ^ 1 = 2

Example 2:

Input: 3
Output: "111"
Explantion: (-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 = 3

Example 3:

Input: 4
Output: "100"
Explantion: (-2) ^ 2 = 4

Note:

0 <= N <= 10^9
"""

###############################################################################
"""
Solution: iteration.

Suppose n = a3*(-2)^3 + a2*(-2)^2 + a1*(-2)^1 + a0*(-2)^0.

Taking n & 1, we get a0.

Then right shift by 1 gives:
-a3*(-2)^2 - a2*(-2)^1 - a1

""" 
class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"

        s = ""

        while n != 0:
            if n % 2 == 1:
                s = '1' + s
                n -= 1
            else:
                s = '0' + s

            #n //= -2
            n = -(n >> 1)

        return s

"""
Solution 1b: 
""" 
class Solution1b:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"

        s = ""

        while n:
            s = str(n & 1) + s

            #n = (n-1) // -2
            n = -(n >> 1)

        return s

###############################################################################
"""
Solution 2: recursive.
"""
class Solution2:
    def baseNeg2(self, n: int) -> str:
        def rec(n):
            if n == 0:
                return ""

            s = ""

            if n % 2 == 1:
                s += '1'
                n -= 1
            else:
                s += '0'

            return rec(n // -2) + s
            #return rec(-(n >> 1)) + s

        if n == 0:
            return "0"
        
        return rec(n)

"""
Solution 2b:
"""
class Solution2b:
    def baseNeg2(self, n: int) -> str:
        def rec(n):
            if n == 0:
                return ""

            return rec((n-1) // -2) + str(n & 1)
            #return rec(-(n >> 1)) + str(n & 1)

        if n == 0:
            return "0"
        
        return rec(n)


"""
pos value
0   (-2)^0 = 1
1   (-2)^1 = -2
2   (-2)^2 = 4
3   (-2)^3 = -8

4   (-2)^4 = 16
5   (-2)^5 = -32
6   (-2)^6 = 64
7   (-2)^7 = -128

8   (-2)^8 = 256

n   rep
1   001

2   110     4 - 2
3   111     4 - 2 + 1
4   100     
5   101     4 + 1

6   1_1010   16 - 8 - 2
8   1_1000   16 - 8
10  1_1110   16 - 8 + 4 - 2
12  1_1100   16 - 8 + 4
14  1_0010   16 - 2
16  1_0000        
18  1_0110   16 + 4 - 2
20  1_0100   16 + 4

22  110_1010  64 - 32 - 8 - 2
24  110_1000  64 - 32 - 8
26              
28  
30  110_0010  64 - 32 - 2
32  110_0000  64 - 32

48  111_0000  64 - 32 + 16

"""
            
###############################################################################

if __name__ == "__main__":
    def test(low, high, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\nlow = {low}")
        print(f"high = {high}")

        res = sol.baseNeg2(n)
        
        print(f"\nres = {res}\n")


    sol = Solution() 

    comment = "LC ex1; answer = 110"
    n = 2
    test(n, comment)
                
    comment = "LC ex1; answer = 111"
    n = 3
    test(n, comment)

    comment = "LC ex1; answer = 100"
    n = 4
    test(n, comment)

    comment = "LC TC; answer = 0"
    n = 0
    test(n, comment)
