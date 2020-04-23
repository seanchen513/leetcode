"""
201. Bitwise AND of Numbers Range
Medium

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4

Example 2:

Input: [0,1]
Output: 0
"""

###############################################################################
"""
Solution: another way to find common leftmost part of m and n.

https://leetcode.com/problems/bitwise-and-of-numbers-range/discuss/56721/2-line-Solution-with-detailed-explanation

"""
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m < n:
            n &= n - 1 # unset R-most 1-bit in n

        return n

###############################################################################
"""
Solution 2: find common leftmost part of m and n.

If m != n, then they have different parity and the final bits are different.
So shift both m and down to right to remove final bits.
Keep going until m == n.
This happens when we reached the common left part of m and n.
Then we shift back to the left by the same amount we shifted to the right.

Another way to look at it:
Traversing from m to n, the bits keep changing, with the bits further to
the right changing more frequently. The bits that change cause the AND of
the range to have a 0 at the corresponding positions. A bit doesn't change
unless all the bits to its right have changed. So the only 1-bits in the
AND of the range are the leftmost bits that m and n share.

O(log max(m,n)) time: worst case is when both m and n need to be shifted to 0.
O(1) extra space

"""
class Solution2:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        k = 0

        while m != n:
            k += 1
            m >>= 1
            n >>= 1

        return m << k

"""
Solution 2b: recursive version.
"""
class Solution2b:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if n > m: # n != m
            return self.rangeBitwiseAnd(m >> 1, n >> 1) << 1
        
        return m

###############################################################################
"""
Solution 3:

Any range that includes 0 has answer 0.
Any range that includes both 1 and 2 has answer 0.

Example: contains two different powers of 2, so answer is 0.

2 = 0b0010
3 = 0b0011
4 = 0b0100

Largest range that contains only one power of 2 is like [9, 31].
The only power of 2 in [2^k + 1, 2^(k+2) - 1] is 2^(k+1).
Smallest example is [1, 2].

Example of range that contains only one power of 2: [9, 31]
9  = 0b00_1001
10 = 0b00_1010
16 = 0b01_0000
31 = 0b01_1111
Answer is 0.

15 & 16 = 0b0_1111 & 0b1_0000 = 0

*** If a range includes a power of 2 and the number just before it,
then the answer is 0.
Suppose p is a power of 2 in the range and its only 1-bit is the kth bit.
Then p-1 has kth bit 0. So p & (p-1) = 0. So the bitwise AND or the range is 0.

We can tell a range is like this if NOT all the numbers in it share the same
L-most 1-bit. In particular, we can check the first and last number.

Assume if a range includes a power of 2, then it is the only power of 2 in the
range, and that the range begins with that power of 2.
That is, assume all numbers in the range share the same L-most 1-bit.

This 1-bit corresponds to the largest power of 2 that is <= m.
We can then subtract m from each number in the range, and recursively
calculate for the new range.

Example: range [5, 7]
5 = 0b101
6 = 0b110
7 = 0b111

They all share the same L-most 1-bit, which corresponds to 4.
Biggest power of 2 that is < m = 5 is 4.

Subtract 4 from all to get new range [1, 3]:
1 = 0b001
2 = 0b010
3 = 0b011

They do not share the same L-most 1-bit, so the bitwise AND for this range is 0.

Combining answers give 4 + 0 = 4.

"""
class Solution3:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        def left_bit(n): # return position of leftmost 1-bit (-1 for n=0)
            count = -1
            while n:
                n >>= 1
                count += 1

            return count

        if m == 0:
            return 0
        # if m == 1:
        #     return int(n == 1)

        k = left_bit(m)
        if k != left_bit(n):
            return 0

        res = 1 << k

        return res | self.rangeBitwiseAnd(m - res, n - res)

###############################################################################
"""
Solution 4: brute force

TLE
"""
class Solution4:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        s = m
        
        for i in range(m+1, n+1):
            s &= i
            if s == 0:
                return 0
        
        return s

###############################################################################

if __name__ == "__main__":
    def test(m, n, comment=None):       
        print("="*80)
        if comment:
            print(comment)

        print(f"\nm = {m}")
        print(f"n = {n}")
        
        res = sol.rangeBitwiseAnd(m, n)

        print(f"\nresult = {res}\n")

    sol = Solution() # find common L-most part by unsetting R-most 1-bit of n until n < m
    
    #sol = Solution2() # find common L-most part by checking m != n and doing >> 1
    #sol = Solution2b() # recursive version
    
    #sol = Solution3() # use fact that if p is power of 2, then p & (p-1) = 0.

    #sol = Solution4() # brute force; TLE

    comment = 'LC ex1; answer = 4'
    m = 5
    n = 7
    test(m, n, comment)

    comment = 'LC ex2; answer = 0'
    m = 0
    n = 1
    test(m, n, comment)

    comment = 'LC TC; answer = 2'
    m = 2
    n = 2
    test(m, n, comment)

    comment = 'LC TC; answer = 0'
    m = 2
    n = 4
    test(m, n, comment)

    comment = '; answer = 32'
    m = 33
    n = 63
    test(m, n, comment)

    comment = "LC TC; answer = 0"
    m = 600000000
    n = 2147483645
    test(m, n, comment)
