"""
367. Valid Perfect Square
Easy

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true

Example 2:

Input: 14
Output: false
"""

###############################################################################
"""
Solution: binary search

O(log n) time
O(1) extra space
"""
class Solution:
    def isPerfectSquare(self, n: int) -> bool:
        lo = 1
        hi = n

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if mid * mid < n:
                lo = mid + 1
            else:
                hi = mid

        return lo * lo == n

###############################################################################
"""
Solution 2: brute force

O(sqrt(n)) time
O(1) extra space
"""
class Solution2:
    def isPerfectSquare(self, n: int) -> bool:
        i = 1
        
        while i * i <= n:
            if i * i == n:
                return True
                
            i += 1
        
        return False
                    
"""
Solution 2b: same, but use parity of n to start at 1 or 2, and go by step of 2.

O(sqrt(n)) time
O(1) extra space
"""
class Solution2b:
    def isPerfectSquare(self, n: int) -> bool:
        if n & 1: # odd
            i = 1
        else:
            i = 2
            
        i2 = i*i
            
        while i2 <= n:
            if i2 == n:
                return True
            
            i += 2
            i2 = i*i
        
        return False

###############################################################################

if __name__ == "__main__":
    def test(n, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"n = {n}")

        res = sol.isPerfectSquare(n)

        print(f"\nres = {res}\n")


    sol = Solution() # binary search

    #sol = Solution2() # brute force
    #sol = Solution2b() # same, but step by 2
    

    comment = "LC ex1; answer = True"
    n = 16
    test(n, comment)

    comment = "LC ex2; answer = False"
    n = 14
    test(n, comment)

    comment = "LC ex1; answer = True"
    n = 1
    test(n, comment)
