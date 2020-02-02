"""
494. Target Sum
Medium

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5

Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.

Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
"""

from typing import List

###############################################################################
"""
Solution 1: Recursion.
In this case:
1. index runs from len(nums)-1 to 0 (or < 0)
2. state vars are index "i" and current target sum "target"

O(2^n) time

LC: TLE
"""
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        def num_ways(i, target):
            #if i == 0:
            #    return (nums[0] == target) + (nums[0] == -target)
            if i < 0:
                return target == 0

            return num_ways(i-1, target - nums[i]) + num_ways(i-1, target + nums[i])

        return num_ways(len(nums)-1, S)

###############################################################################
"""
Solution 1b: Recursion.
In this case:
1. index runs from 0 to len(nums)-1.
2. state vars are index "i" and current sum "curr_sum".

O(2^n) time
"""
class Solution1b:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        def rec(i, curr_sum):
            if i == len(nums):
                return (curr_sum == S)
            
            pos = rec(i+1, curr_sum + nums[i])
            neg = rec(i+1, curr_sum - nums[i])

            return pos + neg

        return rec(0, 0)

"""
Solution 1c: Another way to write solution 1b.  
Use nonlocal count variable r ather than returning a count.
"""
class Solution1c:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        def rec(i, curr_sum):
            nonlocal count

            if i == len(nums):
                count += (curr_sum == S)
            else:            
                rec(i+1, curr_sum + nums[i])
                rec(i+1, curr_sum - nums[i])

        count = 0
        rec(0, 0)
        return count

###############################################################################
"""
Solution 2: Recursion w/ memoization. (based on solution 1)
In this case:
1. index runs from len(nums)-1 to 0 (or < 0)
2. state vars are index "i" and current target sum "target"
 
"""
class Solution2:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        def num_ways(i, target):
            nonlocal cache

            if (i, target) in cache:
                return cache[(i, target)]

            #if i == 0:
            #    return (nums[0] == target) + (nums[0] == -target)
            if i < 0:
                return target == 0

            pos_ways = num_ways(i-1, target - nums[i]) # take +nums[i] for sum
            neg_ways = num_ways(i-1, target + nums[i]) # take -nums[i] for sum
            
            cache[(i, target)] = pos_ways + neg_ways

            return pos_ways + neg_ways

        cache = {}
        return num_ways(len(nums)-1, S)

###############################################################################
"""
Solution 2b: Recursion w/ memoization. (based on solution 1b)
In this case:
1. index runs from 0 to len(nums)-1.
2. state vars are index "i" and current sum "curr_sum".

"""
class Solution2b:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        def rec(i, curr_sum):
            nonlocal cache

            if (i, curr_sum) in cache:
                return cache[(i, curr_sum)]

            if i == len(nums):
                return (curr_sum == S)

            pos = rec(i+1, curr_sum + nums[i])
            neg = rec(i+1, curr_sum - nums[i])

            cache[(i, curr_sum)] = pos + neg

            return pos + neg
        
        cache = {}
        return rec(0, 0)

###############################################################################
"""
Solution 3: Tabulation using dict that maps sums to their frequencies.
"""
class Solution3:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        from collections import defaultdict

        counts = defaultdict(int) # rather than plain dict to be careful
        counts[0] = 1

        for x in nums:
            new_counts = defaultdict(int) # make new object

            for old_sum, freq in counts.items():
                new_counts[old_sum + x] += freq
                new_counts[old_sum - x] += freq

            counts = new_counts
        
        return counts[S]


###############################################################################
"""
Solution 4: Naive iteration.

LC: TLE
"""
class Solution4:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)

        # offset index for "sums" by +1 so we can use sums = [0]
        # as a base case.
        sums = [0]

        for i in range(0, n): 
            sums = [x + nums[i] for x in sums] + [x - nums[i] for x in sums]
            
        return sum(x == S for x in sums)

###############################################################################
"""
Solution 5: Naive.  Use itertools.product() to generate all possible Cartesian 
products of [-1, 1], with length len(nums).  Use these to calculate sums.
This simulates n for loops.

O(n 2^n) time, where n = length of array

O(n 2^n) extra space potentially for the 2^n tuples of +/- 1 generated,
but itertools.product() probably generates them one at a time.
If that's the case, it's O(n) space.

LC: TLE
"""
import itertools
#import numpy as np

class Solution5:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)
        p = itertools.product([-1,1], repeat=n) # 2^n tuples

        ### If we can use numpy:
        #return sum(np.dot(signs, num) == S for signs in p)

        ### 1-liner for below:
        #return sum( sum(signs[i] * nums[i] for i in range(n)) == S for signs in p )

        count = 0

        for signs in p:
            if sum(signs[i] * nums[i] for i in range(n)) == S:
                count += 1

        return count

###############################################################################

if __name__ == "__main__":
    def test(arr, target_sum, comment=None):
        solutions = [Solution(), Solution1b(), Solution1c(),
            Solution2(), Solution2b(), Solution3(), Solution4()]

        res = [s.findTargetSumWays(arr, target_sum) for s in solutions]

        print("="*80)
        if comment:
            print(comment, "\n")
        print(arr, "\n")
        print(f"target sum = {target_sum}")

        print(f"\nSolutions: {res}\n")

        
    comment = "LC example; answer = 5; how many ways to choose 4 (+1) and 1 (-1)?"
    arr = [1, 1, 1, 1, 1] 
    target_sum = 3
    test(arr, target_sum, comment)

    comment = "LC test case that TLE's naive solution; answer = 0"
    arr = [29,6,7,36,30,28,35,48,20,44,40,2,31,25,6,41,33,4,35,38]
    target_sum = 35
    test(arr, target_sum, comment)

    comment = "LC test that TLE's simple recursion; answer = 7050"
    arr = [40,21,33,25,8,20,35,9,5,27,0,18,50,21,10,28,6,19,47,15]
    target_sum = 3
    test(arr, target_sum, comment)

    comment = "LC test case that TLE's naive iteration; answer = 6468"
    arr = [18,50,26,2,15,14,14,2,42,43,38,44,24,17,19,25,3,10,42,20]
    target_sum = 24
    test(arr, target_sum, comment)

    comment = "Trivial case"
    arr = []
    target_sum = 0
    test(arr, target_sum, comment)

    comment = "Trivial case"
    arr = []
    target_sum = 1
    test(arr, target_sum, comment)
