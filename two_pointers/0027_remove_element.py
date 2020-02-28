"""
27. Remove Element
Easy

Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.

Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""

from typing import List

###############################################################################
"""
Solution 1: use pointer/index for position to put next array element not equal
to given value.

O(n) time
O(1) extra space
"""
class Solution:
    def removeElement(self, arr: List[int], val: int) -> int:
        n = len(arr)
        p = 0

        for i in range(n):
            if arr[i] != val:
                arr[p] = arr[i]
                p += 1

        return p

###############################################################################
"""
Solution 2: When given value encountered, copy over it with a value from the
end of the array.  Use pointer/index to track next index to copy from.

For when removals are rare, ie, few if any elements are equal to the given 
value.

Number of assignment operations equal to number of elements to remove.

O(n) time
O(1) extra space
"""
class Solution2:
    def removeElement(self, arr: List[int], val: int) -> int:
        n = len(arr) - 1
        i = 0

        while i < n:
            if arr[i] == val:
                arr[i] = arr[n]
                n -= 1
            else:
                i += 1

        return n + 1
        
###############################################################################

if __name__ == "__main__":
    def test(arr, val, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\narr = {arr}")
        print(f"val = {val}")
        
        res = sol.removeElement(arr, val)

        print(f"\narr = {arr}")
        print(f"res = {res}")
        

    sol = Solution()
    sol = Solution2() # when removals are rare

    comment = "LC ex1; answer = 2"
    arr = [3,2,2,3]
    val = 3
    test(arr, val, comment)

    comment = "LC ex2; answer = 5"
    arr = [0,1,2,2,3,0,4,2]
    val = 2
    test(arr, val, comment)

