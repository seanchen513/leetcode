"""
46. Permutations
Medium

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

from typing import List
import collections
import itertools

###############################################################################
"""
Solution 1: recursion, passing starting index to swap values of succeeding 
indices with. Aka, "swap" backtracking.

O(n * n!) time: O(n!) recursive calls, O(n) for copying list ("a[:]").

There's also time taken by all the swap operations...
Overall is probably O(n * n!) or O(n^2 * n!).

O(n * n!) extra space: n! permutations in the end, each taking O(n) space.

O(n) extra space: for recursive stack space.
"""
class Solution:
    def permute(self, a: List[int]) -> List[List[int]]:
        def rec(first=0):
            if first == n:
                res.append(a[:]) # important to make copy
                return

            # Be careful to include case of swapping a[first] with itself!
            for i in range(first, n):
                a[first], a[i] = a[i], a[first]
                rec(first + 1)
                a[first], a[i] = a[i], a[first] # swap back

        n = len(a)
        res = []

        rec()

        return res

"""
Solution 1b: same, but backtrack fn returns list of permutations.

Seems to be a lot of unnecessary joining of lists (empty list + full list)
at all levels of recursion except the lowest one.
"""
class Solution1b:
    def permute(self, a: List[int]) -> List[List[int]]:
        def rec(first=0):
            perms = []

            if first == n:
                perms.append(a[:]) # important to make copy
                return perms

            for i in range(first, n):
                a[first], a[i] = a[i], a[first]
                perms += rec(first + 1)
                a[first], a[i] = a[i], a[first] # swap back

            return perms

        n = len(a)

        return rec(0)

###############################################################################
""" 
Solution 2: recursion, passing permutation being built and counter.

This generalizes in case the input array contains duplicates.
"""
class Solution2:
    def permute(self, arr: List[int]) -> List[List[int]]:
        def rec(perm, freq):			
            if len(perm) == n:
                res.append(perm[:]) # important to make a copy
                return

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
NOT A SOLUTION--just for illustration

Recursion, passing permutation being built and set of unused elements so far.

The problem seems to be that adding and removing elements from the set
disrupts the order of elements in the set, so that looping through the set
doesn't work as expected.

"""
class Solution2_NOT:
    def permute(self, arr: List[int]) -> List[List[int]]:
        def rec(perm, unused_elts):			
            if not unused_elts: 
            # if len(perm) == n:
                res.append(perm[:]) # important to make a copy
                return

            for x in unused_elts:
                perm.append(x)
                unused_elts.remove(x)

                rec(perm, unused_elts)

                perm.pop()
                unused_elts.add(x)

        #n = len(arr)
        res = []

        rec([], set(arr))

        return res

"""
Solution 2b: same, but the backtrack modifications are within the
arguments to the recursive function call.

Since we pass a modified copy of the permutation when calling the recursive 
backtrack function, we don't have to make a copy of each final permutation.

"""
class Solution2b:
    def permute(self, arr: List[int]) -> List[List[int]]:
        def rec(perm, unused_elts):
            if not unused_elts:
                res.append(perm) # don't need to make copy of perm
                return

            for x in unused_elts:
                rec(perm + [x], unused_elts - set([x]))

        res = []

        rec([], set(arr))

        return res

"""
Solution 2c: index version of sol 2b
"""
class Solution2c:
    def permute(self, arr: List[int]) -> List[List[int]]:
        def rec(indices, perm=[]):			
            if not indices: # unused indices
                res.append(perm)
                return

            for i in indices:
                rec(indices - set([i]), perm + [arr[i]])

        n = len(arr)
        indices = set(range(n))
        res = []

        rec(indices)

        return res

###############################################################################
"""
Solution 3: iteration

Build list of permutations iteratively.

For kth iteration, we start with all permutations of length k.
For each of these perms, form set of elements that haven't been used yet.
For each unused element, append it to the current perm to form a new
perm to add to a new list of perms of length k+1.

0th iteration: starts with list of just the empty permutation, [ [] ].
1st iteration: starts with [ [x0], [x1], ..., [x_(n-1)] ].

where x0 is shorthand for arr[0], etc.

"""
class Solution3:
    def permute(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        all_elts = set(arr)
        res = [[]]

        for _ in range(n):
            next_res = []

            for perm in res:
                elts = all_elts - set(perm)
                
                for x in elts:
                    next_res.append(perm + [x])

            res = next_res

        return res

"""
Solution 3b: index version of sol 3.
"""
class Solution3b:
    def permute(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        all_indices = set(range(n))
        res = [[]]

        for _ in range(n):
            next_res = []

            for perm in res:
                indices = all_indices - set(perm)
                
                for i in indices:				
                    next_res.append(perm + [i])

            res = next_res

        return [[arr[i] for i in perm] for perm in res]

"""
Solution 3c: same as sol 3, but store set of unused elements in tuple
along with permutation.

kth iteration: O(k! * n * (n-k)) time
- Start with k! permutations and n-k unused elements.
- Creating new list "perm + [x]" takes O(k) time.
- Creating new set "unused_elts - set([x])" takes O(n-k) time.
- Creating both the new list and new set together takes O(n) time.

O(n! * n^2) time ?

O(n! * n) space: n! permutations in the end, with each taking O(n) space.
"""
class Solution3c:
    def permute(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        res = [([], set(arr))]

        for _ in range(n):
            next_res = []

            for perm, unused_elts in res:
                
                for x in unused_elts:
                    next_res.append((perm + [x], unused_elts - set([x]))) # O(n) time

            res = next_res

        return [perm for perm, _ in res]


"""
Solution 3d: index version of sol 3c.
"""
class Solution3d:
    def permute(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        res = [([], set(range(n)))]

        for _ in range(n):
            next_res = []

            for perm, unused_indices in res:
                
                for i in unused_indices:
                    next_res.append((perm + [arr[i]], unused_indices - set([i])))

            res = next_res

        return [perm for perm, _ in res]

###############################################################################
"""
Solution 4: iteration

Build up list of permutations iteratively.

For kth element, insert it at all possible places in all existing
permutations to create new list of permutations.

kth iteration: start with all permutations of elements arr[i], i=0..k-1.

0th iteration: starts with list of just the empty permutation, [ [] ].
1st iteration: starts with [ [x0] ].
2nd iteration: starts with [ [x1, x0], [x0, x1] ].

where x0 is shorthand for arr[0], etc.

O(n^2 * n!) time ?
- Outer loop has n iterations.
- For iteration k (0-based), we start with k! permutations that we loop over.
- Each of these perms has length k.
- For each of these permutations, we loop k+1 times, doing slicing and joining
of lists that take O(k) time.

Overall time complexity:
sum(k! * (k+1) * k) for k = 0, 1, ..., n-1.

O(n! * n) extra space: for output list of n! perms, each taking O(n) space.
"""
class Solution4:
    def permute(self, arr: List[int]) -> List[List[int]]:
        perms = [[]]

        for x in arr:
            new_perms = []

            for p in perms:
                for i in range(len(p) + 1):
                    new_perms.append(p[:i] + [x] + p[i:])

            perms = new_perms

        return perms

###############################################################################
"""
Solution 5: use itertools.permutations().
"""
class Solution5:
    def permute(self, arr: List[int]) -> List[List[int]]:
        return list(map(list, itertools.permutations(arr, len(arr))))

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment, "\n")

        print(f"{arr}")

        res = sol.permute(arr)

        print(f"\nresult: {res}\n")


    sol = Solution() # recursion, passing first index to swap succeeding elts with
    #sol = Solution1b() # same, but return list of permutations from backtrack fn

    #sol = Solution2() # recursion, passing permutation being built and counter.
    #sol = Solution2b() # recursion, passing set of elements not used yet
    #sol = Solution2c() # index version
    
    """
    For kth iteration, start with all permutations of length k.
    For each of these perms, form set of elements that haven't been used yet.
    For each unused element, append it to the current perm to form a new
    perm to add to a new list of perms of length k+1.
    """
    #sol = Solution3() # 
    #sol = Solution3b() # index version of sol 
    
    #sol = Solution3c() # same, but store set of unused elts in tuple along with perm
    #sol = Solution3d() # index version of sol 2c

    """
    Iteration. For kth element, insert it at all possible places in all 
    existing permutations to create new list of permutations.
    """
    sol = Solution4() 
    
    """ use itertools.permutations """
    #sol = Solution5() 

    
    comment = "Trivial case: no elements"
    arr = []
    test(arr, comment)

    comment = "One element"
    arr = [1]
    test(arr, comment)

    comment = "LC example"
    arr = [1,2,3]
    test(arr, comment)

    comment = ""
    arr = ['z','x','y']
    test(arr, comment)
