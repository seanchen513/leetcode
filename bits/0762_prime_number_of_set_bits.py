"""
62. Prime Number of Set Bits in Binary Representation
Easy

Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a prime number of set bits in their binary representation.

(Recall that the number of set bits an integer has is the number of 1s present when written in binary. For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.)

Example 1:

Input: L = 6, R = 10
Output: 4

Explanation:
6 -> 110 (2 set bits, 2 is prime)
7 -> 111 (3 set bits, 3 is prime)
9 -> 1001 (2 set bits , 2 is prime)
10->1010 (2 set bits , 2 is prime)

Example 2:

Input: L = 10, R = 15
Output: 5

Explanation:
10 -> 1010 (2 set bits, 2 is prime)
11 -> 1011 (3 set bits, 3 is prime)
12 -> 1100 (2 set bits, 2 is prime)
13 -> 1101 (3 set bits, 3 is prime)
14 -> 1110 (3 set bits, 3 is prime)
15 -> 1111 (4 set bits, 4 is not prime)

Note:

L, R will be integers L <= R in the range [1, 10^6].
R - L will be at most 10000.
"""

###############################################################################
"""
Solution: brute force

L and R can be at most 10**6, which has 20 bits. The largest prime number
less than 20 is 19.

O(D) time, where D = R - L

O(D log D) time in bit complexity model since counting bits for one integer
takes O(log D) time.

O(1) extra space

Runtime: 540 ms, faster than 42.94% of Python3 online submissions
Memory Usage: 13 MB, less than 87.50% of Python3 online submissions
"""
class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        def prime_set_bits(n):
            count = 0

            while n:
                count += 1
                n &= n - 1
                
            return count in primes
        
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        
        return sum(prime_set_bits(i) for i in range(L, R+1))
            
###############################################################################
"""
Solution 2: use bin() and string.count().

Runtime: 184 ms, faster than 86.68% of Python3 online submissions
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}

        return sum(bin(i).count('1') in primes for i in range(L, R+1))

###############################################################################
"""
Solution 3: bit shift with 665772 instead of checking prime set.

0b00000010100010101100 is the bit wise representation of 665772.
The set bits are exactly the bits in prime positions (2,3,5,...,19).
(0-based positions, reading from the right).

https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/discuss/113232/665772
"""
class Solution3:
    def countPrimeSetBits(self, L, R):
        return sum(665772 >> bin(i).count('1') & 1 for i in range(L, R+1))

###############################################################################

if __name__ == "__main__":
    def test(L, R, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\nL, R = {L}, {R}")

        res = sol.countPrimeSetBits(L, R)

        print(f"\nres = {res}\n")


    sol = Solution() # brute force
    sol = Solution2() # use bin() and string.count()
    sol = Solution3() # bit shift 665772

    comment = "LC ex1; answer = 4"
    L = 6
    R = 10
    test(L, R, comment)

    comment = "LC ex2; answer = 5"
    L = 10
    R = 15
    test(L, R, comment)

    comment = "answer = 78"
    L = 1
    R = 128
    test(L, R, comment)
