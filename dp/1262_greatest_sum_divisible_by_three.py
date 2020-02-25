"""
1262. Greatest Sum Divisible by Three
Medium

Given an array nums of integers, we need to find the maximum possible sum of elements of the array such that it is divisible by three.

Example 1:

Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).

Example 2:

Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.

Example 3:

Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
 
Constraints:

1 <= nums.length <= 4 * 10^4
1 <= nums[i] <= 10^4
"""

from typing import List
import heapq

###############################################################################
"""
Solution: tabulation using state variables to track max sums up to index i
with remainders 0, 1, and 2.

O(n) time
O(1) extra space
"""
class Solution:
    def maxSumDivThree(self, arr: List[int]) -> int:
        max0 = max1 = max2 = float('-inf') # max sums with mod 0, 1, 2

        for x in arr:
            if x % 3 == 0:
                max0 = max(max0 + x, x) # in case max0 was -inf before
                max1 += x
                max2 += x

            elif x % 3 == 1:
                # The sole "x" term is in case max0 and max1 are -inf.
                max0, max1, max2 = max(max0, max2 + x), \
                    max(max1, max0 + x, x), \
                    max(max2, max1 + x)
            
            else: # rem == 2:
                # The sole "x" term is in case max0 and max2 are -inf.
                max0, max1, max2 = max(max0, max1 + x), \
                    max(max1, max2 + x), \
                    max(max2, max0 + x, x)

            # print(f"\nmax0 = {max0}")
            # print(f"max1 = {max1}")
            # print(f"max2 = {max2}")

        return max0 if max0 > float('-inf') else 0

###############################################################################
"""
Solution 2:

O(n) time
O(1) extra space

https://leetcode.com/problems/greatest-sum-divisible-by-three/discuss/431077/JavaC%2B%2BPython-One-Pass-O(1)-space
"""
class Solution2:
    def maxSumDivThree(self, arr: List[int]) -> int:
        seen = [0,0,0]

        for x in arr:
            for i in seen[:]:
                seen[(i + x) % 3] = max(seen[(i + x) % 3], i + x)

        return seen[0]

###############################################################################
"""
Solution 3: math.

Let s = sum of the array.  Look at s % 3.  There are 3 cases:

(1) s % 3 == 0: then s itself is the answer.

(2) s % 3 == 1: look at the smallest number with mod 1, and look at the sum
of the two smallest numbers with mod 2.  Subtract the smallest of these two
from the total sum.

(3) s % 3 == 2: look at the smallest number with mod 2, and look at the sum
of the two smallest numbers with mod 1.  Subtract the smallest of these two
from the total sum.

Notes:
1. The two loops can be combined, but I kept them separate to minimize 
operations per function call.
2. Two of the cases can be combined, but I kept them separate for clarity.
3. Code can be condensed using min() and heapq.nsmallest(), but I'm not sure 
of the time and space complexities of the latter.

O(n) time
O(1) extra space
"""
class Solution3:
    def maxSumDivThree(self, arr: List[int]) -> int:
        s = sum(arr)
        if s % 3 == 0:
            return s
        
        # smallest numbers with mod 1 and 2, resp.
        min1 = min2 = float('inf')
        
        if s % 3 == 1:
            min2b = float('inf') # 2nd smallest number with mod 2

            for x in arr:
                if x % 3 == 1 and x < min1:
                    min1 = x

                if x % 3 == 2:
                    if x < min2:
                        min2, min2b = x, min2
                    elif x < min2b:
                        min2b = x

            return max(s - min1, s - min2 - min2b)

        if s % 3 == 2:
            min1b = float('inf') # 2nd smallest number with mod 2
            
            for x in arr:
                if x % 3 == 1:
                    if x < min1:
                        min1, min1b = x, min1
                    elif x < min1b:
                        min1b = x
                    
                if x % 3 == 2 and x < min2:
                    min2 = x
            
            return max(s - min2, s - min1 - min1b)                    

                    
"""
Solution 3b: same idea as sol 3, but use min() and heapq.nsmallest().
"""
class Solution3b:
    def maxSumDivThree(self, arr: List[int]) -> int:
        s = sum(arr)
        if s % 3 == 0:
            return s
        
        if s % 3 == 1:
            # Note: min1 might not have remainder 1.
            min1 = min(arr, key=lambda x: ( ((x+2) % 3), x) )
            
            # Note: min2 might contain numbers that don't have remainder 2.
            min2 = heapq.nsmallest(2, arr, key=lambda x: (-(x % 3), x))
            
            # print(f"\nmin1 = {min1}")
            # print(f"min2 = {min2}")

            return max(s - min1, s - sum(min2))
        
        if s % 3 == 2:
            min1 = heapq.nsmallest(2, arr, key=lambda x: ( ((x+2) % 3), x) )
            min2 = min(arr, key=lambda x: (-(x % 3), x))

            # print(f"\nmin1 = {min1}")
            # print(f"min2 = {min2}")

            return max(s - sum(min1), s - min2)

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(arr)

        res = sol.maxSumDivThree(arr)

        print(f"\nres = {res}")


    sol = Solution() # tabulation using max0, max1, max2
    #sol = Solution2() # concise using seen[], but O(n) space
    sol = Solution3() # math sol
    #sol = Solution3b() # math sol, concise using heapq.nsmallest() and min()

    comment = "LC ex1; answer = 18"
    arr = [3,6,5,1,8]
    test(arr, comment)

    comment = "LC ex2; answer = 0"
    arr = [4]
    test(arr, comment)

    comment = "LC ex3; answer = 12"
    arr = [1,2,3,4,4]
    test(arr, comment)

    comment = "; answer = "
    arr = [1,1]
    test(arr, comment)

    comment = "LC test case; answer = 84"
    arr = [2,19,6,16,5,10,7,4,11,6]
    test(arr, comment)

    comment = "LC test case; answer = 195"
    arr = [2,3,36,8,32,38,3,30,13,40]
    test(arr, comment)

    comment = "mod 2, only one number with mod 1"
    arr = [1,3,2,2]
    test(arr, comment)
