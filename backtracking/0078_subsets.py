"""
78. Subsets
Medium

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

from typing import List
import itertools

###############################################################################
"""
Solution 1: recursion. Backtrack implicitly by passing copies of subsets when 
necessary.

Idea: for each subset generated from the first k elements, we get subsets
generated from the first k+1 elements by including or excluding the 
(k+1)th element. 

Branching factor of 2, and depth n.

O(n * 2^n) time: there are 2^n subsets and up to n elements per subset.

O(n * 2^n) space for storing subsets.
O(n) space for recursive stack space.

"""
class Solution:
    def subsets(self, arr: List[int]) -> List[List[int]]:
        def rec(index=0, subset=[]):
            if index == n:
                res.append(subset)
                return

            rec(index + 1, subset)
            rec(index + 1, subset + [arr[index]])

        n = len(arr)
        res = []

        rec()

        return res

"""
Solution 1b: recursion. Backtrack explicitly, and at the bottom of the
recursion tree, append a *COPY* of the subset to the results.
"""
class Solution1b:
    def subsets(self, arr: List[int]) -> List[List[int]]:
        def rec(index=0, subset=[]):
            if index == n:
                res.append(subset[:]) # make a copy
                return

            rec(index+1, subset)
            
            subset.append(arr[index])
            rec(index+1, subset)

            subset.pop() # backtrack

        n = len(arr)
        res = []

        rec()

        return res


"""
Solution 1c: recursion. Backtrack implicitly by passing copies of subsets 
when necessary.

This variation parametrizes the backtrack function by the size k of the
subset. Instead of having one large recursion tree, we have n smaller
recursion trees. The branching factor varies from 1 to n, but the depth
of the recursion tree is generally smaller as we return early when
the length of the subset reaches the desired k.

"""
class Solution1c:
    def subsets(self, arr: List[int]) -> List[List[int]]:
        def rec(first=0, subset=[]):
            if len(subset) == k:
                res.append(subset[:]) # make a copy
                return

            for i in range(first, n):
                rec(i + 1, subset + [arr[i]])

        n = len(arr)
        res = []

        for k in range(n+1):
            rec()

        return res

"""
Solution 1d: recursion. Backtrack explicitly, and at the bottom of the
recursion tree, append a *COPY* of the subset to the results.

This variation parametrizes the backtrack function by the size k of the
subset.

https://leetcode.com/problems/subsets/solution/

"""
class Solution1d:
    def subsets(self, arr: List[int]) -> List[List[int]]:
        def rec(first=0, subset=[]):
            if len(subset) == k:
                res.append(subset[:]) # make a copy
                return

            for i in range(first, n):
                subset.append(arr[i])
                
                rec(i + 1, subset)

                subset.pop() # backtrack

        n = len(arr)
        res = []

        for k in range(n+1):
            rec()

        return res

###############################################################################
"""
Solution 2: iteration.

O(n * 2^n) time: there are 2^n subsets and up to n elements per subset.

O(n * 2^n) space

"""
class Solution2:
    def subsets(self, arr: List[int]) -> List[List[int]]:
        res = [[]]

        for x in arr:
            #res += [subset + [x] for subset in res]
            res.extend([subset + [x] for subset in res])

        return res

###############################################################################
"""
Solution 3: bits.

Each number from 0 to 2**len(arr) - 1 corresponds to a subset.
There are 2**len(arr) such subsets.

Each bit in the binary representation of the number represents whether
an element from the input array is in the corresponding subset.

Note: we can replace the inner loop with:
for x in arr: ... subset += [x]

O(n * 2^n) time
O(n * 2^n) space

"""
class Solution3:
    def subsets(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        n_subsets = 2**n
        res = []

        # Each i represents a subset via its pattern of n bits.
        for i in range(n_subsets):
            # Loop through bits
            subset = []
            for b in range(n): # bit index
                if i & 1:
                    subset += [arr[b]]
                i >>= 1

            res.append(subset)

        return res

"""
Solution 3b: same as sol 3, but more concise.
"""
class Solution3b:
    def subsets(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        n_subsets = 2**n
        res = []

        # Each i represents a subset via its pattern of n bits.
        for i in range(n_subsets):
            res.append( [arr[b] for b in range(n) if (i >> b) & 1] )

        return res

"""
Solution 3c: same as sol 3b, but using bit string.

"""
class Solution3c:
    def subsets(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        n_subsets = 2**n
        res = []

        # Each i represents a subset via its pattern of n bits.
        for i in range(n_subsets):
            bit_str = f"{i:{n}b}" # left padded with space
            res.append( [arr[b] for b in range(n) if bit_str[b] == '1'] )

        return res

"""
Solution 3d: same as sol 3, but use operations % and //= instead of bit 
operations & and >>=.

"""
class Solution3d:
    def subsets(self, arr: List[int]) -> List[List[int]]:
        n_subsets = 2**len(arr)
        res = []

        # Each i represents a subset via its pattern of bits.
        for i in range(n_subsets):
            subset = []

            for x in arr:
                if i % 2 == 1:
                    subset.append(x)
                i //= 2

            res.append(subset)

        return res

###############################################################################
"""
Solution 4: use itertools.combinations().

Simple list comprehension; don't worry about "combo" not being a list.

"""
class Solution4:
    def subsets(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        
        return [combo for k in range(n+1) for combo in itertools.combinations(arr, k) ]

"""
Solution 4b: same, but also make "combo" a list.
"""
class Solution4b:
    def subsets(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)

        return [list(combo) for k in range(n+1) for combo in itertools.combinations(arr, k) ]

"""
Solution 4c: use itertools.combinations() and itertools.chain.from_iterable().

Don't worry about converting anything to lists.
"""
class Solution4c:
    def subsets(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        
        return itertools.chain.from_iterable(itertools.combinations(arr, k) for k in range(n+1))

"""
Solution 4d: use itertools.combinations() and itertools.chain.from_iterable(),
but convert everything to lists afterwards.
"""
class Solution4d:
    def subsets(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)

        res = itertools.chain.from_iterable(itertools.combinations(arr, k) for k in range(0, n+1))

        return list(map(list, res))
        
"""
Solution 4e: use itertools.combinations().

Instead of using list comprehension or itertools.chain.from_iterable(),
use list extend() and map(list, *).
"""
class Solution4e:
    def subsets(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        res = []

        for k in range(n+1):
            #res.extend( [list(combo) for combo in itertools.combinations(arr, k)] )
            res.extend( map(list, itertools.combinations(arr, k)) )

        return res

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment, "\n")

        print(f"{arr}")

        res = sol.subsets(arr)

        print(f"\results: {res}\n")


    sol = Solution()   # recursion, backtrack implicitly
    sol = Solution1b() # backtrack explicitly
    sol = Solution1c() # backtrack implicitly, parametrize by size of subset
    sol = Solution1d() # backtrack explicitly, parametrize by size of subset
    
    #sol = Solution2() # iteration
    
    #sol = Solution3() # bits
    #sol = Solution3b() # bits, more concise
    #sol = Solution3c() # bits, using bit string
    #sol = Solution3d() # bits, using % and //= operations
    
    #sol = Solution4() # use itertools.combinations()
    #sol = Solution4b() # use itertools.combinations() and itertools.chain.from_iterable()
    #sol = Solution4c()
    #sol = Solution4d()
    #sol = Solution4e()

    comment = "Trivial case: no elements"
    arr = []
    test(arr, comment)

    comment = "One element"
    arr = [1]
    test(arr, comment)

    comment = "LC example: 3 elements"
    arr = [1,2,3]
    test(arr, comment)
    