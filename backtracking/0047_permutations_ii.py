"""
47. Permutations II
Medium

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

from typing import List
import collections
import itertools

###############################################################################
"""
Solution: backtracking using an element counter.

Count elements, and do backtracking by choosing each element with positive 
count left, decrement its count, and appending the element to the growing perm.

Backtrack by popping the element from the end of the perm, and incrementing 
its count.

Since we are not modifying the input array in-place, we have to pass the
permutation as a parameter to the backtrack function.

"""
class Solution:
    def permuteUnique(self, arr: List[int]) -> List[List[int]]:
        def rec(perm, freq):
            if len(perm) == n:
                res.append(perm[:]) # important to make a copy

            for x in freq:
                if freq[x] > 0:
                    perm.append(x)
                    freq[x] -= 1

                    rec(perm, freq)
                    
                    perm.pop()
                    freq[x] += 1

        n = len(arr)
        res = []

        rec([], collections.Counter(arr))

        return res

"""
Solution 1b: same, but pass a modified copy of the permutation when
calling the recursive backtrack function. 

In this case, we don't have to make a copy of each final permutation.
"""
class Solution1b:
    def permuteUnique(self, arr: List[int]) -> List[List[int]]:
        def rec(perm, freq):
            if len(perm) == n:
                res.append(perm) # don't need to make a copy

            for x in freq:
                if freq[x] > 0:
                    freq[x] -= 1

                    rec(perm + [x], freq) # passing modified copy of perm
                    
                    freq[x] += 1

        n = len(arr)
        res = []

        rec([], collections.Counter(arr))

        return res

###############################################################################
"""
Solution 2: iteration...

Build up list of permutations iteratively.

For kth element, insert it at all possible places in all existing
permutations to create new list of permutations.

To handle duplicaton of perms, avoid inserting an element after any of its 
duplicates.
"""
class Solution2:
    def permuteUnique(self, arr: List[int]) -> List[List[int]]:
        res = [[]]

        for x in arr:
            new_res = []

            for p in res:
                for i in range(len(p) + 1):
                    new_res.append(p[:i] + [x] + p[i:])

                    if i < len(p) and p[i] == x: # handles duplication
                        break

            res = new_res

        return res

###############################################################################
"""
Solution 3: use "swap" backtracking as if there were no duplicates. Handle
duplicates by using a set to store permutations in tuple form.

Recall that tuples are hashable and can be stored in sets, while lists
are not hashable and cannot be stored in sets.

SLOW.
"""
class Solution3:
    def permuteUnique(self, arr: List[int]) -> List[List[int]]:
        def rec(start):
            if start == n:
                res.add(tuple(arr)) # makes a copy in tuple form

            for i in range(start, n):
                arr[start], arr[i] = arr[i], arr[start]
                rec(start + 1)
                arr[start], arr[i] = arr[i], arr[start] # swap back

        n = len(arr)
        res = set()

        rec(0)

        return res
        #return list(res)
        #return list(list(perm) for perm in res)

###############################################################################
"""
Solution 4: use itertools.permutations(). Handle duplicate perms by storing
perms as tuples in a set.
"""
class Solution4:
    def permuteUnique(self, arr: List[int]) -> List[List[int]]:
        return set(map(tuple, itertools.permutations(arr, len(arr))))

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment, "\n")

        print(f"{arr}")

        res = sol.permuteUnique(arr)

        print(f"\nresult: {res}\n")


    sol = Solution() # backtracking with element counter
    sol = Solution1b() # same, but pass modified copy of perm when calling backtrack fn
    
    sol = Solution2() # iteration

    #sol = Solution3() # "swap" backtracking, maintaining set of perms in tuple form
    
    #sol = Solution4() # use itertools.permutations
    
    comment = "Trivial case: no elements"
    arr = []
    test(arr, comment)

    comment = "One element"
    arr = [1]
    test(arr, comment)

    comment = ""
    arr = [1,2,3]
    test(arr, comment)

    comment = ""
    arr = ['z','x','y']
    test(arr, comment)

    comment = "LC example"
    arr = [1,1,2]
    test(arr, comment)

