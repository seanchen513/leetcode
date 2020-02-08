"""
560. Subarray Sum Equals K
Medium

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

from typing import List
import collections

"""
Solution: use runnings sums and track frequencies.

First, calculate running sums of array.
Then loop through array of running sums.
If current running sum is s[i], then we need another running sum s[j], j>=i, 
so that s[j] - s[i] = arr[i+1] + ... + arr[j] = k.  Or s[j] = s[i] + k.
We increment frequency counter for key s[i] + k in a dictionary "want".
This entry will be checked by future running sums.

We check subarrays ending at the current index by incrementing the
answer count by want[s[i]].  This is the number of previous running sums
that were looking for s[i] to help form k.

O(n) time
O(n) extra space: for dict
"""
class Solution:
    def subarraySum(self, arr: List[int], k: int) -> int:
        n = len(arr)
        count = 0

        # Running sums starting at arr[0].
        # s[0] is reserved to be 0 so this identity holds:
        # s[j+1] - s[i] == arr[i] + ... + arr[j] for j >= i
        s = [0]*(n+1)

        # dict of frequencies.
        # Key is desired running sum so that subtracting a previous running
        # sum gives k. 
        want = collections.defaultdict(int)

        for i in range(1, n+1):
            s[i] = s[i-1] + arr[i-1] # calculate current running sum
            
            want[k + s[i]] += 1

            count += want[s[i]]
            
        return count

###############################################################################
"""
Solution2: use running sums

O(n^2) time
O(n) extra space

TLE
"""
class Solution2:
    def subarraySum(self, arr: List[int], k: int) -> int:
        n = len(arr)
        count = 0

        s = [0]*(n+1)

        for i in range(1, n+1):
            s[i] = s[i-1] + arr[i-1]

        for start in range(n):
            for end in range(start+1, n+1):
                if s[end] - s[start] == k:
                    count += 1

        return count

###############################################################################
"""
Solution3: brute force

O(n^2) time
O(1) extra space
"""
class Solution3:
    def subarraySum(self, arr: List[int], k: int) -> int:
        n = len(arr)
        count = 0

        for start in range(n):
            s = 0

            for end in range(start, n):
                s += arr[end]
                if s == k:
                    count += 1

        return count

###############################################################################

if __name__ == "__main__":
    def test(arr, k, comment=None):       
        print("="*80)
        if comment:
            print(comment)

        res = s.subarraySum(arr, k)

        print(f"\n{arr}")
        print(f"\nk = {k}")
        print(f"\nresult = {res}")


    s = Solution() # use running sums with dict of frequencies
    s = Solution2() # use running sums
    s = Solution3() # brute force

    comment = "LC example; answer = 2"    
    arr = [1,1,1]
    k = 2
    test(arr, k, comment)

    comment = "LC test case; answer = 55"
    arr = [0,0,0,0,0,0,0,0,0,0]
    k = 0
    test(arr, k, comment)

    comment = "answer = 2: [2,3,4], [4,5]"
    arr = [1,2,3,4,5]
    k = 9
    test(arr, k, comment)
