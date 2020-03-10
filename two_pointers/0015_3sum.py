"""
15. 3Sum
Medium

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

from typing import List
import itertools

###############################################################################
"""
Solution: Sort array.  Loop through array, using each unique value as a 
target value.  Use two pointers, starting from index after target and last
index.  Move the pointers depending on the sum of the sum of their array
values compared to the target value.

O(n^2) time
O(1) extra space other than output.

Based on:
https://leetcode.com/problems/3sum/discuss/232712/Best-Python-Solution-(Explained)

Runtime: 592 ms, faster than 94.96% of Python3 online submissions for 3Sum.
Memory Usage: 16.2 MB, less than 100.00% of Python3 online submissions for 3Sum.
"""
class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        
        n = len(arr)
        res = []
        
        for i in range(n-2): # index for target number
            if arr[i] > 0: # can't have 3 positive values adding to 0
                break

            if i > 0 and arr[i] == arr[i-1]: # avoid duplicate target values
                continue

            target = -arr[i]
            start = i + 1
            end = n - 1

            while start < end:
                s = arr[start] + arr[end]
                
                if s < target:
                    start += 1
                elif s > target:
                    end -= 1
                else:
                    res.append( [arr[i], arr[start], arr[end]] )

                    # Move "start" and "end" pointers to avoid duplicates.
                    while start < n-1 and arr[start] == arr[start+1]:
                        start += 1
                    while end > 0 and arr[end] == arr[end-1]:
                        end -= 1
                    start += 1
                    end -= 1

        return res

###############################################################################
"""
Solution 2: same as sol 1, but use "seen" set for each iteration of inner loop.
Ie, treat as series of 2Sum problems.  Use set for pre-output to avoid
duplicate triplets.

O(n^2) time
O(n) extra space other than output: for "seen" set.

Runtime: 728 ms, faster than 82.82% of Python3 online submissions for 3Sum.
Memory Usage: 18 MB, less than 6.43% of Python3 online submissions for 3Sum.
"""
class Solution2:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        
        n = len(arr)
        res = set()

        for i in range(n-1):
            if arr[i] > 0: # can't have 3 positive values adding to 0
                break

            if i > 0 and arr[i] == arr[i-1]: # because...
                continue

            x = arr[i]
            seen = set()

            for j in range(i+1, n):
                y = arr[j]
                if y in seen:
                    res.add( (x, y, -x-y) )
                else:
                    seen.add( -x-y )

        return list(map(list, res))

###############################################################################
"""
Solution 3: brute force.

O(n^3) time

TLE
"""
class Solution3:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        s = sorted(arr)
        seen = set()
        
        n = len(s)
        
        for i in range(n):
            x = s[i]
            
            for j in range(i+1, n):
                y = s[j]

                for k in range(j+1, n):
                    if x + y + s[k] == 0:
                        if (x, y, s[k]) not in seen:
                            seen.add((x,y,s[k]))
                                
        return list(seen)

"""
Solution 3b: brute force using itertools.combinations()

O(n^3) time

TLE
"""
class Solution3b:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        res = set()

        for p in itertools.combinations(arr, 3):
            if sum(p) == 0:
                mn = min(p)
                mx = max(p)
                res.add((mn, -mn-mx, mx))
        
        return list(res)

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(arr)

        res = sol.threeSum(arr)

        print(f"\nres = {res}\n")


    sol = Solution() # use 2 pointers
    sol = Solution2() # use set; treat as series of 2Sum problems
    #sol = Solution3() # brute force; triple nested loop
    #sol = Solution3b() # brute force using itertools.combinations()

    comment = "LC example; answer = [[-1,0,1], [-1,-1,2]]"
    arr = [-1, 0, 1, 2, -1, -4]
    test(arr, comment)

    comment = "LC test case; answer = [[0,0,0]]"
    arr = [0, 0, 0, 0]
    test(arr, comment)

    comment = "LC test case; answer = []"
    arr = [0, 0]
    test(arr, comment)

    comment = "LC test case; answer = []"
    arr = [1, 2, -2, -1]
    test(arr, comment)

    # comment = "LC test case"
    # arr = [-7,-1,-13,2,13,2,12,3,-11,3,7,-15,2,-9,-13,-13,11,-10,5,-13,2,-12,0,-8,8,-1,4,10,-13,-5,-6,-4,9,-12,5,8,5,3,-4,9,13,10,10,-8,-14,4,-6,5,10,-15,-1,-3,10,-15,-4,3,-1,-15,-10,-6,-13,-9,5,11,-6,-13,-4,14,-3,8,1,-4,-5,-12,3,-11,7,13,9,2,13,-7,6,0,-15,-13,-11,-8,9,-14,1,11,-7,13,0,-6,-15,11,-6,-2,4,2,9,-15,5,-11,-11,-11,-13,5,7,7,5,-10,-7,6,-7,-11,13,9,-10,-9]
    # test(arr, comment)

    comment = "LC test case; answer = [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]"
    arr = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    test(arr, comment)

    comment = ""
    arr = [0]*100
    test(arr, comment)
    