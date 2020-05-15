"""
918. Maximum Sum Circular Subarray
Medium

Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)

Example 1:

Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3

Example 2:

Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10

Example 3:

Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4

Example 4:

Input: [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3

Example 5:

Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1
 
Note:

-30000 <= A[i] <= 30000
1 <= A.length <= 30000
"""

from typing import List

###############################################################################
"""
Solution: consider 2 cases and use Kadane's algo in each.

Problem can be split into 2 cases, and Kadane's algo can be applied to each
case. The final answer is the max of the two answers to the two cases.

(1) max subarray does not wrap around.
This can be solved using Kadane's algo.

(2) max circular subarray wraps around.
The part of the array outside the max circular subarray forms an array itself
that does not wrap around. Therefore, we can use Kadane's algo on it.
To maximize the circular subarray, we want to minimize its complement.

sum(max circ subarray) = total_sum - sum(min subarray that doesn't wrap around)

For the min subarray, we want to be careful to not include the final element
in the array. This is because the final element needs to be in the max circular
subarray in order for it to wrap around.

O(n) time
O(1) extra space
"""
class Solution:
    def maxSubarraySumCircular(self, arr: List[int]) -> int:
        n = len(arr)
        
        s = 0 # current sum for case 1
        t = 0 # current sum for case 2
        total_sum = 0

        res = float('-inf') # case 1: max sum
        res2 = -res # case 2: max sum excluding final element

        for i, x in enumerate(arr):
            total_sum += x
            s += x
            t += x

            if s > res:
                res = s
            if s < 0:
                s = 0

            if t < res2 and i < n-1: # exclude last element
                res2 = t
            if t > 0:
                t = 0

        return max(res, total_sum - res2)

"""
Solution 1b: same, but in case 2, instead of finding min sum, find max sum
of negative array (excluding final element).
"""
class Solution1b:
    def maxSubarraySumCircular(self, arr: List[int]) -> int:
        n = len(arr)
        
        s = 0 # current sum for case 1
        t = 0 # current sum of negative array for case 2
        total_sum = 0

        res = res2 = float('-inf') # max sums for case 1 and 2

        for i, x in enumerate(arr):
            total_sum += x
            s += x
            t -= x

            if s > res:
                res = s
            if s < 0:
                s = 0

            if t > res2 and i < n-1: # exclude last element
                res2 = t
            if t < 0:
                t = 0

        return max(res, total_sum + res2)

"""
LC example 2:

5 -3  5

max sum = 5 - 3 + 5 = 7
min sum excl last elt = -3
total sum = 7
total sum - min sum excl last elt = 7 - (-3) = 10

answer = max(7, 10) = 10

###
LC example 3:

3 -1  2 -1

max sum = 3 -1 + 2 = 4
min sum excl last elt = -1
total sum = 3
total sum - min sum excl last elt = 3 - (-1) = 4

answer = max(4, 4) = 4

###
LC example 5: (shows why we want to exclude final elt in case 2)

-2 -3 -1

max sum = -1
min sum excl last elt = -2 -3 = -5
total sum = -6
total sum - min sum excl last elt = -6 - (-5) = -1

answer = max(-1, -1) = -1
"""

###############################################################################
"""
Solution 2: consider 2 cases. For each case, solve using greedy approach:
find min or max diff of prefix sums...

O(n) time
O(n) extra space: for array of prefix sums
"""
class Solution2:
    def maxSubarraySumCircular(self, arr: List[int]) -> int:
        n = len(arr)

        min_pre = 0
        max_pre = 0

        max_diff = float('-inf') # case 1: max diff of prefix sums
        min_diff = float('inf') # case 2: min diff of prefix sums, excluding last elt

        pre = [0] * (n+1) # dummy 0 at start; indices shifted by 1 wrt "arr"

        for i, x in enumerate(arr):
            pre[i+1] = pre[i] + x

            if pre[i+1] - min_pre > max_diff:
                max_diff = pre[i+1] - min_pre

            if pre[i+1] - max_pre < min_diff and i < n-1: # exclude last elt
                min_diff = pre[i+1] - max_pre

            if pre[i+1] < min_pre:
                min_pre = pre[i+1]

            if pre[i+1] > max_pre:
                max_pre = pre[i+1]

        return max(max_diff, pre[-1] - min_diff)

"""
LC example 3:

0  1  2  3  index
3 -1  2 -1  

3  2  4  3  pre

max diff = pre[2] - pre[-1] = 4 - 0 = 4
min diff excl last elt = pre[1] - pre[0] = 2 - 3 = -1
total sum = pre[-1] = 3

total sum - min sum excl last elt = 3 - (-1) = 4

answer = max(4, 4) = 4

###
LC example 2:

0  1  2     index
5 -3  5

5  2  7     pre

max diff = pre[2] - pre[-1] = 7 - 0 = 7
min diff excl last elt = pre[1] - pre[0] = 2 - 5 = -3
total sum = pre[-1] = 7

total sum - min sum excl last elt = 7 - (-3) = 10

answer = max(7, 10) = 10
"""

###############################################################################
"""
Solution 3: brute force

O(n^2) time
O(1) extra space

TLE on test case of size ~10k
"""
class Solution3:
    def maxSubarraySumCircular(self, arr: List[int]) -> int:
        n = len(arr)
        res = float('-inf')
        #arr += arr
        
        for i in range(n): # start index
            s = 0
            
            for j in range(i, i+n):
                s += arr[j % n]
                #s += arr[j]

                if s > res:
                    res = s
                    
        return res         

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\narr = {arr}")

        res = sol.maxSubarraySumCircular(arr)

        print(f"\nres = {res}\n")


    sol = Solution() # Kadane's algo
    #sol = Solution1b() # same, but find max sum of negative array

    #sol = Solution2() # greedy; prefix sums
    
    #sol = Solution3() # brute force

    comment = "LC ex1; answer = 3"
    arr = [1,-2,3,-2]
    test(arr, comment)

    comment = "LC ex2; answer = 10"
    arr = [5,-3,5]
    test(arr, comment)

    comment = "LC ex3; answer = 4"
    arr = [3,-1,2,-1]
    test(arr, comment)

    comment = "LC ex4; answer = 3"
    arr = [3,-2,2,-3]
    test(arr, comment)

    comment = "LC ex5; answer = -1"
    arr = [-2,-3,-1]
    test(arr, comment)
