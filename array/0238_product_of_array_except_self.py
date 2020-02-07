"""
238. Product of Array Except Self
Medium

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""

from typing import List

###############################################################################
"""
Solution: calculate running products from left and right.  To do this in
O(1) space, other than the output array, use the output array itself to
precalculate the running product from the right side.  This can also be
done the other way.

Don't need to know the final running product for each direction.

O(n) time without using divison
O(1) extra space other than output array
"""
class Solution:
    def productExceptSelf(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = arr[:] # make copy

        # precalculate running products from right
        for i in reversed(range(1, n-1)):
            res[i] *= res[i+1]

        res[0] = res[1]

        left = arr[0]
        for i in range(1, n-1):
            res[i] = left * res[i+1]
            left *= arr[i]

        res[n-1] = left

        return res

###############################################################################
"""
Solution 2: use logs.  Assume array elements are positive integers.

It's possible to deal with zeros by checking for them.
It's possible to deal with negative numbers by tracking signs separately
from the logs.
It's possible to deal with floats, but have to deal with rounding issues.
"""
import math

class Solution2:
    def productExceptSelf(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0]*n

        for i in range(n):
            res[i] = math.log(arr[i])

        log_sum = sum(res)

        for i in range(n):
            res[i] = round((math.e)**(log_sum - res[i]))

        return res

###############################################################################

if __name__ == "__main__":
    def test(arr, k, comment=None):
        res = s.productExceptSelf(arr)
        
        print("="*80)
        if comment:
            print(comment)
            
        print(f"\n{arr}")
        print(f"\nresult = {res}")


    s = Solution()  # use running products from left and right
    #s = Solution2() # use logs
    

    comment = "LC example; answer = [24,12,8,6]"    
    arr = [1,2,3,4]
    test(arr, comment)

    comment = "LC test case; answer = [0,0]"
    arr = [0,0]
    test(arr, comment)
