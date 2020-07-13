"""
190. Reverse Bits
Easy

Reverse bits of a given 32 bits unsigned integer.

Example 1:

Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000

Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

Example 2:

Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111

Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.

Note:

Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.

In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above the input represents the signed integer -3 and the output represents the signed integer -1073741825.

Follow up:

If this function is called many times, how would you optimize it?
"""


"""
dcp161
LC190 easy

This problem was asked by Facebook.

Given a 32-bit integer, return the number with its bits reversed.

For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000, return 0000 1111 0000 1111 0000 1111 0000 1111.
"""

# Clarify whether to return a number in decimal or binary form.

###############################################################################
"""
Solution: use bin() and int().
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n)[2::]
        s = s[::-1] + '0' * (32 - len(s))
        
        return int(s, base=2)

###############################################################################
"""
Solution 2: use format string and int().
"""
class Solution2:
    def reverseBits(self, n: int) -> int:
        return int(f"{n:032b}"[::-1], base=2)

"""
Solution 2b: use format() and int().
"""
class Solution2b:
    def reverseBits(self, n: int) -> int:
        #s = format(n, '032b')
        s = "{:032b}".format(n)
        #s = f"{n:032b}"

        return int(s[::-1], base=2)

###############################################################################
"""
Solution 3: use bit manipulation.

Shift the result to the left one position at a time, and shift the input
to the right one position at a time.
"""
class Solution3:
    def reverseBits(self, n: int) -> int:
        r = 0

        for _ in range(32):
            r = (r << 1) | (n & 1)
            n >>= 1

        return r

"""
Solution 3b: same, but use + and % instead of | and &.
"""
class Solution3b:
    def reverseBits(self, n: int) -> int:
        r = 0

        for _ in range(32):
            r = (r << 1) + (n % 2)
            n >>= 1

        return r

"""
Solution 3c: same, but don't shift the result directly. 
Instead, shift the new bit (n & 1) to the correct position before
OR'ing to the result.

"""
class Solution3c:
    def reverseBits(self, n: int) -> int:
        r = 0

        for pos in range(31, -1, -1):
            r |= (n & 1) << pos
            n >>= 1

        return r

"""
Solution 3d: same, but don't shift the result directly. 
Instead, shift the addend (the new bit n % 2) to the correct position 
before adding to the result.

Same as sol 3c, but use + and % instead of | and &.
"""
class Solution3d:
    def reverseBits(self, n: int) -> int:
        r = 0

        for pos in range(31, -1, -1):
            r += (n % 2) << pos
            n >>= 1

        return r

###############################################################################

if __name__ == "__main__":
    def test(n, comment=None):
        print("="*80)
        if comment:
            print(comment, "\n")

        print(f"n = {n}")

        res = sol.reverseBits(n)

        print(f"\nresult = {res}\n")


    #sol = Solution()  # use bin() and int()
    
    #sol = Solution2() # use format string and int()
    #sol = Solution2b() # use format() and int()
    
    sol = Solution3() # use bit manip; use | and &
    #sol = Solution3b() # same, but use + and % instead of | and &.
    
    #sol = Solution3c() # don't shift result directly; use | and &
    #sol = Solution3d() # don't shift result directly; use + and %

    comment = "LC ex1; answer = 964176192"
    n = 43261596
    test(n, comment)

    comment = "LC ex2; answer = 3221225471"
    n = 4294967293
    test(n, comment)

    comment = "; answer = 398458880"
    n = 1000
    test(n, comment)

    comment = "; answer = 0"
    n = 0
    test(n, comment)

    comment = "; answer = 2147483648"
    n = 1
    test(n, comment)
