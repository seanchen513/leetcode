"""
628. Maximum Product of Three Numbers
Easy

Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:

Input: [1,2,3]
Output: 6
 
Example 2:

Input: [1,2,3,4]
Output: 24
 
Note:

The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
"""

from typing import List
###############################################################################
"""
Solution: use sorting to find the 2 mins and 3 maxes needed.

The max product is either the product of the three largest numbers,
or the product of the largest number and the two negative numbers (if there
are any) that are greatest in absolute value.

O(n log n) time: due to sorting
O(n) extra space: for sorted array if we don't want to modify input
O(1) extra space: if sorting in-place using heapsort
    - quicksort is O(log n), and mergesort is O(n)
"""
class Solution:
    def maximumProduct(self, a: List[int]) -> int:
        n = len(a)
        s = sorted(a)

        return max(s[0]*s[1], s[n-2]*s[n-3] ) * s[n-1]

###############################################################################
"""
Solution: same idea as sol #1, but do a linear scan instead of sorting.

O(n) time
O(1) extra space
"""
class Solution2:
    def maximumProduct(self, a: List[int]) -> int:
        n = len(a)
        max1 = max2 = max3 = float('-inf') # let max1 >= max2 >= max3
        min1 = min2 = float('inf') # let min1 <= min2

        for i in range(n):
            x = a[i]
            if x >= max1:
                max3 = max2
                max2 = max1
                max1 = x
            elif x >= max2:
                max3 = max2
                max2 = x
            elif x >= max3:
                max3 = x

            if x <= min1:
                min2 = min1
                min1 = x
            elif x <= min2:
                min2 = x

        return max(min1*min2, max2*max3) * max1

###############################################################################
"""
Solution 3: same idea, but use heapq.nsmallest() and heapq.nlargest().

O(n) time
O(1) extra space

https://leetcode.com/problems/maximum-product-of-three-numbers/discuss/104739/Python-O(N)-and-1-line
"""
class Solution3:
    
    def maximumProduct(self, arr: List[int]) -> int:
        import heapq
        return max(arr) * max(a * b for a, b in 
            [heapq.nsmallest(2, arr), heapq.nlargest(3, arr)[1:]] )

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):       
        print("="*80)
        if comment:
            print(comment)

        res = s.maximumProduct(arr)

        print(f"\n{arr}")
        print(f"\nresult = {res}")


    #s = Solution() # use sorting
    #s = Solution2() # linear scan
    s = Solution3() # use heapq.nsmallest() and heapq.nlargest()

    comment = "LC ex1; answer = 6"    
    arr = [1,2,3]
    test(arr, comment)

    comment = "LC ex2; answer = 24"    
    arr = [1,2,3,4]
    test(arr, comment)

    comment = "LC test case; answer = -6"
    arr = [-1,-2,-3]
    test(arr, comment)

    comment = "LC test case; answer = 378"
    arr = [9,1,5,6,7,2]
    test(arr, comment)
