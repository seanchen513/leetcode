"""
60. Permutation Sequence
Medium

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"

Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.

Example 1:

Input: n = 3, k = 3
Output: "213"

Example 2:

Input: n = 4, k = 9
Output: "2314"
"""

import math

###############################################################################
"""
Solution: iteration.

O(n^2) time: for deleting elements from the "digits" array each iteration.
O(n) extra space: for output and for "digits" array.
"""
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        #digits = list(map(str, range(1, n+1)))
        digits = [str(i) for i in range(1, n+1)]
        res = []

        #f = math.factorial(n)
        f = 1
        for i in range(1, n+1):
            f *= i

        k -= 1 # make k 0-based count

        while len(digits) > 0: # while n > 0
            f //= len(digits) # f //= n 
            
            idx = k // f
            res.append(digits[idx])
            del digits[idx]

            k -= idx * f
            #n -= 1

        return ''.join(res)

"""
Solution 1b: almost same as sol 1, but use d = digits[k // f] instead of 
idx = k // f.

"""
class Solution1b:
    def getPermutation(self, n: int, k: int) -> str:
        #digits = list(map(str, range(1, n+1)))
        digits = [str(i) for i in range(1, n+1)]
        res = []

        f = math.factorial(n)
        k -= 1 # make k 0-based count

        while len(digits) > 0: # while n > 0
            f //= len(digits) # f //= n 
            
            d = digits[k // f]

            res.append(d)
            digits.remove(d)

            k %= f # k -= (k // f) * f
            #n -= 1

        return ''.join(res)

###############################################################################
"""
Solution 2: recursion

n = 4
k = 9
n! = 4! = 24

3! < 9 < 4!

9 - 3! = 3

1234
1243
1324
1342
1423
1432

2134
2143
2314

2
n = 3
k = 3
idx = k // (n-1)! = 3 // 2! = 3 // 2 = 1
digits = [1,3,4]
d = 3

23
n = 2
k = 1
idx = 1 // 1! = 1
digits = [1,4]

Runtime: 20 ms, faster than 98.66% of Python3 online submissions
Memory Usage: 13.8 MB, less than 8.33% of Python3 online submissions
"""
class Solution2:
    def getPermutation(self, n: int, k: int) -> str:
        def rec(k):
            if len(digits) == 1:
                res.append(digits[0])
                return 

            # first call: len(digits) = n, f = (n-1)!
            f = math.factorial(len(digits) - 1) # (n-1)! initially
            d = digits[k // f]

            res.append(d)
            digits.remove(d)

            rec(k % f)

        #digits = list(map(str, range(1, n+1)))
        digits = [str(i) for i in range(1, n+1)]
        res = []

        rec(k-1) # make k 0-based count

        return ''.join(res)

"""
Solution 2b: same as sol 1, but pass f as a parameter, and use idx = k // f.
"""
class Solution2b:
    def getPermutation(self, n: int, k: int) -> str:
        def rec(k, f):
            if len(digits) == 1:
                res.append(digits[0])
                return 

            # first call: len(digits) = n, f = n! before this division below
            f //= len(digits)
            
            idx = k // f

            res.append(digits[idx])
            del digits[idx]

            rec(k % f, f)

        #digits = list(map(str, range(1, n+1)))
        digits = [str(i) for i in range(1, n+1)]
        res = []
        f = math.factorial(n)

        rec(k-1, f) # make k 0-based count

        return ''.join(res)

###############################################################################

if __name__ == "__main__":
    def test(arr, k, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\nn = {n}")
        print(f"k = {k}")

        res = sol.getPermutation(n, k)

        print(f"\nres = {res}\n")


    sol = Solution() # iteration
    #sol = Solution1b() #
    
    #sol = Solution2() # recursion
    #sol = Solution2b()

    comment = "LC ex1; answer = 213"
    n = 3
    k = 3
    test(n, k, comment)

    comment = "LC ex2; answer = 2314"
    n = 4
    k = 9
    test(n, k, comment)

    comment = "; answer = 2341"
    n = 4
    k = 10
    test(n, k, comment)

    comment = "; answer = 845697321"
    n = 9 # 9! = 362880
    k = 300000
    test(n, k, comment)
