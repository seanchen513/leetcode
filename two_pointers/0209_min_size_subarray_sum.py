"""
209. Minimum Size Subarray Sum
Medium

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2

Explanation: the subarray [4,3] has the minimal length under the problem constraint.

Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
"""

from typing import List
import bisect

###############################################################################
"""
Solution: use two pointers.

Note: problem states s > 0. So for inner while, once i == j + 1, then
curr_sum = 0, so "curr_sum >= s" does not hold and loop ends. Therefore,
given s > 0 means we don't need the extra loop condition "i <= j".

O(n) time
O(1) extra space
"""
class Solution:
    def minSubArrayLen(self, s: int, arr: List[int]) -> int:
        n = len(arr)
        i = 0
        
        curr_sum = 0
        res = n + 1

        for j in range(n): # right endpoint
            curr_sum += arr[j]

            #while i <= j and curr_sum >= s:
            while curr_sum >= s: # if s > 0, don't need to check i <= j
                res = min(res, j - i + 1)
                curr_sum -= arr[i]
                i += 1

        if res == n + 1:
            return 0

        return res
        
###############################################################################
"""
Solution 2: use binary search...

Since condition is inclusive, we want to use bisect_left, not bisect (bisect_right).

LC example:
n = len(arr) = 6
n+1 = len(pre) = 7
s = 7

  2 3 1 2  4  3   arr
0 2 5 6 8 12 15   pre
0 1 2 3 4  5  6   i = index for pre

i = 0
pre[0] = 0
pre[0] + s = 0 + 7 = 7
bisect_left(7) gives j=4 since pre[4]=8 is first value of pre >= 7
subarray is 2+3+1+2 = 8 = 8 - 0 = pre[4] - pre[0]
length = j - i = 4 - 0 = 4

i = 4
pre[4] = 8
pre[4] + s = 8 + 7 = 15
bisect_left(15) gives j=6 since pre[6]=15 is first value of pre >= 15
subarray is 4+3 = 7 = 15 - 8 = pre[6] - pre[4]
length = j - i = 6 - 4 = 2

i = 5
pre[5] = 12
pre[5] + s = 12 + 7 = 19
bisect_left(19) gives j=len(pre)=n+1=7 (out of range) since 19 cannot be found in pre
Since j == n+1, we break from loop.


O(n log n) time
O(n) extra space: for array of prefix sums

"""
class Solution2:
    def minSubArrayLen(self, s: int, arr: List[int]) -> int:
        n = len(arr)
        res = n + 1

        # Calculate prefix sums
        pre = [0] * (n+1)
        for i, x in enumerate(arr):
            pre[i+1] = pre[i] + x

        for i in range(n+1):
            j = bisect.bisect_left(pre, pre[i] + s)

            if j < n + 1:
                res = min(res, j - i)
            else:
                break

        if res == n + 1:
            return 0

        return res

"""
LC TC; answer = 6
s = 80
arr = [10,5,13,4,8,4,5,11,14,9,16,10,20,8]

    10   5  13   4   8   4   5  11  14   9  16  10  20   8  arr
 0  10  15  28  32  40  44  49  60  74  83  99 109 129 137  pre

 0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  index i for pre
80  90  95 108 112 120 124 129 140 154 163 179 189 209 217  s + pre[i]

10  11  11  12  13  13  13 *13  15 ...                      j = bisect_left() 
10  10   9   9   9   8   7   6                              j - i

"""

###############################################################################
"""
Solution 3: brute force

O(n^2) time
O(1) extra space

TLE
"""
class Solution3:
    def minSubArrayLen(self, s: int, arr: List[int]) -> int:
        n = len(arr)
        res = n + 1

        for i in range(n):
            curr_sum = 0

            for j in range(i, n):
                curr_sum += arr[j]

                if curr_sum >= s:
                    res = min(res, j - i + 1)
                    break
        
        if res == n + 1:
            return 0

        return res

###############################################################################

if __name__ == "__main__":
    def test(s, arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\narr = {arr}")
        print(f"s = {s}")

        res = sol.minSubArrayLen(s, arr)

        print(f"\nres = {res}\n")


    sol = Solution() # use 2 pointers
    #sol = Solution2() # use binary search
    #sol = Solution3() # brute force

    comment = "LC example; answer = 2"
    s = 7
    arr = [2,3,1,2,4,3]
    test(s, arr, comment)

    comment = "LC TC; answer = 2"
    s = 15
    arr = [5,1,3,5,10,7,4,9,2,8]
    test(s, arr, comment)

    comment = "LC TC; answer = 0"
    s = 3
    arr = [1,1]
    test(s, arr, comment)

    comment = "LC TC; answer = 6"
    s = 80
    arr = [10,5,13,4,8,4,5,11,14,9,16,10,20,8]
    test(s, arr, comment)

    comment = "LC TC; answer = 3"
    s = 11
    arr = [1,2,3,4,5]
    test(s, arr, comment)

    comment = "LC TC; answer = 5"
    s = 15
    arr = [1,2,3,4,5]
    test(s, arr, comment)

    comment = "LC TC; answer = 0"
    s = 100
    arr = []
    test(s, arr, comment)

    comment = "LC TC; answer = 1"
    s = 4
    arr = [1,4,4]
    test(s, arr, comment)

    comment = "LC TC; answer = 1"
    s = 6
    arr = [10,2,3]
    test(s, arr, comment)
