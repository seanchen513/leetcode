"""
1256. Encode Number
Medium

Given a non-negative integer num, Return its encoding string.

The encoding is done by converting the integer to a string using a secret function that you should deduce from the following table:

n   f(n)
0   ""
1   "0"
2   "1"
3   "00"
4   "01"
5   "10"
6   "11"
7   "000"

Example 1:

Input: num = 23
Output: "1000"

Example 2:

Input: num = 107
Output: "101100"


Constraints:

0 <= num <= 10^9

"""

###############################################################################
"""
    f(n)    reg
0   ""      0
1   0       1
2   1       10
3   00      11
4   01      100
5   10      101
6   11      110
7   000     111
8   ?       1000

"""

###############################################################################
"""
Solution: recursion to get prefix.

n   f(n)    prefix
0   ""
1   0    
2   1    
3   00      0 ~ 1
4   01      0 ~ 1
5   10      1 ~ 2
6   11      1 ~ 2
7   000     00 ~ 3

f(n) = f((n-1)//2) + (1 if n is even, else 0)

"""
class Solution:
    def encode(self, n: int) -> str:
        if n == 0:
            return ''
        if n == 1:
            return '0'
        if n == 2:
            return '1'

        prefix = self.encode((n-1)//2)

        if n % 2 == 0:
            return prefix + '1'
        else:
            return prefix + '0'

###############################################################################
"""
Solution 2: note that "1" + f(n) = bin(n+1)

n   f(n)    g(n) = "1" + f(n) ~ bin(n+1)
0   ""      1 ~ 1
1   0       10 ~ 2
2   1       11 ~ 3
3   00      100 ~ 4
4   01      101 ~ 5
5   10      110 ~ 6
6   11      111 ~ 7
7   000     1000 ~ 8

"""
class Solution2:
    def encode(self, n: int) -> str:
        return f"{n+1:b}"[1:]
        #return bin(n+1)[3:]

###############################################################################

if __name__ == "__main__":
    def test(n, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\nn = {n}")

        res = sol.encode(n)
        
        print(f"\nres = {res}\n")


    sol = Solution() 
    sol = Solution2() 

    comment = "LC ex1; answer = 1000"
    n = 23
    test(n, comment)

    comment = "LC ex2; answer = 101100"
    n = 107
    test(n, comment)
