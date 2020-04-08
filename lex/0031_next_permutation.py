"""
31. Next Permutation
Medium

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

from typing import List

###############################################################################
"""
Solution:

O(n) time, where n = len(nums)
O(1) extra space
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        
        n = len(nums)
        
        # From right to left, find first index where value is < previous value.
        i = n - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        # If no such index was found, then values are in mono decreasing
        # order, eg, [3,2,1], so reverse nums to mono increasing order,
        # which gives the lowest possible order.
        if i == -1:
            nums[:] = nums[::-1]
            return 
        
        # From right to left, find the first value that is > the one found above.
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
            
        # Swap the two values.
        nums[i], nums[j] = nums[j], nums[i]
        
        # Reverse the part of nums after the original position of the first 
        # value, ie, the leftmost position.
        nums[i+1:] = nums[:i:-1]
        
        return
        
###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(arr)

        sol.nextPermutation(arr)

        print(f"\nAFTER: {arr}\n")


    sol = Solution()

    comment = "LC ex1; answer = 1,3,2"
    arr = [1,2,3]
    test(arr, comment)

    comment = "LC ex2; answer = 1,2,3"
    arr = [3,2,1]
    test(arr, comment)

    comment = "LC ex3; answer = 1,5,1"
    arr = [1,1,5]
    test(arr, comment)

    comment = "single element"
    arr = [1]
    test(arr, comment)

    comment = "all elements equal"
    arr = [1,1,1,1,1]
    test(arr, comment)

    comment = "increasing order"
    arr = [1,2,3,4,5]
    test(arr, comment)

    comment = "decreasing order"
    arr = [5,4,3,2,1]
    test(arr, comment)
