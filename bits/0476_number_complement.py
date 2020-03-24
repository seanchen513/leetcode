"""
476. Number Complement
Easy

Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Example 1:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
 
Example 2:

Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

Note:

The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/
"""

import math

###############################################################################
"""
Solution: use bit manipulation. Flip bit by bit w/ no branching, and by
XOR'ing with mask.
"""
class Solution:
    def findComplement(self, num: int) -> int:
        x = num
        k = 1 # mask 

        while num:
            x ^= k # flip bit where mask k has set bit

            num >>= 1
            k <<= 1
            
        return x

"""
Solution 1b: flip bit by bit. Uses branching ("if" statement) and OR'ing with
mask.
"""
class Solution1b:
    def findComplement(self, num: int) -> int:
        x = 0
        k = 1 # mask to set bit position

        while num:
            if num & 1 == 0:
                x |= k

            num >>= 1
            k <<= 1
            
        return x

###############################################################################
"""
Solution 2: compute bit length and XOR with bit mask of all 1s
"""
class Solution2:
    def findComplement(self, num: int) -> int:
        n_bits = 0
        k = num
        while k:
            n_bits += 1
            k >>= 1

        #n_bits = math.floor(math.log2(num)) + 1
        #n_bits = num.bit_length()

        mask = (1 << n_bits) - 1

        return mask ^ num
            
###############################################################################
"""
Solution 3: compute bit length and use it to form bit mask of all 1s.
Subtract num from it.

Using int.bit_length() is just one way to compute bit length.
"""
class Solution3:
    def findComplement(self, num: int) -> int:
        return (1 << num.bit_length()) - 1 - num

###############################################################################
"""
Solution 4: highestOneBit OpenJDK algo from Hacker's Delight.

Idea is to create the bit mask of all 1s by propagating the highest 1-bit
into the lower ones.
"""
class Solution4:
    def findComplement(self, num: int) -> int:
        mask = num

        mask |= (mask >> 1)
        mask |= (mask >> 2)
        mask |= (mask >> 4)
        mask |= (mask >> 8)
        mask |= (mask >> 16)

        return mask ^ num

###############################################################################
"""
Solution 5: form bit mask of all 1s by repeatedly right-shifting 1 until
it's greater than num.
"""
class Solution5:
    def findComplement(self, num: int) -> int:
        i = 1
        while i <= num:
            i <<= 1
        
        return (i - 1) ^ num

###############################################################################
"""
Solution 5: use bin() or formatted string, and int().
"""
class Solution6:
    def findComplement(self, num: int) -> int:
        s = f"{num:b}" # bin(s)[2:]
        t = ""

        for c in s:
            if c == "0":
                t += "1"
            else:
                t += "0"

        return int(t, 2)
       
###############################################################################

if __name__ == "__main__":
    def test(n, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"n = {n}")

        res = sol.findComplement(n)

        print(f"\nres = {res}\n")


    sol = Solution() # flip bit by bit, and XOR with masks
    #sol = Solution1b() # flip bit by bit, and OR with masks (use branching)
    
    sol = Solution2() # compute bit length and XOR with bit mask of all 1s
    sol = Solution3() # form mask of all 1s using int.bit_length()
    sol = Solution4() # form mask of all 1s via Hacker's Delight
    sol = Solution5() # form mask of all 1s by repeatedly R-shifting 1...
    
    #sol = Solution6() # use bin() or formatted string, and int().
    
    comment = "LC ex1; answer = 2"
    n = 5
    test(n, comment)

    comment = "LC ex2; answer = 0"
    n = 1
    test(n, comment)

    comment = "answer = 510"
    n = 513
    test(n, comment)
