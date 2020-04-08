"""
556. Next Greater Element III
Medium

Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:

Input: 12
Output: 21
 
Example 2:

Input: 21
Output: -1
"""

import itertools

###############################################################################
"""
Solution: 

1. Traverse right to left because we want least significant digit (digits[i])
to change/swap to form the nexter greater number.
2. After finding this digit, we want to swap it with the next greater digit
to the right.
3. We reverse the right part of digits at the end because we know those
digits are in decreasing order, and we want them to be in increasing order.


Example:
           i      j
n      = 9 1 9543 2
         9 2 9543 1 after digit swap
answer = 9 2 13459

Example:
               i j
n      = 91954 2 3
         91954 3 2 after digit swap
answer = 9195432

Example:
           i     j
n      = 9 1 987 210
         9 2 987 110 after digit swap
answer = 9 2 011789

O(d) time, where d is number of digits in n
O(d) extra space: for converting int to list of digits

Runtime: 24 ms, faster than 84.42% of Python3 online submissions
Memory Usage: 13.8 MB, less than 50.00% of Python3 online submissions
"""
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if n < 10:
            return -1

        # list of one-char strings representing digits of n
        digits = list(map(str, str(n)))
        m = len(digits)
        #print(f"digits = {digits}")

        # from right to left, find first index with smaller digit value than previous
        for i in range(m-2, -1, -1):
            if digits[i] < digits[i+1]:
                break

        # looped through all digits and didn't find decreasing digit
        if digits[i] >= digits[i+1]:
            return -1

        # from right to left, find first element (rightmost digit) > digits[i]
        for j in range(m-1, i, -1):
            if digits[j] > digits[i]:
                break

        #print(f"digits before swap: {digits[i], digits[j]}")

        # swap the two digits
        digits[i], digits[j] = digits[j], digits[i]
        
        # reverse the digits after digits[i]
        res = int(''.join(digits[:i+1] + digits[:i:-1]) )

        return res if res < 2**31 else -1

"""
Solution 1b: rewrite
"""
class Solution1b:
    def nextGreaterElement(self, n: int) -> int:
        if n < 10:
            return -1

        # list of one-char strings representing digits of n
        digits = list(map(str, str(n)))
        m = len(digits)

        # from right to left, find first index with smaller digit value than previous
        i = m - 2
        while i >= 0 and digits[i] >= digits[i+1]:
            i -= 1

        # looped through all digits and didn't find decreasing digit
        #if digits[i] >= digits[i+1]:
        if i == -1:
            return -1

        # from right to left, find first element (rightmost digit) > digits[i]
        j = m - 1
        while digits[j] <= digits[i]:
            j -= 1

        # swap the two digits
        digits[i], digits[j] = digits[j], digits[i]
        
        # reverse the digits after digits[i]
        res = int(''.join(digits[:i+1] + digits[:i:-1]) )

        return res if res < (1 << 31) else -1
        #return res if res.bit_length() < 32 else -1
        #return res if len(bin(res)) < 34 else -1 # extra 2 for "0b" in bin()

###############################################################################
"""
Solution 2: use itertools.permutations() to find set of all unique permutations 
of digits. Then do linear scan of set to find answer.

O(d!) time: to find all permutations of digits, where n has d digits.
O(d!) extra space

TLE on:
n = 1999999999
answer = -1
"""
class Solution2:
    def nextGreaterElement(self, n: int) -> int:
        # tuple of one-char strings representing digits of n
        # eg, ['1', '2']
        digits = tuple(map(str, str(n))) 
        
        # set of tuples, each a unique permutation of digits
        s = set(itertools.permutations(digits))

        res = None
        min_diff = float('inf')

        for tup in s:
            if tup > digits and int(''.join(tup)) - n < min_diff:
                min_diff = int(''.join(tup)) - n
                res = tup
        
        return int(''.join(res)) if res else -1

"""
Solution 2b: use itertools.permutations() and set() to find sorted list of all unique
permutations of digits. Then use bisect() to find answer.

TLE on:
n = 1999999999
answer = -1
"""
class Solution2b:
    def nextGreaterElement(self, n: int) -> int:
        # tuple of one-char strings representing digits of n
        # eg, ['1', '2']
        digits = tuple(map(str, str(n))) 
        
        # sorted list of tuples, each a unique permutation of digits
        s = sorted(set(itertools.permutations(digits)))
        
        import bisect
        i = bisect.bisect(s, digits)
        
        return int(''.join(s[i])) if i < len(s) else -1

###############################################################################

if __name__ == "__main__":
    def test(n, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\nn = {n}")

        res = sol.nextGreaterElement(n)

        print(f"\nres = {res}\n")


    sol = Solution() #
    sol = Solution1b() #

    #sol = Solution2() # brute force using itertools.permutations(); linear scan of set
    #sol = Solution2b() # brute force using itertools.permutations(); sort and bisect

    comment = "LC ex1; answer = 21"
    n = 12
    test(n, comment)

    comment = "LC ex1; answer = -1"
    n = 21
    test(n, comment)

    comment = "LC TC; answer = -1"
    n = 11
    test(n, comment)

    comment = "LC TC; answer = -1"
    n = 1
    test(n, comment)
    #exit()

    comment = "LC TC; answer = 13222344"
    n = 12443322
    test(n, comment)

    comment = "LC TC; answer = 123456798"
    n = 123456789
    test(n, comment)

    comment = "LC TC; answer = -1"
    n = 1999999999
    test(n, comment)

    comment = "LC TC; answer = -1" # 2147483674 > 2^31 - 1
    n = 2147483647 # 2^31 - 1, max 32-bit positive signed int
    test(n, comment)

    # comment = "; answer = 123456879"
    # n = 123456798
    # test(n, comment)

    # comment = "; answer = 213456789"
    # n = 198765432
    # test(n, comment)

    comment = "; answer = 9213459"
    n = 9195432
    test(n, comment)

    comment = "; answer = 92011789"
    n = 91987210
    test(n, comment)
