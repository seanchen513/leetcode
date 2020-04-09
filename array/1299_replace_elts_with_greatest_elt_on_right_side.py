"""
1299. Replace Elements with Greatest Element on Right Side
Easy

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]

Constraints:

1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5
"""

from typing import List

###############################################################################
"""
Solution: traverse array in reverse, and track max so far.

O(n) time
O(1) extra space
"""
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mx = -1
        
        for i in range(len(arr) - 1, -1, -1):
            temp = max(mx, arr[i])
            arr[i] = mx
            mx = temp
            
        return arr
