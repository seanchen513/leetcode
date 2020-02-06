"""
239. Sliding Window Maximum
Hard

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Note:
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
"""

from typing import List

###############################################################################
"""
Solution 1: use decreasing deque with window k.  Store indices.

Loop through given array:
1. Popleft elements that are outside window.
2. Pop (right) elements are <= current value.
3. Add current index to deque.
4. If we have considered at least k elts, then add value for index from
front of deque to results list.

O(n) time
O(n) extra space - O(k) for deque, but O(n-k+1) for output

Runtime: 144 ms, faster than 98.35% of Python3 online submissions
Memory Usage: 19.3 MB, less than 100.00% of Python3 online submissions
"""
import collections

class Solution:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        if n == 0 or k == 0:
            return []

        q = collections.deque()
        res = []
        
        for i in range(0, n):
            # Remove elements outside the current window.
            while q and i - q[0] >= k:
                q.popleft()

            # Remove elements with values smaller than current value
            # This maintains a decreasing deque.
            # These removed values can't be maxes furthermore due to the
            # new value being bigger.
            while q and arr[q[-1]] <= arr[i]:
                q.pop()

            q.append(i)

            if i >= k - 1:
                res.append(arr[q[0]])

        return res

###############################################################################
"""
Solution 2: Calculate running maxes within blocks forward and reverse.

O(n) time: three passes of array
O(n) extra space: two arrays of size n for running maxes, aside from output
"""
class Solution2:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        if n == 0 or k == 0:
            return []

        left = [0]*n # running maxes within a block, going forward
        right = [0]*n # running maxes within a block, going in reverse

        ### Calculate running maxes within a block, going foward.
        left[0] = arr[0] 
        for i in range(1,n):
            if i % k == 0: # start of a block
                left[i] = arr[i] 
            else:
                left[i] = max(left[i-1], arr[i])
                
        ### Calculate running maxes within a block, going in reverse.
        right[n-1] = arr[n-1]
        for i in reversed(range(n-1)):
            if i % k == k - 1: # end of a block
                right[i] = arr[i]
            else:
                right[i] = max(right[i+1], arr[i])

        ### Use running maxes in both directions to calculate results.
        res = []
        for i in range(n-k+1):
            res.append(max(left[i+k-1], right[i]))

        return res

###############################################################################
"""
Solution: brute force

O(nk) time
O(k) extra space - O(k) for deque; don't include O(n-k+1) for output
"""
class Solution3:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        if n == 0 or k == 0:
            return []

        return [max(arr[start:start+k]) for start in range(n-k+1)]

###############################################################################

if __name__ == "__main__":
    def test(arr, k, comment=None):
        res = s.maxSlidingWindow(arr, k)
        
        print("="*80)
        if comment:
            print(comment)
            
        print(f"\n{arr}")
        print(f"k = {k}")
        print(f"\nmaxes = {res}")


    #s = Solution()  # decreasing deque
    s = Solution2() # running maxes within a block going fwd and in reverse
    #s = Solution3() # brute force

    comment = "LC example; answer = [3,3,5,5,6,7]"    
    arr = [1,3,-1,-3,5,3,6,7]
    k = 3
    test(arr, k, comment)

    comment = "LC test case; answer = [1,-1]"
    arr = [1,-1]
    k = 1
    test(arr, k, comment)

    comment = "LC test case; answer = [3,3,2,5]"
    arr = [1,3,1,2,0,5]
    k = 3
    test(arr, k, comment)

    comment = "LC trivial case; answer = []"
    arr = []
    k = 0
    test(arr, k, comment)

    comment = "LC test case; answer = [7,7,7,7,7]"
    arr = [-7,-8,7,5,7,1,6,0]
    k = 4
    test(arr, k, comment)

    comment = "LC test case; answer = [8,8,8,6,6]"
    arr = [1,-9,8,-6,6,4,0,5]
    k = 4
    test(arr, k, comment)

    comment = "LC test case; answer = [10,10,9,2]"
    arr = [9,10,9,-7,-4,-8,2,-6]
    k = 5
    test(arr, k, comment)

    comment = "Window of size 1"
    arr = [3,1,4,1,5,9,2,6,5]
    k = 1
    test(arr, k, comment)
