"""
970. Powerful Integers
Easy

Given two positive integers x and y, an integer is powerful if it is equal to x^i + y^j for some integers i >= 0 and j >= 0.

Return a list of all powerful integers that have value less than or equal to bound.

You may return the answer in any order.  In your answer, each value should occur at most once.

Example 1:

Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
Explanation: 
2 = 2^0 + 3^0
3 = 2^1 + 3^0
4 = 2^0 + 3^1
5 = 2^1 + 3^1
7 = 2^2 + 3^1
9 = 2^3 + 3^0
10 = 2^0 + 3^2

Example 2:

Input: x = 3, y = 5, bound = 15
Output: [2,4,6,8,10,14] 

Note:

1 <= x <= 100
1 <= y <= 100
0 <= bound <= 10^6
"""

from typing import List

###############################################################################
"""
Solution 1:

"""
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound < 2:
            return []

        if x == 1 and y == 1:
            return [2]
        
        if x > y:
            x, y = y, x
            
        if x == 1:
            s = set()
            n = 1

            while n <= bound:
                s.add(1 + n)
                n *= y

            return list(s)
        
        s = set()
        n = 1
        
        while n <= bound:    
            q = 1

            while n + q <= bound:
                s.add(n + q)
                q *= y
        
            n *= x
            
        return list(s)

###############################################################################
"""
Solution 2: more concise than sol 1, but includes more "if" statements
within loops.

"""
class Solution2:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        s = set()
        p = 1

        while p <= bound:
            q = 1

            while q <= bound:
                if p + q <= bound:
                    s.add(p + q)

                if y == 1:
                    break
        
                q *= y

            if x == 1:
                break
            
            p *= x

        return list(s)
