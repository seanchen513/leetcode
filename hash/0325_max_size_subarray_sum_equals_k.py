"""
325. Maximum Size Subarray Sum Equals k
Medium

Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4 
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.

Example 2:

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2 
Explanation: The subarray [-1, 2] sums to 1 and is the longest.

Follow Up:
Can you do it in O(n) time?
"""

from typing import List

###############################################################################
"""
Solution: use dict that maps prefix sums to first index found.

Be careful to deal with case where a prefix sum can equal k by initializing
d = {0: -1}.

O(n) time
O(n) extra space

Runtime: 104 ms, faster than 99.86% of Python3 online submissions
Memory Usage: 16.8 MB, less than 20.00% of Python3 online submissions
"""
class Solution:
    def maxSubArrayLen(self, arr: List[int], k: int) -> int:
        s = 0 # prefix sum
        mx = 0 # max  of subarrays with sum k
        d = {0: -1} # maps prefix sums to index

        for i in range(len(arr)):
            s += arr[i]

            if s not in d:
                d[s] = i

            if s - k in d:
                mx = max(mx, i - d[s - k])

        return mx

"""
Solution 1b: same as sol 1, but instead of initializing d[0] = -1, we
check if prefix sum == k in loop.
"""
class Solution1b:
    def maxSubArrayLen(self, arr: List[int], k: int) -> int:
        s = 0 # prefix sum
        mx = 0 # max  of subarrays with sum k
        d = {} # maps prefix sums to index

        for i in range(len(arr)):
            s += arr[i]

            if s == k:
                mx = i + 1
            elif s - k in d:
                mx = max(mx, i - d[s - k])

            if s not in d:
                d[s] = i

        return mx

###############################################################################
"""
Solution 2: brute force

O(n^2) time
O(1) extra space

TLE
"""
class Solution2:
    def maxSubArrayLen(self, arr: List[int], k: int) -> int:
        n = len(arr)
        mx = -1
        
        for i in range(n):
            s = 0
            
            for j in range(i, n):
                s += arr[j]
                
                if j - i >= mx and s == k:
                    mx = j - i
                    
        return mx + 1
                    
###############################################################################
"""
Solution 3: brute force using running sums

O(n^2) time
O(n) extra space

TLE
"""
class Solution3:
    def maxSubArrayLen(self, arr: List[int], k: int) -> int:
        if not arr:
            return 0

        n = len(arr)

        sums = [0] # running sums
        for i in range(n):
            sums.append( sums[-1] + arr[i] )
            
        for di in range(n, 0, -1):
            for i in range(n - di + 1):
                if sums[i + di] - sums[i] == k:
                    return di

        return 0

###############################################################################

if __name__ == "__main__":
    def test(arr, k, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(arr)

        res = sol.maxSubArrayLen(arr, k)

        print(f"\nres = {res}\n")


    sol = Solution() # use dict that maps prefix sums to index
    sol = Solution1b() # same but check if prefix sum == k in loop

    #sol = Solution2() # brute force
    #sol = Solution2() # brute force using running sums

    comment = "LC ex1; answer = 4"
    arr = [1, -1, 5, -2, 3]
    k = 3
    test(arr, k, comment)

    comment = "LC ex2; answer = 2"
    arr = [-2, -1, 2, 1]
    k = 1
    test(arr, k, comment)

    comment = "LC TC; answer = 0"
    arr = []
    k = 0
    test(arr, k, comment)

    comment = "LC TC; answer = 4"
    arr = [1,-1,5,-2,3]
    k = 3
    test(arr, k, comment)
