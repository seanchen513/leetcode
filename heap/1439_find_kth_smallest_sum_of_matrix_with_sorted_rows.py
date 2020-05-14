"""
1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows
Hard

You are given an m * n matrix, mat, and an integer k, which has its rows sorted in non-decreasing order.

You are allowed to choose exactly 1 element from each row to form an array. Return the Kth smallest array sum among all possible arrays.

Example 1:

Input: mat = [[1,3,11],[2,4,6]], k = 5
Output: 7
Explanation: Choosing one element from each row, the first k smallest sum are:
[1,2], [1,4], [3,2], [3,4], [1,6]. Where the 5th sum is 7.  

Example 2:

Input: mat = [[1,3,11],[2,4,6]], k = 9
Output: 17

Example 3:

Input: mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
Output: 9
Explanation: Choosing one element from each row, the first k smallest sum are:
[1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]. Where the 7th sum is 9.  

Example 4:

Input: mat = [[1,1,10],[2,2,9]], k = 7
Output: 12
 
Constraints:

m == mat.length
n == mat.length[i]
1 <= m, n <= 40
1 <= k <= min(200, n ^ m)
1 <= mat[i][j] <= 5000
mat[i] is a non decreasing array.
"""

from typing import List
import collections
import functools
import itertools
import heapq

###############################################################################
"""
Solution: use min heap to store (sum, tuple of column indices in each row).
Use set to track which combinations of elts have been visited, so we don't
push duplicate entries onto the heap.

Note: m^n possible sums.

O(k*m log maxh) ~ O(k*m*n log m) ~ O(m^(n+1) * n log m) time
- loop k times to get kth smallest sum
- in each iteration, consider each of m rows to find new sums (inner loop)
- log term for heappush() within each inner loop

O(maxh) = O(m^(n+1)) extra space: for heap

where maxh = max size of heap = O(m^(n+1))

In each of k iteration, pop 1 elt and add at most m elts.
So add at most k*(m-1) ~ m**(n+1) elts, since max k ~ m**n.

"""
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m = len(mat)
        n = len(mat[0])

        if k >= m**n: # optional
            return sum(mat[r][-1] for r in range(m))

        # min heap init'd with (sum of first elt in each row, list of indices).
        h = [(sum(mat[r][0] for r in range(m)), [0]*m)]

        seen = set()
        count = 0 # how many smallest sums have we considered so far

        while count < k:
            s, ind = heapq.heappop(h) # sum, list of indices
            
            count += 1
            #if count == k:
            #    return s

            # For each row, consider new sum where the next element of that row
            # is included instead of the current element.
            for r in range(m):
                c = ind[r]
                if c + 1 < n:
                    ind2 = ind[:]
                    ind2[r] += 1

                    if tuple(ind2) not in seen:
                        seen.add(tuple(ind2))
                        heapq.heappush(h, (s + mat[r][c+1] - mat[r][c], ind2))
        
        return s

"""
For testing.
In particular, for finding the max size that the min heap ever reaches.
"""
class Solution1b:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m = len(mat)
        n = len(mat[0])

        if k >= m**n: # optional
            return sum(mat[r][-1] for r in range(m))

        # min heap init'd with sum of first elt in each row.
        h = [(sum(mat[r][0] for r in range(m)), [0]*m)]

        seen = set()
        count = 0 # how many smallest sums have we considered so far
        maxh = 0 # max size of heap; for testing

        while count < k:
            s, ind = heapq.heappop(h)
            maxh = max(maxh, len(h)) # for testing
            
            #print(f"\ncount={count}, s={s}, ind={ind}")
            #print(f"len(h) = {len(h)}")
            #print(f"seen={seen}")
            
            count += 1
            #if count == k:
            #    return s

            for r in range(m):
                c = ind[r]

                if c + 1 < n:
                    ind2 = ind[:]
                    ind2[r] += 1

                    if tuple(ind2) not in seen:
                        seen.add(tuple(ind2))
                        heapq.heappush(h, (s + mat[r][c+1] - mat[r][c], ind2))
        
        print(f"max len(h) = {maxh}")
        
        return s

###############################################################################
"""
Solution 2: divide & conquer

Adapt LC373 Find k Pairs with Smallest Sums.
(Instead of it returning k smallest pairs, have it return k smallest sums.)

O(m*k log m) ~ O(m^2 n log m) time: helper function is used m-1 times,
and max k = m*n.

Helper function is O(k log m) ~ O(m*n log m) time.

Runtime: 112 ms, faster than 96.12% of Python3 online submissions
Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m = len(mat)
        res = mat[0]

        for i in range(1, m):
            res = self.kSmallestSums(res, mat[i], k)

        return res[k-1]

    # Adapted from LC373 Find k Pairs with Smallest Sums.
    def kSmallestSums(self, arr1: List[int], arr2: List[int], k: int) -> List[List[int]]:
        if not arr1 or not arr2:
            return []

        # Start with first sum only.
        h = [(arr1[0] + arr2[0], 0, 0)] # (sum, row index, col index)

        m = len(arr1)
        n = len(arr2)

        # Adjust k in case it's > number of possible sums.
        k = min(k, m*n)
        res = [] # results

        while len(res) < k:
            s, r, c = heapq.heappop(h) # sum, row index, column index

            #res.append( [arr1[r], arr2[c]] ) # original; to return pairs rather than sums
            res.append(s)

            if c == 0 and r+1 < m: # add entry from first sum of next row
                heapq.heappush(h, (arr1[r+1] + arr2[0], r+1, 0) )

            if c+1 < n: # add entry from next sum of same row
                heapq.heappush(h, (arr1[r] + arr2[c+1], r, c+1) )

        return res

###############################################################################
"""
Solution 3: like D&C sol. Iteratively calculate k smallest sums up to row r by
looking at sums of elts in current row with k smallest sums up to row r-1, and
sorting them.

len(h) = k and len(row) = n, so there are kn sums from h and row.
Sorting these sums take O(kn log kn) time.
This is done m-1 times.

O(kmn log kn) time

O(k) extra space: for list h
O(kn) extra space for list of sums and sorted() ?
"""
class Solution3:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        # For first row, k smallest sums are the first k elements.
        h = mat[0][:k] # mat[0][:] also works

        for row in mat[1:]:
            h = sorted([x+y for x in row for y in h])[:k]

        return h[k-1]

###############################################################################

if __name__ == "__main__":
    def test(mat, k, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\nmatrix = {mat}")
        print(f"k = {k}")

        res = sol.kthSmallest(mat, k)

        print(f"\nres = {res}\n")


    sol = Solution() # use min heap and visited set
    sol = Solution1b() # testing

    #sol = Solution2() # divide & conquer
    #sol = Solution3() # iteratively calculate k smallest sums up to row r...

    comment = "LC ex1; answer = 7"
    arr = [[1,3,11],[2,4,6]]
    k = 5
    test(arr, k, comment)

    comment = "LC ex2; answer = 17"
    arr = [[1,3,11],[2,4,6]]
    k = 9
    test(arr, k, comment)

    comment = "LC ex3; answer = 9"
    arr = [[1,10,10],[1,4,5],[2,3,6]]
    k = 7
    test(arr, k, comment)

    comment = "LC ex4; answer = 12"
    arr = [[1,1,10],[2,2,9]]
    k = 7
    test(arr, k, comment)
    
    comment = "; answer = 3"
    arr = [[1,1,1],[1,1,1],[1,1,1]]
    k = 25
    test(arr, k, comment)
    
    comment = "; answer = 4"
    arr = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
    k = 250
    test(arr, k, comment)

    comment = "; answer = 3"
    arr = [[1,1,1,1],[1,1,1,1],[1,1,1,1]]
    k = 63
    test(arr, k, comment)

    comment = "; answer = 4"
    arr = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]]
    k = 62
    test(arr, k, comment)

    comment = "; answer = 4"
    arr = [[1]*2 for _ in range(10)]
    k = 10**2 
    test(arr, k, comment)

"""
m = 2
n = 10

k = 10**2 - 1 -> maxh = 323


"""


"""
m = 10, n = 5
n**(m-1) ?

62 -> 451
1000 -> 5619
10000 -> 43120
10**5 - 1 = 99999 -> 278120

5**10 = 9,765,625
10*5 =100,000

m**n - xxxx

k(m-1) = (10**5 - 1) * 9 ~ 900k
m-1 = 9

max k ~ m**n

k(m-1) ~ (m**n)(m-1) ~ m**(n+1)
"""


