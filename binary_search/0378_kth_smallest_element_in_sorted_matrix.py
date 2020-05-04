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
import itertools

###############################################################################
"""
Solution: use binary search on value space (lo, mid, hi are values). 
Search function is count of elements that are <= mid.
Target is k.

Min of matrix is mat[0][0], upper left corner.
Max of matrix is mat[-1][-1], lower right corner.

smallest    .   .   .   .   .
.           .               .
.               .           .
.                   .       .
n-1,0   .   .   .   .     largest

https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/301357/Java-0ms-(added-Python-and-C%2B%2B)%3A-Easy-to-understand-solutions-using-Heap-and-Binary-Search


O(n * log (max - min)) time
- O(log(max - min)) iterations
- counting number of elements <= mid takes O(2n) time

O(1) extra space
"""
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        lo = lowest = matrix[0][0]
        hi = highest = matrix[-1][-1] # matrix[n-1][n-1]

        while lo < hi:
            mid = lo + (hi - lo) // 2

            # Count number of elements <= mid.
            # 
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
                
                else: # x <= mid
                    smaller = max(smaller, x) # largest number <= mid
                    count += r + 1 # inc by num elts in current column up to and incl x 
                    c += 1

            # Pick right or left side.
            if count < k: # must be strict here ?
                lo = larger
            else:
                hi = smaller

        return lo

"""
LC example:
 1  5  9
10 11 13
12 13 15

lowest = 1, highest = 15

(iteration 1)
lo = 1
hi = 15
mid = 8

inner loop
    x = mat[2][0] = 12 > mid = 8
    larger = min(larger, x) = min(15, 12) = 12
    r -= 1, so r = 1

    x = mat[1][0] = 10 > mid = 8
    larger = min(larger, x) = min(12, 10) = 10
    r -= 1, so r = 0

    x = mat[0][0] = 1 <= mid = 8
    smaller = max(smaller, x) = max(1, 1) = 1
    count += (r+1), so count += 1, so count = 1
    c += 1, so c = 1

    x = mat[0][1] = 5 <= mid = 8
    smaller = max(smaller, x) = max(1, 5) = 5
    count += (r+1), so count += 1, so count = 2
    c += 1, so c = 2

    x = mat[0][2] = 9 > mid = 8
    larger = min(larger, x) = min(10, 9) = 9
    r -= 1, so r = -1

out of loop
    count = 2 < k = 8
    so lo = larger = 9
    note: smaller = 5; have 5 <= 8 (mid) < 9 (along row)


          N/A
           ^
 1 -> 5 -> 9
 ^
10
 ^
12


(iteration 2)
lo = 9
hi = 15
mid = 12

inner loop
    x = mat[2][0] = 12 = mid = 12
    smaller = max(smaller, x) = max(1, 12) = 12
    count += (r+1), so count += 3, so count = 3
    c += 1, so c = 1

    x = mat[2][1] = 13 > mid
    larger = min(larger, x) = min(15, 13) = 13
    r -= 1, so r = 1

    x = mat[1][1] = 11 <= mid
    smaller = max(smaller, x) = max(12, 11) = 11
    count += (r+1), so count += 2, so count = 5
    c += 1, so c = 2

    x = mat[1][2] = 13 > mid
    larger = min(larger, x) = min(13, 13) = 13
    r -= 1, so r = 0

    x = mat[0][2] = 9 <= mid
    smaller = max(smaller, x) = max(11, 9) = 9
    count += (r+1), so count += 1, so count = 6
    c += 1, so c = 3

out of loop
    count = 6 < k = 8
    so lo = larger = 13
    note: smaller = 9; have 9 <= 12 (mid) < 13


         9->N/A
         ^
    11->13
     ^
12->13


(iteration 3)
lo = 13
hi = 15
mid = 14
...

"""

###############################################################################
"""
Solution 2: binary search on value/range space, with inner binary search to
count elements <= mid.

O((n log n) * log(max - min)) = O(n (log n) log(max - min)) time
- O(log(max - min)) iterations
- each bsearch on a row takes O(log n) time
- counting number of elements <= mid uses n bsearches (one per row),
taking total of O(n log n) time

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
Solution 4: use min heap, and treat matrix as n sorted lists.
Don't use fact that columns are also sorted.

Note: min heap has size at most min(k,n).

O(m + k log m) ~ O(k log m) ~ O(n^2 log n) time, where m = min(k,n)
    - O(min(k,n)) to heapify initial list of min(k,n) elements
    - O(k log m) for loop, k iterations, each heap operation O(log m).

O(min(k,n)) ~ O(n) extra space: for heap
    - Initially, min(k,n) elements are placed on heap.
    - In each iteration, an elt is popped from heap, and an elt may or may not
    be pushed onto heap.

"""
class Solution4:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        # Put first element of each row into min heap.
        # Don't need to put more than k elements into heap.
        # Tuple is (val, row index, col index).
        end = min(k, n)
        h = [(matrix[r][0], r, 0) for r in range(end)]
        heapq.heapify(h)

        # h = [] # min heap (size will be at most k)
        # for r in range(end): # row index
        #     heapq.heappush(h, (matrix[r][0], r, 0) ) 

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
            c += 1
            if c < n: # if row has more elements
                heapq.heappush(h, (matrix[r][c], r, c) )
                
        # This point is never reached if 1 <= k <= n*n.

###############################################################################
"""
Solution 5: use max heap of size k, treating matrix as unsorted.

O(n^2 log k) time, where matrix is n-by-n
O(n^2 log n) time, since k ~ O(n^2)

O(k) ~ O(n^2) extra space: for heap
"""
class Solution5:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        h = [] # treat as max heap (of size k) by putting -x into min heap

        for row in matrix:
            for x in row:
                if len(h) == k:
                    heapq.heappushpop(h, -x)
                else:
                    heapq.heappush(h, -x)

        return -h[0]

###############################################################################
"""
Solution 6: use sorting or heapq functions.

"The difference is that Timsort implemented in Python is capable of taking 
advantage of existing partial orderings. Moving sorted data in bulk is always 
faster than comparing and moving individual data elements, due to modern 
hardware architecture."

For sorting (not sure about heapq functions):
O(n^2 log n) time
O(n^2) extra space
"""
class Solution6:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        s = []
        
        for row in matrix:
            s += row

        return sorted(s)[k-1]

        # return sorted(itertools.chain(*matrix))[k-1]
        # return sorted(x for row in matrix for x in row)[k-1]
        # return sorted(itertools.chain.from_iterable(matrix))[k-1]

        ### These have higher runtimes on LC:

        #return list(heapq.merge(*matrix))[k-1]
        #return next(itertools.islice(heapq.merge(*matrix), k-1, k))
        
        #return heapq.nsmallest(k, itertools.chain(*matrix))[-1]
        #return heapq.nsmallest(k, itertools.chain.from_iterable(matrix))[-1]

###############################################################################

if __name__ == "__main__":
    def test(arr, target, comment=None):
        print("="*80)
        if comment:
            print(comment)
        
        print()
        for row in matrix:
            print(row)

        print(f"\nk = {k}")
        
        res = sol.kthSmallest(matrix, k)

        print(f"\nres = {res}")


    sol = Solution() # use bsearch, with ...
    #sol = Solution2() # use bsearch, with inner bsearch to count

    #sol = Solution3() # use bsearch, naive counting of elts <= mid
    #sol = Solution3b() # use bsearch, Pythonic naive counting
    
    #sol = Solution4() # use max heap, treating matrix as n sorted lists
    #sol = Solution5() # use max heap of size k, treating matrix as unsorted

    #sol = Solution6() # sorting

    comment = "LC ex1; answer = 13"
    matrix = [
        [ 1,  5,  9],
        [10, 11, 13],
        [12, 13, 15]]
    k = 8
    test(matrix, k, comment)
   