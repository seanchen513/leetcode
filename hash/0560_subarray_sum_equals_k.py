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

###############################################################################
"""
Solution: use dict to count prefix sums seen so far.

O(n) time
O(n) extra space: for dict
"""
class Solution:
    def subarraySum(self, arr: List[int], k: int) -> int:
        count = 0
        s = 0 # prefix sum

        d = collections.defaultdict(int)
        d[0] = 1 # so prefix sums equal to k are counted

        for x in arr:
            s += x
            
            # curr_sum - prev_sum = s - (s - k) = k
            count += d[s - k]
            
            # Be careful to only update dict after updating count.
            d[s] += 1

        return count

"""
Solution 1b: same as sol 1, but instead of initializing d[0] = 1, we check
if s == k in loop.
"""
class Solution1b:
    def subarraySum(self, arr: List[int], k: int) -> int:
        count = 0
        s = 0 # prefix sum

        d = collections.defaultdict(int)

        for x in arr:
            s += x
            
            if s == k: # count the prefix sum itself
                count += 1

            # curr_sum - prev_sum = s - (s - k) = k
            count += d[s - k]
            
            # Be careful to only update dict after updating count.
            d[s] += 1

        return count

###############################################################################
"""
Solution 2: use dict to count wanted prefix sums.

O(n) time
O(n) extra space: for dict
"""
class Solution2:
    def subarraySum(self, arr: List[int], k: int) -> int:
        count = 0
        s = 0 # prefix sum

        want = collections.defaultdict(int)
        want[k] = 1 # so prefix sums equal to k are counted

        for x in arr:
            s += x
            
            count += want[s]

            # If a future sum is k + s, then 
            # future_sum - curr_sum = (k + s) - s = k.
            # Be careful to only update dict after updating count.
            want[k + s] += 1
            
        return count

"""
Solution 2b: same as sol 2, but instead of initializing want[k] = 1,
we check if s == k in loop.
"""
class Solution2b:
    def subarraySum(self, arr: List[int], k: int) -> int:
        count = 0
        s = 0 # prefix sum

        want = collections.defaultdict(int)
        #want[k] = 1 # so prefix sums equal to k are counted

        for x in arr:
            s += x
            
            if s == k: # count prefix sum itself
                count += 1

            count += want[s]

            # If a future sum is k + s, then 
            # future_sum - curr_sum = (k + s) - s = k.
            # Be careful to only update dict after updating count.
            want[k + s] += 1
            
        return count

"""
Solution 2c: use dict to count wanted prefix sums.

If current prefix sum is s[j], then we need another prefix sum s[i], i < j, 
so that s[j] - s[i] = arr[i+1] + ... + arr[j] = k.  Or s[j] = s[i] + k.
We increment count for key s[j] + k in a dictionary "want".
This entry will be checked by future running sums.

We check subarrays ending at the current index by incrementing the
answer count by want[s[i]].  This is the number of previous running sums
that were looking for s[i] to help form k.

O(n) time
O(n) extra space: for dict
"""
class Solution2c:
    def subarraySum(self, arr: List[int], k: int) -> int:
        n = len(arr)
        count = 0

        # Prefix sums: running sums starting at arr[0].
        # s[0] is reserved to be 0 so this identity holds:
        # s[j+1] - s[i] == arr[i] + ... + arr[j] for j >= i
        s = [0] * (n+1)

        # dict of counts.
        # Keys are desired prefix sums so that subtracting a previous 
        # prefix sum gives k. 
        want = collections.defaultdict(int)

        for i in range(1, n+1):
            s[i] = s[i-1] + arr[i-1]
            
            want[k + s[i]] += 1

            count += want[s[i]]
            
        return count

###############################################################################
"""
Solution 3: brute force using prefix sums.

O(n^2) time
O(n) extra space

TLE
"""
class Solution3:
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
Solution 4: brute force

O(n^2) time
O(1) extra space
"""
class Solution4:
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
        print(f"k = {k}")
        print(f"\nresult = {res}\n")


    s = Solution() # use dict to count prefix sums seen so far
    s = Solution1b() # same but check if sum == k in loop

    #s = Solution2() # use dict to count wanted prefix sums
    #s = Solution2b() # same but check if sum == k in loop
    #s = Solution2c() # same, but use shifted prefix sum array as well

    #s = Solution3() # brute force use prefix sums
    #s = Solution4() # brute force

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

    comment = "answer = 0"
    arr = [1]
    k = 0
    test(arr, k, comment)
