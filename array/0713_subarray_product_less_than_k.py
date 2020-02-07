"""
713. Subarray Product Less Than K
Medium

Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
"""

from typing import List


###############################################################################
"""
Solution: Two pointers.  Loop through the right one, and increment the left
one when needed to decrease the product.

Start with subarray of one element.  Have left = right, and only one nonempty
subset can be formed.

Each time we have a valid subarray and extend it to by one element to
a larger subarray.

Case 1: the larger subarray has product < k.
The number of new subsets formed is equal to the length of the larger subarray.
These new subsets all include the new element, and all but one subset starts 
with one of the elements of the old subarray.  There is also the subset of the 
new element by itself.

Case 2: the larger subarray has product >= k.
We increment the left pointer until the product of new subarray is < k.
The number of new subsets formed is equal to the length of the new subarray.
They all start with the first element of the new subarray.

    LC example: [10,5,2,6], k=100.  
    When right=2, right elt is 2, left=0, left elt is 10.  Product is 100.
    Left incremented to 1.  New subarray is [5,2].  New subsets formed are
    {5} and {5,2}.

If we encounter a single element that is >= k, then in the "while" loop,
we end up with p = 1 (so we're restarting the product) and left = right + 1.
This leads to "res += 0".  No new subsets are formed because the new 
element that is >= k cannot be included in any new subsets.

O(n) time: the inner loop executes at most n times since "left" can be
incremented at most n times total.

O(1) extra space.
"""
class Solution:
    def numSubarrayProductLessThanK(self, arr: List[int], k: int) -> int:
        if k <= 0: return 0

        n = len(arr)
        p = 1 # product
        left = 0 # left index
        res = 0 # result

        for right in range(n):
            p *= arr[right]

            while p >= k:
                p //= arr[left]
                left += 1

            res += right - left + 1
        
        return res

"""
Example: arr = [10, 5, 2, 6]

right = 0
p = 10
interval [0,0] with values [10]
res += 0 - 0 + 1 # Add one set: {10}

right = 1
p = 10*5 = 50
interval [0,1] with values [10,5]
res += 1 - 0 + 1 # Add two sets: {5}, {10,5}

right = 2
p = 50*2 = 100 > k
    p //= 10, so p = 10
    left += 1, so left = 1
interval [1,2] with values [5,2]
res += 2 - 1 + 1 # Add one set: {5,2}

right = 3
p = 10*6 = 60
interval [1,3] with values [5,2,6]
res += 3 - 1 + 1 = 3 # Add 3 sets: {6}, {2,6}, {5,2,6}
"""

###############################################################################
"""
Solution 2: binary search on prefix sums of logs.

This uses the same idea of counting sets as in the "two pointers" method,
but finds the maximal subsets before the product turns too big by
looking at logs of the array values and their running sums (prefix sums).

O(n log n): since we loop through an array, using O(n) bisection each time.
O(n) extra space: for the prefix array

Method:
Apply log to each element of the array and also to k.  Calculate the running
sums of the log array (prefix array).  Since original array elts are pos ints, 
their logs are >= 0.  So the running sums form a non-strictly increasing 
sequence.  In particular, they are sorted, so the bisection method applies.

If we want relation 
(1) arr[i] + ... + arr[j] = prefix[j+1] - prefix[i],
let
prefix[0] = 0, 
prefix[1] = arr[0], 
prefix[2] = arr[1] + arr[0], 
..., 
prefix[n] = arr[0] + .. + arr[n-1].
Disadvantage is that the index "j" is shifted.

If we want relation 
(2) arr[i] + ... + arr[j] = prefix[j] - prefix[i] + arr[i],
let:
prefix[0] = arr[0],
prefix[1] = arr[0] + arr[1],
...,
prefix[n-1] = arr[0] + ... + arr[n-1].
Disadvantage is that we need to deal with an extra term.

For each start index, the maximal subarray has the largest end index j
such that arr[i] + ... + arr[j] < k.  (The logs have been applied to "arr".)  

We can find this j quickly by doing a bisection search for the following to
find an insertion point that comes after j:

(1) Using relation 1:
arr[i] + ... + arr[j] = prefix[j+1] - prefix[i] < k
prefix[j+1] = prefix[i] + k
Target for bisection search is prefix[i] + k - epsilon.
(Right) bisection returns j2=j+2.

(2) Using relation 2:
arr[i] + ... + arr[j] = prefix[j] - prefix[i] + arr[i] < k
prefix[j] < prefix[i] - arr[i] + k
Target for bisection search is prefix[i] - arr[i] + k - epsilon.
(Right) bisection returns j1=j+1.

Python's bisect.bisect() finds the insertion point that comes after j.
Furthermore, when using relation 1, this is shifted an extra one.

The number of new subsets that start with arr[i] is:
(1) j - i + 1  = (j+2) - i - 1 = j2 - i - 1
(2) j - i + 1 = (j+1) - i = j1 - i

Example w/o logs: arr = [1,2,3,4,5], k=7, i=0.
Maximal subarray is [1,2,3], with actual ending index 2.
New subsets formed are [1], [1,2], and [1,2,3]
Number of these is end_index - start_index + 1 = 2 - 0 + 1 = 3.

(1) j2=4 (elt 5).  Numer of new subsets = j2 - 0 - 1 = 4 - 0 - 1 = 3.

(2) j1 = 3 (elt 4).  Number of new subsets = j1 - i = 3 - 0 = 3.

"""
class Solution2:
    def numSubarrayProductLessThanK(self, arr: List[int], k: int) -> int:
        if k == 0: return 0

        from math import log
        from bisect import bisect
        k = log(k)

        n = len(arr)
        prefix = [0]*(n+1)
        prefix[0] = 0 
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + log(arr[i-1])
        
        count = 0
        for i in range(n):
            target = prefix[i] + k - 1e-12
            j = bisect(prefix, target, i) # i is low index for bisection
            count += j - i - 1

        return count

"""
Solution 2b: same as sol 2, but use relation 2.

arr[i] + ... + arr[j] = prefix[j] - prefix[i] + arr[i] < k
prefix[j] < prefix[i] - arr[i] + k
Target for bisection search is prefix[i] - arr[i] + k - epsilon.
"""
class Solution2b:
    def numSubarrayProductLessThanK(self, arr: List[int], k: int) -> int:
        if k == 0: return 0

        from math import log
        from bisect import bisect
        k = log(k)

        n = len(arr)
        prefix = [0]*n
        prefix[0] = log(arr[0])
        for i in range(1, n):
            prefix[i] = prefix[i-1] + log(arr[i])
        
        count = 0
        for i in range(n):
            target = prefix[i] - log(arr[i]) + k - 1e-12
            j = bisect(prefix, target, i) # i is low index for bisection
            
            #if j >= n or prefix[j] >= target:
            #    j -= 1
            
            count += j - i

        return count

###############################################################################
"""
Solution 3: two pointers, my first attempt

Difference from other "two pointers" solution is that the number of new 
subsets isn't calculated until the maximal subarrays are found.  However,
some correction in the counting is needed due to counting overlaps.

O(n) time
O(1) extra space

The execution time on LeetCode is similar to the other "two pointers"
solution.

Runtime: 1292 ms, faster than 23.28% of Python3 online submissions
Memory Usage: 17 MB, less than 11.11% of Python3 online submissions
"""
class Solution3:
    def numSubarrayProductLessThanK(self, arr: List[int], k: int) -> int:
        n = len(arr)
        start, end = 0, 0
        res = 0
        p = 1

        while start < n and end < n:
            p *= arr[end]

            if p < k: # product is smaller than bound, so keep going
                end += 1
            else:
                # we're stuck at a single number > bound, so skip it
                if start == end:
                    start += 1
                    end = start
                    p = 1
                    continue

                # list of length m has m*(m+1)//2 nonempty contiguous sublists
                m = end - start
                res += m*(m+1)//2
                
                while start < end and p >= k:
                    p //= arr[start]
                    start += 1

                # boundary case: start == end, m == 0, so below will subtract
                # 0 from res, and divide so p will be 1.

                # remove overlaps
                m = end - start
                res -= m*(m+1)//2

                p //= arr[end]

        m = end - start
        res += m*(m+1)//2   

        return res

###############################################################################

if __name__ == "__main__":
    def test(arr, k, comment=None):       
        print("="*80)
        if comment:
            print(comment)

        res = s.numSubarrayProductLessThanK(arr, k)

        print(f"\n{arr}")
        print(f"\nk = {k}")
        print(f"\nresult = {res}")


    s = Solution() # 2ptr
    #s = Solution2() # binary search on prefix sums of logs.
    #s = Solution2b() # same as sol#2, but use relation 2
    #s = Solution3() # 2ptr; my first attempt

    comment = "LC example; answer = 8"    
    arr = [10,5,2,6]
    k = 100
    test(arr, k, comment)

    comment = "LC test case; answer = 0"
    arr = [1,2,3]
    k = 0
    test(arr, k, comment)

    comment = "answer = 25"
    arr = [1,1,1,1,8,1,1,1,1,1]
    k = 5
    test(arr, k, comment)

    comment = "answer = 19"
    arr = [1,1,8,1,1,1,8,1,1,1,1]
    k = 5
    test(arr, k, comment)

    comment = "answer = 6"
    arr = [8,1,1,1,8]
    k = 5
    test(arr, k, comment)
