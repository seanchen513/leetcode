"""
1365. How Many Numbers Are Smaller Than the Current Number
Easy

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]

Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

Example 2:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]

Example 3:

Input: nums = [7,7,7,7]
Output: [0,0,0,0]

Constraints:

2 <= nums.length <= 500
0 <= nums[i] <= 100
"""

from typing import List
import collections
import bisect

###############################################################################
"""
Solution 1: use dict to count values.  Build running counts.
Return [count[x-1] for x in arr]

O(n + r) time, where n = length of input array, and r = range of values
O(n + r) extra space

Runtime: 44 ms, faster than 100.00% of Python3 online submissions
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
    def smallerNumbersThanCurrent(self, arr: List[int]) -> List[int]:
        count = collections.Counter(arr)

        # count = collections.defaultdict(int)
        # for x in arr:
        #     count[x] += 1

        for i in range(1,101):
            count[i] += count[i-1]
        
        return [count[x-1] for x in arr]

"""
Solution b: same as sol 1, but use "count" array instead of dict.
"""
class Solution1b:
    def smallerNumbersThanCurrent(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)
        
        count = [0] * 101 # 0 <= arr[i] <= 100
        
        for i, x in enumerate(arr):
            count[x] += 1

        for i in range(1,101):
            count[i] += count[i-1]

        for i, x in enumerate(arr):
            res[i] = count[x - 1] if x else 0

        return res

###############################################################################
"""
Solution 2: use sorting on given array, and dict.setdefault() on indices dict.

setdefault(key[, default])
If key is in the dictionary, return its value. If not, insert key with a value
of default and return default. "default" defaults to None.

Alternatively, build indices dict by setting indices[x] = i only the first 
time that the value x is encountered.

O(n log n) time
O(n) extra space for results
O(n) extra space for sorted 

Runtime: 40 ms, faster than 100.00% of Python3 online submissions
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
    def smallerNumbersThanCurrent(self, arr: List[int]) -> List[int]:
        indices = {}

        for i, x in enumerate(sorted(arr)):
            indices.setdefault(x, i)

        return [indices[x] for x in arr]

"""
Solution 2b: use sorting on given array, and build indices dict by
traversing sorted array in reverse.
"""
class Solution2b:
    def smallerNumbersThanCurrent(self, arr: List[int]) -> List[int]:
        s = sorted(arr)
        indices = {}
        
        #for i in range(len(s)-1, -1, -1):
        for i in reversed(range(len(s))):
            indices[s[i]] = i

        return [indices[x] for x in arr]

###############################################################################
"""
Solution 3: use sorting and binary search

Note:
bisect.bisect_left(s, x) is O(log n) binary search
s.index(x) is O(n) search (linear)

O(n log n) time
O(n) extra space for results
O(n) extra space for sorted array

Runtime: 48 ms, faster than 87.50% of Python3 online submissions
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions
"""
class Solution3:
    def smallerNumbersThanCurrent(self, arr: List[int]) -> List[int]:
        s = sorted(arr)
        res = []
        
        for x in arr:
            res.append( bisect.bisect_left(s, x) )
            #res.append( s.index(x))
        
        return res

"""
Solution 3b: concise version of sol 2.

Runtime: 44 ms, faster than 100.00% of Python3 online submissions
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions
"""
class Solution3b:
    def smallerNumbersThanCurrent(self, arr: List[int]) -> List[int]:
        s = sorted(arr)
        return [bisect.bisect_left(s, x) for x in enumerate(arr)]
        # return [s.index(x) for x in arr]

###############################################################################
"""
Solution 4: brute force

O(n^2) time
O(n) extra space for result

Runtime: 364 ms, faster than 50.00% of Python3 online submissions
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions
"""
class Solution4:
    def smallerNumbersThanCurrent(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)

        for i, x in enumerate(arr):
            res[i] = sum(y < x for y in arr)

        return res

"""
Solution 1b: concise version of sol 1.
"""
class Solution4b:
    def smallerNumbersThanCurrent(self, arr: List[int]) -> List[int]:
        return [sum(y < x for y in arr) for x in arr]


###############################################################################

if __name__ == "__main__":   
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(arr)

        res = sol.smallerNumbersThanCurrent(arr)

        print(f"\nres = {res}\n")

    sol = Solution() # use dict for running count
    #sol = Solution1b() # use array for running count

    #sol = Solution2() # use sorting and dict.setdefault()
    #sol = Solution2b()

    #sol = Solution3() # use sorting and bisect_left()
    #sol = Solution3b() # concise version

    #sol = Solution4() # brute force
    #sol = Solution4b() # concise version

    comment = "LC ex1; answer = [4,0,1,1,3]"
    arr = [8,1,2,2,3]
    test(arr, comment)

    comment = "LC ex2; answer = [2,1,0,3]"
    arr = [6,5,4,8]  
    test(arr, comment)
    
    comment = "LC ex3; answer = Output: [0,0,0,0]"
    arr = [7,7,7,7]
    test(arr, comment)
    