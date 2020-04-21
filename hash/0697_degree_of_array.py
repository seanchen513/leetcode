"""
697. Degree of an Array
Easy

Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2

Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6

Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""

from typing import List
import collections

###############################################################################
"""
Solution: use dicts to count elts, and get first and last occurences of each elt.
Find max count. For keys/elts w/ max count, find min last - first + 1.

O(n) time
O(n) extra space
"""
class Solution:
    def findShortestSubArray(self, arr: List[int]) -> int:
        d = {}
        first = {}
        last = {}
                    
        for i, x in enumerate(arr):
            if x not in first:
                first[x] = i
            
            last[x] = i
            
            d[x] = d.get(x, 0) + 1
        
        max_count = max(d.values()) # ie, degree of "arr"        
        min_diff = len(arr)
        
        for k, cnt in d.items():
            if cnt == max_count:
                min_diff = min(min_diff, last[k] - first[k])
            
        return min_diff + 1 # min length

        #return 1 + min(last[k] - first[k] for k, cnt in d.items() if cnt == max_count)

###############################################################################
"""
Solution 2: use dict that maps each elt to a list of their indices.

O(n) time
O(n) extra space
"""
class Solution2:
    def findShortestSubArray(self, arr: List[int]) -> int:
        d = collections.defaultdict(list)
                    
        for i, x in enumerate(arr):
            d[x].append(i)
        
        max_count = len(max(d.values(), key=len)) # ie, degree of "arr"
        min_diff = len(arr)
        
        for indices in d.values():
            if len(indices) == max_count:
                min_diff = min(min_diff, indices[-1] - indices[0])
            
        return min_diff + 1 # min length

        #return 1 + min(ind[-1] - ind[0] for ind in d.values() if len(ind) == max_count)

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\n{arr}")
        
        res = s.findShortestSubArray(arr)

        print(f"\nresult = {res}\n")


    s = Solution() # use dicts for counts, first, and last
    s = Solution2() # use dict that maps each elt to a list of their indices.

    comment = "LC ex1; answer = 2"
    arr = [1, 2, 2, 3, 1]
    test(arr, comment)

    comment = "LC ex2; answer = 6"
    arr = [1,2,2,3,1,4,2]
    test(arr, comment)
