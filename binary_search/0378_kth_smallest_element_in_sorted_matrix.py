"""
378. Kth Smallest Element in a Sorted Matrix
Medium

Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.
"""

from typing import List
import bisect
import heapq

###############################################################################
"""
Solution: use binary search, counting of elements <= mid...

https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/301357/Java-0ms-(added-Python-and-C%2B%2B)%3A-Easy-to-understand-solutions-using-Heap-and-Binary-Search

"""
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        lo = lowest = matrix[0][0]
        hi = highest = matrix[n-1][n-1]

        while lo < hi:
            mid = lo + (hi - lo) // 2

            # Count number of elements <= mid.
            count = 0
            r = n-1
            c = 0
            smaller = lowest
            larger = highest

            while r >= 0 and c < n:
                x = matrix[r][c]
                if x > mid:
                    larger = min(larger, x) # smallest number > mid
                    r -= 1
                else:
                    smaller = max(smaller, x) # largest number <= mid
                    count += r + 1
                    c += 1

            # Pick right or left side.
            if count < k: # must be strict here ?
                lo = larger
            else:
                hi = smaller

        return lo

###############################################################################
"""
Solution 2: binary search on value/range space, with inner binary search to
count elements <= mid.

O(n (log n) log(max - min)) time ?
O(1) extra space
"""
class Solution2:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        lo = matrix[0][0]
        hi = matrix[n-1][n-1]

        while lo < hi:
            mid = lo + (hi - lo) // 2

            # Count number of elements <= mid.
            count = sum(bisect.bisect(matrix[r], mid) for r in range(n))

            # Pick right or left side.
            if count < k: # must be strict here
                lo = mid + 1
            else:
                hi = mid

        return lo

###############################################################################
"""
Solution 3: use binary search; naive counting of elements <= mid.

https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85173/Share-my-thoughts-and-Clean-Java-Code

"""
class Solution3:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        lo = matrix[0][0]
        hi = matrix[n-1][n-1]

        while lo < hi:
            mid = lo + (hi - lo) // 2

            # Count number of elements <= mid.
            count = 0
            c = n - 1

            for r in range(n): # for each row
                while c >= 0 and matrix[r][c] > mid:
                    c -= 1
                
                count += c + 1

            # Pick right or left side.
            if count < k: # must be strict here
                lo = mid + 1
            else:
                hi = mid

        return lo

"""
Solution 3b: same as sol 1, but use Pythonic way to naively count number
of elements <= mid.
"""
class Solution3b:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        lo = matrix[0][0]
        hi = matrix[n-1][n-1]

        while lo < hi:
            mid = lo + (hi - lo) // 2

            count = sum(x <= mid for row in matrix for x in row)

            if count < k:
                lo = mid + 1
            else:
                hi = mid

        return lo

###############################################################################
"""
Solution 4: use max heap, treating matrix as unsorted.

O(min(k,n) + k log n) ~ O(k log n) time:
    - O(min(k,n)) to put first element of each row into min heap.
    - O(k log n) for main loop, k iterations, each heap operation O(log n).
    - If k << n, then this is O(k + k log n) ~ O(k log n).
    - If k >> n, then this is O(n + k log n) ~ O(k log n).

O(k) extra space: for heap
    - Initially, k elements are placed on heap.
    - In main loop, k iterations, so k elements are placed on heap.
"""
class Solution4:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        h = [] # min heap of size k

        # Put first element of each row into min heap.
        # Don't need to put more than k elements into heap.
        end = min(k, n)
        for r in range(end): # row index
            # tuple is (val, row index, col index)
            heapq.heappush(h, (matrix[r][0], r, 0) ) 

        # Pop smallest element from min heap.
        # If running count equals k, then return the element.
        # If the popped element's row has more elements, add the next element.
        count = 0
        while h:
            val, r, c = heapq.heappop(h) # val, row index, col index
            count += 1

            if count == k:
                return val
            
            # c serves as both column index, and index within row
            if c + 1 < n: # if row has more elements
                heapq.heappush(h, (matrix[r][c+1], r, c+1) )

        # This point is never reached if 1 <= k <= n*n.

###############################################################################
"""
Solution 5: use max heap, treating matrix as unsorted.

O(n log n) time
O(n) extra space: for heap
"""
class Solution5:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        h = [] # treat as max heap (of size k) by putting -x into min heap

        for row in matrix:
            for x in row:
                if len(h) == k:
                    heapq.heappushpop(h, -x)
                else:
                    heapq.heappush(h, -x)

        return -h[0]

###############################################################################

if __name__ == "__main__":
    def test(arr, target, comment=None):
        print("="*80)
        if comment:
            print(comment)

        for row in matrix:
            print(row)

        print(f"k = {k}")
        
        res = sol.kthSmallest(matrix, k)

        print(f"\nres = {res}")


    sol = Solution() # use bsearch, with ...
    #sol = Solution2() # use bsearch, with inner bsearch to count

    #sol = Solution3() # use bsearch, naive counting of elts <= mid
    #sol = Solution3b() # use bsearch, Pythonic naive counting
    
    #sol = Solution4() # use max heap, treating matrix as n sorted lists
    #sol = Solution5() # use max heap, treating matrix as unsorted

    comment = "LC ex1; answer = 13"
    matrix = [
        [ 1,  5,  9],
        [10, 11, 13],
        [12, 13, 15]]
    k = 8
    test(matrix, k, comment)
   