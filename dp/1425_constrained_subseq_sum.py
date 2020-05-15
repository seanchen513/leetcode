"""
1425. Constrained Subsequence Sum
Hard

Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.

Example 1:

Input: nums = [10,2,-10,5,20], k = 2
Output: 37
Explanation: The subsequence is [10, 2, 5, 20].

Example 2:

Input: nums = [-1,-2,-3], k = 1
Output: -1
Explanation: The subsequence must be non-empty, so we choose the largest number.

Example 3:

Input: nums = [10,-2,-10,-5,20], k = 2
Output: 23
Explanation: The subsequence is [10, -2, -5, 20].

Constraints:

1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""

from typing import List
import collections
import heapq

"""
IF SKIP, then can skip k-1 consecutive elts

k=1: cannot have skips/holes.
k=2: can skip over 1 at a time
k=3: can skip over 2 at a time.
"""

###############################################################################
"""
Solution: DP w/ decreasing deque of positive values.

Same dp relations as in sol 2.
Size of deque is not necessarily always k.

O(n) time: each element is pushed and popped at most once.

O(n) extra space: for dp array
O(k) extra space: for deque
"""
class Solution:
    def constrainedSubsetSum(self, arr: List[int], k: int) -> int:
        n = len(arr)

        # ... initialize dp[i] to be sum of arr[i] by itself.
        # This is particularly important in case all array values are negative.
        dp = arr[:] 
        
        q = collections.deque()

        for i in range(n):
            if q: # q[0] is the max of dp[j] for j in [i-k, i)
                dp[i] += q[0]

            # Maintain decreasing deque.
            # dp[i] will be added to deque and it is newer than all other 
            # elements in the deque. Therefore, we can remove other values
            # in the deque that are smaller than dp[i].
            while q and dp[i] > q[-1]:
                q.pop()

            # ...
            if dp[i] > 0:
                q.append(dp[i])

            # Don't need dp[i-k] in next iteration since it will be out of range.
            if i >= k and q and q[0] == dp[i-k]:
                q.popleft()

        return max(dp)

"""
Solved it with DP between two positive numbers (mixture of stepping stairs 
with sliding window (using multiset)) to find the element to go to such that 
the negative cost is minimum. If negative cost > positive sum till now then 
initialize the positive sum to 0 (Kadane's algorithm).

"""

###############################################################################
"""
Solution 2: DP w/ max heap.

Let dp[i] be the max constrained subset sum of elements up to index i,
with dp[i] necessarily including a[i]. Then 

dp[i] = max(dp[j] + a[i]) = a[i] + max(dp[j]) for j in [i - k, i). 

Hence we need to maintain the max of the last k computed dp elements. 
It's easy with a max heap of pairs (dp[j], j).
Just remove the top if it is too old.

Alternatively, can find max dp in range using segment tree (range max query).
This results in same time complexity.

O(n log n) time
O(n) extra space: for dp array and heap
"""
class Solution2:
    def constrainedSubsetSum(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = arr[:] # ...
        h = [] # max heap

        for i in range(n):
            # Remove max dp elements if their indices are not within the
            # last k positions of current index i.
            while h and h[0][1] < i - k:
                heapq.heappop(h)

            if h:
                dp[i] = max(dp[i], arr[i] + h[0][0])

            heapq.heappush(h, (dp[i], i))

        return max(dp) # ...

###############################################################################
"""
Solution 3: DP with inner loop to find max of previous dp's within range k.

O(n*k) time
O(n) extra space: for dp array

TLE
"""
class Solution3:
    def constrainedSubsetSum(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = arr[:] # ...

        for i in range(n):
            start = max(i - k, 0) # don't let start index go below 0

            for j in range(start, i):
                dp[i] = max(dp[i], arr[i] + dp[j])

        return max(dp) # ...
        #return dp[-1] # doesn't work

###############################################################################

if __name__ == "__main__":
    def test(arr, k, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\narr = {arr}")
        print(f"k = {k}")

        res = sol.constrainedSubsetSum(arr, k)

        print(f"\nres = {res}\n")


    sol = Solution() # DP w/ decreasing deque of positive values
    #sol = Solution2() # DP w/ max heap
    #sol = Solution3() # DP with inner loop to find max of previous dp's within range k.

    comment = "LC ex1; answer = 37"
    arr = [10,2,-10,5,20]
    k = 2
    test(arr, k, comment)

    comment = "LC ex2; answer = -1"
    arr = [-1,-2,-3]
    k = 1
    test(arr, k, comment)

    comment = "LC ex3; answer = 23"
    arr = [10,-2,-10,-5,20]
    k = 2
    test(arr, k, comment)
