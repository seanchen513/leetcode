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
Given:
n = 4
k = 9
n! = 4! = 24
We want to find the 9th permutation out of 24.

1234
1243
1324
1342
1423
1432

2134
2143
2314 -- This is the answer.

Notice how the first 6 perms have "1" for the first digit.
The next group of 6 perms have "2" for the first digit, etc.

Within the first group of 6 perms, the perms are grouped by their 2nd digit,
and there are 3 choices for the 2nd digit (2, 3, or 4).
Each of these subgroups have size 2. A similar pattern holds in the other
groups of 6 perms, but with different choices for the 2nd digit.

Within each group of size 2 (share 1st digit and 2nd digit), the perms
are grouped by their 3rd digit, and there are 2 choices for the 3rd digit. 
Each of these subgroups have size 1.

This motivates the factorial number system...

### Algo:

Input k is a 1-based position, but we want to work with 0-based indices,
so adjust k down by 1.

# Round 1: n = 4, k = 8 (adjusted)
# res = [], digits = [1,2,3,4]

Initialize ordered digits = [1,2,3,4].

Compute which group the kth perm is in, ie, what the first digit should be.
These groups have size (n-1)! = 3! = 6.

idx = k // (n-1)!
= 8 // 6 = 1 (in a 0-based index system)

So the 8th perm is in group 1 (0-based).
The first digit is digits[idx] = digits[1] = 2.

We remove "2" from the digits list, so now digits = [1,3,4].
We skipped over idx * (n-1)! number of perms, so now we've reduced the
problem to finding the remaining digits of the kth permutation.

new n = n - 1 = 4 - 1 = 3
new k = k - idx * (n-1)! = 8 - 1 * 3! = 2

# Round 2: n = 3, k = 2
# res = [2], digits = [1,3,4]

Compute which group the kth perm is in, ie, what the second digit should be.
These groups have size (n-1)! = 2! = 2.

idx = k // (n-1)!
= 2 // 2 = 1 (in a 0-based index system)

So the kth perm is in the group 1 (0-based).
The first digit is digits[idx] = digits[1] = 3.
We remove "3" from the digits list, so now digits = [1,4].

new n = n - 1 = 3 - 1 = 2
new k = k - idx * (n-1)! = 2 - 1 * 2! = 0

# Round 3: n = 2, k = 0
# res = [2,3], digits = [1,4]

...

"""

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
