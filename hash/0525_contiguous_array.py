"""
525. Contiguous Array
Medium

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.
"""

from typing import List

###############################################################################
"""
Solution: define "net" count as (count of 1) - (count of 0) from index 0 to i.
Use dict to map "net" to the first index where the "net" value is found.

There are equal numbers of 0's and 1's in a subarray [i,j] if the net count 
at j is the same as the net count at i-1.

Runtime: 820 ms, faster than 100.00% of Python3 online submissions
Memory Usage: 18.1 MB, less than 16.67% of Python3 online submissions
"""
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        net = 0 # net count of 1's minus 0's
        mx = 0 # max length of subarrays with equal numbers of 0's and 1's
        d = {0: -1} # maps net count to first index seen

        for i, x in enumerate(nums):
            if x == 1:
                net += 1
            else:
                net -= 1

            if net in d:
               l = i - d[net]
               if l > mx:
                   mx = l
            else:
                d[net] = i

        return mx

"""
Solution 1b: same as sol 1b, but instead of initializing d[0] = -1, we
check for a net count of 0 in the loop.
"""
class Solution1b:
    def findMaxLength(self, nums: List[int]) -> int:
        net = 0 # net count of 1's minus 0's
        mx = 0 # max length of subarrays with equal numbers of 0's and 1's
        d = {} # maps net count to first index seen

        for i, x in enumerate(nums):
            if x == 1:
                net += 1
            else:
                net -= 1

            if net == 0:
                mx = i + 1
            elif net in d:
               l = i - d[net]
               if l > mx:
                   mx = l
            else:
                d[net] = i

        return mx

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(arr)

        res = sol.findMaxLength(arr)

        print(f"\nres = {res}\n")


    sol = Solution() 
    sol = Solution1b() # same but check net count == 0 in loop

    comment = "LC ex1; answer = 2"
    arr = [0,1]
    test(arr, comment)

    comment = "LC ex2; answer = 2"
    arr = [0,1,0]
    test(arr, comment)

    comment = "LC TC; answer = 4"
    arr = [0,1,0,1]
    test(arr, comment)
    
    comment = "LC TC; answer = 6"
    arr = [0,0,1,0,0,0,1,1]
    test(arr, comment)
