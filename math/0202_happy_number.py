"""
202. Happy Number
Easy

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true

Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""
###############################################################################
"""
Solution 1: use set to keep track of seen sums of squares.
"""
class Solution:  
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while 1:           
            n = sum([int(d)**2 for d in str(n)])

            # Can also use looped math to calculate new n
            
            if n in seen:
                return False
            if n == 1:
                return True
            
            seen.add(n)

###############################################################################
"""
Solution 2: use Floyd cycle detection.
"""
class Solution2:  
    def isHappy(self, n: int) -> bool:
        def next(n):
            sum_sq = 0
            while n:
                d = n % 10
                sum_sq += d*d
                n //= 10
            
            return sum_sq

        slow = n
        fast = next(n)

        while slow != fast:
            slow = next(slow)
            fast = next(next(fast))

        return slow == 1
