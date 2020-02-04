"""
263. Ugly Number
Easy

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3

Example 2:

Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2

Example 3:

Input: 14
Output: false 
Explanation: 14 is not ugly since it includes another prime factor 7.
Note:

1 is typically treated as an ugly number.
Input is within the 32-bit signed integer range: [−2**31,  2**31 − 1].
"""
###############################################################################

class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
           return False
        
        while n % 5 == 0:
            n //= 5

        while n % 3 == 0:
            n //= 3
        
        #while n % 2 == 0:
        #    n //= 2
        
        while n & 1 == 0:
            n >>= 1
            
        return n == 1

###############################################################################

if __name__ == "__main__":
    def test(n=100):
        solutions = [Solution()]

        res = []
        for s in solutions:
            res += [s.isUgly(n)]

        print("="*80)
        print(f"Testing results of solutions for n = {n}\n")
        print(res)


    #test(8*9*5)
    test(2**31 - 1) # 2,147,483,647
