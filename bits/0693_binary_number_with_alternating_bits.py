"""
693. Binary Number with Alternating Bits
Easy

Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101

Example 2:
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.

Example 3:
Input: 11
Output: False
Explanation:
The binary representation of 11 is: 1011.

Example 4:
Input: 10
Output: True
Explanation:
The binary representation of 10 is: 1010.
"""

import re

###############################################################################
"""
Solution 1: check bits one by one.

Runtime: 28 ms, faster than 59.22% of Python3 online submissions
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        last = n & 1
        n >>= 1

        while n:
            if n & 1 == last:
                return False
            
            last = n & 1
            n >>= 1

        return True

###############################################################################
"""
Solution 2: assume 32-bit integers.  Check against all 32-bit alternating
patterns.

Runtime: 20 ms, faster than 96.69% of Python3 online submissions
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
    def hasAlternatingBits(self, n: int) -> bool:
        pattern = 0b10101010_10101010_10101010_10101010

        while pattern:
            if n == pattern:
                return True
            pattern >>= 1

        return False

###############################################################################
"""
Solution 3: Check if n and (n >> 1) have different bits in every position.

(1) n ^ (n >> 1) has all set bits after a certain point
(2) n ^ (n >> 1) + 1 is a power of two, ie, has exactly one set bit.

Side note: This inspires the formula:
n + n//2 + 1 = 2**p

For even n:
2n + n + 2 = 2**(p+1)
3n + 2 = 2**(p+1)
3n = 2**(p+1) - 2 = 2(2**p - 1)
n = 2(2**p - 1) / 3

For odd n:
2n + (n-1) + 2 = 2**(p+1)
3n + 1 = 2**(p+1)
n = (2**(p+1) -1) / 3
This is just half of the formula for even n+1.

p = 0: n = 0
p = 2: n = 2        p = 1: n = 1
p = 4: n = 10       p = 3: n = 5
p = 6: n = 42       p = 5: n = 21
p = 8: n = 170      p = 7: n = 85
"""
class Solution3:
    def hasAlternatingBits(self, n: int) -> bool: # n > 0
        k = n ^ (n >> 1)
        return k & (k + 1) == 0 # check if k+1 is a power of 2

"""
Solution 3b: shift right twice, then XOR to cancel bits.  
If n is alternating, we're left with a single set bit, ie, a power of 2.
"""
class Solution3b:
    def hasAlternatingBits(self, n: int) -> bool: # n > 0
        k = n ^ (n >> 2)
        return k & (k - 1) == 0

###############################################################################
"""
Solution 4: Iteratively decompose n into last bit and rest of bits.  Check 
if last bit is same as last bit of rest of bits.
"""
class Solution4:
    def hasAlternatingBits(self, n: int) -> bool:
        n, last_bit = divmod(n, 2)
        
        while n:
            if last_bit == n & 1:
                return False

            n, last_bit = divmod(n, 2)

        return True

###############################################################################
"""
Solution 5: Convert to string using bin() and check for '11' and '00'.
"""
class Solution5:
    def hasAlternatingBits(self, n: int) -> bool:
        bits = bin(n)
        return '00' not in bits and '11' not in bits

"""
Solution 5b: Convert to string using bin() and checking adjacent bits.
"""
class Solution5b:
    def hasAlternatingBits(self, n: int) -> bool:
        bits = bin(n)
        return all( bits[i] != bits[i+1] for i in range(len(bits) - 1) )

###############################################################################
"""
Solution 6: positive regex on bin(n).
"""
class Solution6:
    def hasAlternatingBits(self, n: int) -> bool:
        return re.search(r"^0b(10)*1?$", bin(n)) != None
        
"""
Solution 6b: negative regex on bin(n).
"""
class Solution6b:
    def hasAlternatingBits(self, n: int) -> bool:
        return not re.search(r"00|11", bin(n))

"""
Solution 6c: regex on bin(n ^ (n >> 1)) to check that it ends in all 1's.
"""
class Solution6c:
    def hasAlternatingBits(self, n: int) -> bool:
        k = n ^ (n >> 1)
        return re.search(r"^0b1+$", bin(k)) != None

###############################################################################

if __name__ == "__main__":
    def test(n, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(f"\nn = {n}")
        
        res = sol.hasAlternatingBits(n)
        print(f"\nres = {res}")


    sol = Solution() # check bit by bit
    sol = Solution2() # check if n is equal to any 32-bit pattern
    
    sol = Solution3() # check if (n ^ (n >> 1)) + 1 is power of 2
    sol = Solution3b() # check if n ^ (n >> 2) is power of 2

    sol = Solution4() # decompose into last bit and rest of bits using divmod()
    
    sol = Solution5() # use bin()  and check for '11' and '00'
    sol = Solution5b() # use bin() and check adjacent bits

    sol = Solution6() # positive regex
    #sol = Solution6b() # negative regex
    sol = Solution6c() # regex on bin(n & (n >> 1)) to check it ends in all 1's

    comment = "LC ex1; answer = True"
    n = 5
    test(n, comment)
    
    comment = "LC ex1; answer = False"
    n = 7
    test(n, comment)
    
    comment = "LC ex1; answer = False"
    n = 11
    test(n, comment)
    
    comment = "LC ex1; answer = True"
    n = 10
    test(n, comment)
    
    comment = "answer = False"
    n = 6
    test(n, comment)
