"""
215. Kth Largest Element in an Array
Medium

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

from typing import List
import heapq
import random

###############################################################################
"""
Solution 1: use min heap of size k

PRO: can deal w/ real-time (online) stream data
CON: O(k) space rather than O(1) space used in sorting in-place

O(n log k) time
O(k) space
"""
class Solution:
    def findKthLargest(self, arr: List[int], k: int) -> int:
        h = [] # min heap of size k

        for x in arr:
            if len(h) == k:
                heapq.heappushpop(h, x) # O(log k)
            else:
                heapq.heappush(h, x) # O(log k)

        return h[0]

###############################################################################
"""
Solution 2: use heapq.nlargest()

O(n log k) time
O(k) space ?
"""
class Solution2:
    def findKthLargest(self, arr: List[int], k: int) -> int:
        return heapq.nlargest(k, arr)[-1]

###############################################################################
"""
Solution 3: D&C using quick select, and move duplicates to be contiguous.

O(n) time avg case, O(n^2) worst case.
O(1) extra space

If use median of medians to pick pivots (not implemented here):
O(n) time worst case
O(log n) extra space
"""
class Solution3:
    def findKthLargest(self, arr: List[int], k: int) -> int:
        def partition(left, right):
            pivot = arr[right]
            i = left

            for j in range(left, right):
                if arr[j] > pivot: # Note ">"
                    arr[j], arr[i] = arr[i], arr[j]
                    i += 1

            ### Used for median of medians
            #store_index = i # start of indices with values == pivot

            # Move duplicates of pivot to be contiguous.
            for j in range(i, right):
                if arr[j] == pivot:
                    arr[j], arr[i] = arr[i], arr[j]
                    i += 1

            # Swap original pivot at arr[right] to ith index position.
            arr[i], arr[right] = arr[right], arr[i]

            # Don't need to worry about range of duplicates if not doing
            # median of medians.
            return i

        # Assume valid k.
        n = len(arr)
        left = 0
        right = n - 1

        while left <= right:
            p = random.randint(left, right)
            arr[p], arr[right] = arr[right], arr[p]
            
            p = partition(left, right)
            
            # using quickselect for index k-1 to get kth largest
            if p == k - 1: 
                return arr[p]
            elif p < k - 1:
                left = p + 1
            else: # p > k - 1
                right = p - 1

###############################################################################
"""
Solution 4: use sorting.

O(n log n) time
O(1) extra space: for in-place sorting.
"""
class Solution4:
    def findKthLargest(self, arr: List[int], k: int) -> int:
        arr.sort()
        return arr[-k]

###############################################################################

if __name__ == "__main__":
    def test(arr, k, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(arr)
        print(f"k = {k}")

        res = sol.findKthLargest(arr, k)

        print(f"\nres = {res}")


    sol = Solution() # max heap of size k
    sol = Solution2() # heapq.nlargest(k, arr)[-1]
    sol = Solution3() # quick select
    #sol = Solution4() # sort

    comment = "LC ex1; answer = 5"
    arr = [3,2,1,5,6,4]
    k = 2
    test(arr, k, comment)

    comment = "LC ex2; answer = 4"
    arr = [3,2,3,1,2,4,5,5,6]
    k = 4
    test(arr, k, comment)
