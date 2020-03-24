"""
504. Base 7
Easy

Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"

Example 2:
Input: -7
Output: "-10"

Note: The input will be in range of [-1e7, 1e7].
"""

###############################################################################
"""
Solution: use string concatenation.
"""
class Solution:
    def convertToBase7(self, n: int) -> str:
        if n == 0:
            return "0"
        
        neg = True if n < 0 else False
        n = -n if n < 0 else n
        s = ""
        
        while n:
            s += str(n % 7)
            n //= 7
            
        return "-" + s[::-1] if neg else s[::-1]

"""
Solution 1b: rewrite of sol 1.
"""
class Solution1b:
    def convertToBase7(self, num: int) -> str:
        n = abs(num)
        s = ""

        while n:
            s = str(n % 7) + s
            n //= 7

        return "-" * (num < 0) + s or "0"

###############################################################################
"""
Solution 2: use list and join().
"""
class Solution2:
    def convertToBase7(self, n: int) -> str:
        if n == 0:
            return "0"
        
        neg = True if n < 0 else False
        n = -n if n < 0 else n
        s = []
        
        while n:
            s.append(str(n % 7))
            n //= 7
            
        #s = list(map(str, s))
            
        if neg:
            s.append("-")
        
        return ''.join(reversed(s))

###############################################################################
"""
Solution 3: recursion
"""
class Solution3:
    def convertToBase7(self, n: int) -> str:
        if n < 0:
            return "-" + self.convertToBase7(-n)
        
        if n < 7:
            return str(n)

        return self.convertToBase7(n // 7) + str(n % 7)

###############################################################################

if __name__ == "__main__":
    def test(n, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\nn = {n}")

        res = sol.convertToBase7(n)

        print(f"\nres = {res}\n")


    sol = Solution()
    sol = Solution1b()

    #sol = Solution2()
    sol = Solution3() # recursion

    comment = "LC ex1; answer = 202"
    n = 100
    test(n, comment)

    comment = "LC ex2; answer = -10"
    n = -7
    test(n, comment)

    comment = "answer = 2626"
    n = 1000
    test(n, comment)
