"""
373. Find K Pairs with Smallest Sums
Medium

You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]] 
Explanation: The first 3 pairs are returned from the sequence: 
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [1,1],[1,1]
Explanation: The first 2 pairs are returned from the sequence: 
             [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [1,3],[2,3]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
"""

from typing import List
import heapq
import itertools
   
###############################################################################
"""
Solution 1: use min heap. Get smallest k elements from m sorted lists of sums.

Start with first sum arr1[0] + arr2[0]. Each time an entry is popped from
heap, push the entry next in the row (if there are anymore). If the popped
entry was first in its row, then also add the first entry of the next row.

Based on solution 5 here:
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/discuss/84550/Slow-1-liner-to-Fast-solutions

//
Idea from: (solution 1b is based on this)
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/discuss/84551/simple-Java-O(KlogK)-solution-with-explanation

Example:
arr1 = [1,7,11,16]
arr2 = [2,9,10,15]

Arrange values of arr1 along column, and values of arr2 along row.
The sums form a matrix. Since the arrays are sorted, each row and column of 
the matrix is also sorted.

    2       9       10      15
1   1+2     1+9     1+10    1+15
7   7+2     7+9     7+10    7+15
11  11+2    11+9    11+10   11+15
16  16+2    16+9    16+10   16+15

    2       9       10      15
1   3       10      11      16
7   9       16      17      22
11  13      20      21      26
16  18      25      26      31

Looking at rows, we have m sorted lists of sums. So this problem is like
merging m sorted lists, or finding the smallest k elements from m sorted
lists.

O(k log m) ~ O(mn log m) time

O(m) extra space: for heap
- Start with 1 elt in heap. If smallest sum is in 1st column, then 2 elts
are pushed onto heap, for net change of +1. This can be done m-1 times at
the start, resulting in m elts on the heap.

Runtime: 44 ms, faster than 92.22% of Python3 online submissions
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
    def kSmallestPairs(self, arr1: List[int], arr2: List[int], k: int) -> List[List[int]]:
        if not arr1 or not arr2:
            return []

        # Start with first sum only.
        h = [(arr1[0] + arr2[0], 0, 0)] # (sum, row index, col index)

        m = len(arr1)
        n = len(arr2)

        # Adjust k in case it's > number of possible sums.
        # Alternatively, can use "while h and len(res) < k".
        k = min(k, m*n)
        res = [] # results

        while len(res) < k:
        #while h and len(res) < k:
            #print(h)
            _, r, c = heapq.heappop(h) # sum, row index, column index

            res.append( [arr1[r], arr2[c]] )

            if c == 0 and r+1 < m: # add entry from first sum of next row
                heapq.heappush(h, (arr1[r+1] + arr2[0], r+1, 0) )

            if c+1 < n: # add entry from next sum of same row
                heapq.heappush(h, (arr1[r] + arr2[c+1], r, c+1) )

        return res

"""
Solution 1b: use min heap. Get smallest k elements from m sorted lists of sums.

Same as sol 1, but start by adding first element of each sorted list to heap.

Size of heap is at most m1 = min(k, m).

O(m1 + k log m1) ~ O(mn log m) time
- O(m1) time for building initial heap and for heapify
- O(k log m1) time for O(2k) heap operations on heap of size at most m1.

O(m1) ~ O(m) extra space: for heap

"""
class Solution1b:
    def kSmallestPairs(self, arr1: List[int], arr2: List[int], k: int) -> List[List[int]]:
        if not arr1 or not arr2:
            return []

        m = len(arr1)
        n = len(arr2)

        # Adjust k in case it's > number of possible sums.
        # Alternatively, can use "while h and len(res) < k".
        k = min(k, m*n)
        res = [] # results

        # h = [] # min heap
        # for i, x in enumerate(arr1):
        #     heapq.heappush(h, (x + y, i, 0) ) # (sum, row index, column index)

        # Add first element of each list of sorted sums to heap.
        y = arr2[0]
        #h = [(x+y, i, 0) for i, x in enumerate(arr1)]
        m1 = min(k, m)
        h = [(arr1[i] + y, i, 0) for i in range(m1)]
        heapq.heapify(h)

        while len(res) < k:
        #while h and len(res) < k:
            _, r, c = heapq.heappop(h) # sum, row index, column index

            res.append( [arr1[r], arr2[c]] )

            if c+1 < n: # add entry from next sum of same row
                heapq.heappush(h, (arr1[r] + arr2[c+1], r, c+1) )

        return res

###############################################################################
"""
Solution 2: turn each row into generator of triples (x+y, x, y) instead of
generating whole matrix.  Use heapq.merge().

Runtime: 48 ms, faster than 80.04% of Python3 online submissions
Memory Usage: 13.3 MB, less than 77.78% of Python3 online submissions
"""
class Solution2:
    def kSmallestPairs(self, arr1: List[int], arr2: List[int], k: int) -> List[List[int]]:
        streams = map(lambda x: ([x+y, x, y] for y in arr2), arr1)
        stream = heapq.merge(*streams)
        return [[x,y] for _, x, y in itertools.islice(stream, k)]

###############################################################################
"""
Solution 3: brute force using itertools.product()

Note: returns list of tuples.  Can wrap it using map(list, *) to return list
of lists.

O(mn log mn) time: due to sorting list of mn tuples
O(mn) extra space

Runtime: 196 ms, faster than 42.40% of Python3 online submissions
Memory Usage: 41.7 MB, less than 33.33% of Python3 online submissions
"""
class Solution3:
    def kSmallestPairs(self, arr1: List[int], arr2: List[int], k: int) -> List[List[int]]:
        return sorted(itertools.product(arr1, arr2), key=sum)[:k]

###############################################################################
"""
Solution 4: use itertools.product() with heapq.nsmallest(k, *, key=sum).

O(mn log k) time: mn heap pushes into heap of size k
O(k) extra space: since heapq.nsmallest() uses heap of size k

Runtime: 144 ms, faster than 47.53% of Python3 online submissions
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions
"""
class Solution4:
    def kSmallestPairs(self, arr1: List[int], arr2: List[int], k: int) -> List[List[int]]:
        return heapq.nsmallest(k, itertools.product(arr1, arr2), key=sum)

###############################################################################

if __name__ == "__main__":
    def test(nums1, nums2, k, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\narr1 = {nums1}")
        print(f"arr2 = {nums2}")
        print(f"k = {k}")
        
        res = sol.kSmallestPairs(nums1, nums2, k)

        print(f"\nres = {res}\n")


    sol = Solution() # use min heap; treat as m sorted lists of sums
    #sol = Solution1b() # same, but start with first sum of each row
    
    #sol = Solution2() # use heapq.merge() on generators for each row
    
    #sol = Solution3() # brute force using itertools.product(arr1, arr2, key=sum)
    #sol = Solution4() # use itertools.product() with heapq.nsmallest(k, *).
    
    comment = "LC ex1; answer = [[1,2],[1,4],[1,6]]"
    nums1 = [1,7,11]
    nums2 = [2,4,6]
    k = 3
    test(nums1, nums2, k, comment)
    
    comment = "LC ex2; answer = [1,1],[1,1]"
    nums1 = [1,1,2]
    nums2 = [1,2,3]
    k = 2
    test(nums1, nums2, k, comment)
    
    comment = "LC ex3; answer = [1,3],[2,3]"
    nums1 = [1,2]
    nums2 = [3]
    k = 3
    test(nums1, nums2, k, comment)

    comment = "LC test case; answer = []"
    nums1 = []
    nums2 = []
    k = 5
    test(nums1, nums2, k, comment)

    comment = "LC test case; answer = [[1,1],[1,1],[2,1],[1,2],[1,2],[2,2],[1,3],[1,3],[2,3]]"
    nums1 = [1,1,2]
    nums2 = [1,2,3]
    k = 10
    test(nums1, nums2, k, comment)

    comment = "discussion example; answer = "
    nums1 = [1,7,11,16]
    nums2 = [2,9,10,15]
    k = 20
    test(nums1, nums2, k, comment)
