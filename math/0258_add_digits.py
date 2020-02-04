"""
258. Add Digits
Easy

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 

Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""

"""
Solution 1
"""
class Solution:
    def addDigits(self, n: int) -> int:
        while n > 9:
            n = sum([int(d) for d in str(n)])
            
        return n

"""
Solution 2:

O(1) time: use digit root congruence formula
dr(n) = 1 + (n-1) % 9 for n > 0
dr(n) = 1 + (n-1) % (b-1) for base b

ie, this is a periodic sequence of period b-1=9

https://en.wikipedia.org/wiki/Digital_root#Congruence_formula
"""
class Solution2:
    def addDigits(self, n: int) -> int:
        return 1 + (n - 1) % 9 if n > 0 else 0
