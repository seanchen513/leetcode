"""
338. Counting Bits
Medium

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]

Example 2:

Input: 5
Output: [0,1,1,2,1,2]

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?

Space complexity should be O(n).

Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
"""

from typing import List

###############################################################################
"""
Solution 1: reduce to smaller case by parity.

Let sb(n) = number of set bits of n.
If n is even, then LSB is 0.  So sb(n) = sb(n//2).
If n is odd, then LSB is 1.  So sb(n) = sb(n//2) + 1.

O(n) time
O(n) extra space for result

Runtime: 68 ms, faster than 99.63% of Python3 online submissions
Memory Usage: 19.8 MB, less than 5.00% of Python3 online submissions
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0]

        for i in range(1, n+1):
            bits.append(bits[i >> 1] + (i & 1))
            
            ### Write in terms of mod instead of bit operations; using "if"
            # if i % 2 == 0: # even
            #     bits.append(bits[i//2])
            # else: # odd
            #     bits.append(bits[i//2] + 1)

        return bits

"""
Solution 1b: reduce to smaller case by unsetting last set bit.

O(n) time
O(n) extra space for result

Runtime: 76 ms, faster than 93.34% of Python3 online submissions for Counting Bits.
Memory Usage: 19.5 MB, less than 5.00% of Python3 online submissions for Counting Bits.
"""
class Solution1b:
    def countBits(self, n: int) -> List[int]:
        bits = [0]*(n+1)

        for i in range(1, n+1):
            bits[i] = bits[i & (i-1)] + 1
            
        return bits

"""
Solution 1c: same as sol 1b, but prefill most of "bits" with 1 to avoid
having to add 1 for each case.
"""
class Solution1c:
    def countBits(self, n: int) -> List[int]:
        bits = [0] + [1]*n

        for i in range(1, n+1):
            bits[i] += bits[i & (i-1)]
            
        return bits

###############################################################################
"""
Solution 2: repeatedly copy list and add 1.

Let sb(n) = number of set bits of n.

If integer k is a power of 2, then sb(k) = 1.

Suppose n is not a power of 2.
Let n = k + (n % k) where k is biggest power of 2 that is less than n.
The set bits of n come from the one set bit of k and the set bits of n % k.

sn(n) = 1 + sb(n % k)

0 = 0000    0
1 = 0001    1
2 = 0010    1
3 = 0011    2

4 = 0100    1
5 = 0101    2
6 = 0110    2
7 = 0111    3

8 = 1000    1
9 = 1001    2
10 = 1010   2
11 = 1011   3

12 = 1100   2
13 = 1101   3
14 = 1110   3
15 = 1111   4

16 = 10000  1
...


1: 01
3: 01 12
7: 0112 1223
15: 0112_1223 1223_2334
31: 0112_1223 1223_2334 1233_2334 2344_3445

O(n) time: each value in result list was copied from another value once
O(n) extra space for result

Runtime: 72 ms, faster than 97.86% of Python3 online submissions
Memory Usage: 19.7 MB, less than 5.00% of Python3 online submissions
"""
class Solution2:
    def countBits(self, n: int) -> List[int]:
        bits = [0]

        while len(bits) <= n:
            #bits += map(lambda x: x+1, bits[:])
            bits += [x+1 for x in bits]

        return bits[:n+1]

"""
Solution 2b: same as sol 2, but half as much adding 1

Runtime: 68 ms, faster than 99.63% of Python3 online submissions
Memory Usage: 19.5 MB, less than 5.00% of Python3 online submissions
"""
class Solution2b:
    def countBits(self, n: int) -> List[int]:
        if n == 0: return [0]
        bits = [0,1]

        while len(bits) <= n:
            last_half = bits[len(bits)//2:]
            bits += last_half + [x+1 for x in last_half]

        return bits[:n+1]

###############################################################################
"""
Solution 3: naive, brute force, popcount

O(kn) time, where k is number of bits in n
O(n) extra space for result

Runtime: 132 ms, faster than 22.72% of Python3 online submissions
Memory Usage: 19.7 MB, less than 5.00% of Python3 online submissions
"""
class Solution3:
    def countBits(self, n: int) -> List[int]:
        def popcount(x):
            count = 0
            while x:
                x &= x - 1 # unset right-most set bit
                count += 1
            return count

        return [popcount(x) for x in range(n+1)]

###############################################################################

if __name__ == "__main__":
    def test(n, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(f"\nn = {n}")
        
        res = sol.countBits(n)
        print(f"\nres = {res}")


    sol = Solution() # reduce to smaller case by parity
    #sol = Solution1b() # reduce to smaller case by unsetting last set bit
    #sol = Solution1c() # same as sol 1b, but prefill "bits" with 1's
    
    #sol = Solution2() # use pattern in count of bits; keep copying list and adding 1.
    #sol = Solution2b() # same, but half as much adding 1

    #sol = Solution3() # naive, brute force

    comment = "LC ex1; answer = [0,1,1]"
    n = 2
    test(n, comment)

    comment = "LC ex2; answer = [0,1,1,2,1,2]"
    n = 5
    test(n, comment)

    comment = ""
    n = 32
    test(n, comment)
