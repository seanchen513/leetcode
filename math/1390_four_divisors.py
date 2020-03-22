"""
1390. Four Divisors
Medium

Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors.

If there is no such integer in the array, return 0.

Example 1:

Input: nums = [21,4,7]
Output: 32
Explanation:
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.

Constraints:

1 <= nums.length <= 10^4
1 <= nums[i] <= 10^5
"""

from typing import List

###############################################################################
"""
Solution: coutn and sum divisors by checking up to ~sqrt(n), early return,
memoized.

Perfect squares have an odd number of divisors, so they can't have 4 divisors.

O(n * sqrt(n)) time
O(n) extra space with memoization
O(1) extra space without memoization

This passes without memoization, but memoization makes LC runtime lower.

My post:
https://leetcode.com/problems/four-divisors/discuss/547281/Python3%3A-Count-and-sum-divisors-by-checking-up-to-~sqrt(n)-early-return-memoized

Runtime: 288 ms, faster than 100.00% of Python3 online submissions for Four Divisors.
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Four Divisors.
"""
import functools
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        @functools.lru_cache(None)
        def sum_div(n):
            count = 2 # for divisors 1 and n itself
            s = 1 + n # sum of divisors; not true for n=1, but dioesn
            
            end = int(n**0.5)
            if end*end == n: # cannot have 4 divisors
                return 0
            
            for i in range(2, end+1):
                if n % i == 0:
                    count += 2
                    s += i + n // i
                        
                    if count > 4:
                        return 0

            return s if count == 4 else 0

        return sum(sum_div(x) for x in nums)

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(arr)

        res = sol.sumFourDivisors(arr)

        print(f"\nres = {res}\n")


    sol = Solution()

    comment = "LC example; answer = 32"
    arr = [21,4,7]
    test(arr, comment)

    comment = "LC test case; answer = 0"
    arr = [1,2,3,4,5]
    test(arr, comment)
    
    comment = "LC test case; answer = 45"
    arr = [1,2,3,4,5,6,7,8,9,10]
    test(arr, comment)
