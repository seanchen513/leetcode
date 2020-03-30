"""
1243. Array Transformation
Easy

Given an initial array arr, every day you produce a new array using the array of the previous day.

On the i-th day, you do the following operations on the array of day i-1 to produce the array of day i:

If an element is smaller than both its left neighbor and its right neighbor, then this element is incremented.
If an element is bigger than both its left neighbor and its right neighbor, then this element is decremented.
The first and last elements never change.
After some days, the array does not change. Return that final array.

Example 1:

Input: arr = [6,2,3,4]
Output: [6,3,3,4]
Explanation: 
On the first day, the array is changed from [6,2,3,4] to [6,3,3,4].
No more operations can be done to this array.

Example 2:

Input: arr = [1,6,3,4,3,5]
Output: [1,4,4,4,4,5]
Explanation: 
On the first day, the array is changed from [1,6,3,4,3,5] to [1,5,4,3,4,5].
On the second day, the array is changed from [1,5,4,3,4,5] to [1,4,4,4,4,5].
No more operations can be done to this array.
 
Constraints:

1 <= arr.length <= 100
1 <= arr[i] <= 100
"""

from typing import List

###############################################################################
"""
Solution: brute force

O(n) extra space
"""
class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        n = len(arr) - 1
        b_changed = True
        arr2 = arr[:]
        
        while b_changed:
            b_changed = False
            
            for i in range(1, n):
                if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                    arr2[i] -= 1
                    b_changed = True
                    
                elif arr[i] < arr[i-1] and arr[i] < arr[i+1]:
                    arr2[i] += 1
                    b_changed = True
                    
            arr = arr2[:]
            
        return arr

###############################################################################
"""
Solution: use prev, curr, and next variables instead of 2nd array.

O(1) extra space
"""
class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        n = len(arr) - 1
        b_changed = True

        while b_changed:
            b_changed = False
            curr = arr[0]
            next = arr[1]
            
            for i in range(1, n):
                prev = curr
                curr = next
                next = arr[i+1]

                if prev < curr > next:
                    arr[i] -= 1
                    b_changed = True

                elif prev > curr < next:
                    arr[i] += 1
                    b_changed = True

        return arr
