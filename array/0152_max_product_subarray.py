"""
152. Maximum Product Subarray
Medium

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

from typing import List

###############################################################################
"""
Solution: use running products from the left and right.  Reset the running
product for the term after a 0 is encountered.  Answer is max among all
running products.

If there's no zeros in the array, then the subarray with max product
must start with the first element or end with the last element.
Proof: Suppose we have a subarray from i to j that doesn't include the first
or last elements.  If arr[i-1] > 0 or arr[j+1] > 0, then we should expand
the subarray to include the ones that are positive to increase the product.
If both arr[i-1] < 0 and arr[j+1] < 0, then we can include both of them
and their negative signs cancel out.

Suppose there are zeros in the array.  They split up the array into
subarrays where we can apply the procedure from above.  While traversing
the array, if a zero is encountered, we reset the running product starting
with the term after the zero.

Another way to look at this is in terms of number of negative numbers in the
array.  If there are an even number of them, then the max product includes
the whole array.  If there are an odd number of them, then the max product
starts from the left and ends just before the last negative number,
or starts after the first negative number and ends at the last number.
If there are zeros in the array, apply this same logic to the subarrays
bounded by zero(s).

O(n) time
O(n) extra space
"""
class Solution: 
    def maxProduct(self, arr: List[int]) -> int:
        n = len(arr)
        left = arr[:] # assume we don't want to modify "arr"
        right = arr[:]

        for i in range(1, n):
            # if 0 was previous running product, 
            # reset running product with current term
            left[i] *= left[i-1] or 1 

        for i in reversed(range(1, n)):
            right[i-1] *= right[i] or 1

        return max(left + right) # max(union of sets)

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):       
        print("="*80)
        if comment:
            print(comment)

        res = s.maxProduct(arr)

        print(f"\n{arr}")
        print(f"\nresult = {res}")


    s = Solution() # running products from left and right

    comment = "LC example; answer = 6"    
    arr = [2,3,-2,4]
    test(arr, comment)

    comment = "LC ex2; answer = 0"
    arr = [-2,0,-1]
    test(arr, comment)

    comment = "LC test case; answer = -2"
    arr = [-2]
    test(arr, comment)

    comment = "LC test case; answer = 2"
    arr = [0,2]
    test(arr, comment)

    comment = "LC test case; answer = 24"
    arr = [-2,3,-4]
    test(arr, comment)

