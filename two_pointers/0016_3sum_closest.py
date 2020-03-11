"""
16. 3Sum Closest
Medium

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

from typing import List
import itertools
import bisect

###############################################################################
"""
Solution: sort, then use 2 pointers with bisect.

O(n^2) time

Runtime: 44 ms, faster than 99.81% of Python3 online submissions
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
    def threeSumClosest(self, arr: List[int], target: int) -> int:
        arr.sort()
        
        n = len(arr)
        min_diff = closest = float('inf')
        
        for i in range(n-2):
            # Skip duplicates of values that have already been considered.
            if i > 0 and arr[i] == arr[i-1]:
                continue

            x = arr[i]
            start = i + 1
            end = n - 1

            while start < end:
                s = x + arr[start] + arr[end]
                diff = s - target

                if diff <= -min_diff:
                    threshold = arr[start] - min_diff - diff
                    start = bisect.bisect(arr, threshold, start, end)

                elif diff >= min_diff:
                    # Want largest value < threshold
                    threshold = arr[end] + min_diff - diff                    
                    end = bisect.bisect_left(arr, threshold, start, end) - 1

                elif diff < 0:
                    closest = s
                    min_diff = -diff
                    start += 1

                elif diff > 0:
                    closest = s
                    min_diff = diff
                    end -= 1
                else:
                    return s
        
        return closest
        
"""
Solution 1b: sort, then use 2 pointers w/o bisect.

No loops with thresholds:
Runtime: 76 ms, faster than 97.21% of Python3 online submissions
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions

Using loops with thresholds:
Runtime: 56 ms, faster than 97.51% of Python3 online submissions
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions
"""
class Solution1b:
    def threeSumClosest(self, arr: List[int], target: int) -> int:
        arr.sort()
        
        n = len(arr)
        min_diff = closest = float('inf')
        
        for i in range(n-2):
            # Skip duplicates of values that have already been considered.
            if i > 0 and arr[i] == arr[i-1]:
                continue

            x = arr[i]
            start = i + 1
            end = n - 1

            while start < end:
                s = x + arr[start] + arr[end]
                diff = s - target

                if diff <= -min_diff:
                    """
                    while arr[start] - arr[orig_start] <= (-min_diff) - diff
                    while arr[start] <= arr[orig_start] - min_diff - diff
                    """
                    # threshold = arr[start] - min_diff - diff
                    # while start < end and arr[start] <= threshold:
                    #     start += 1

                    start += 1

                elif diff >= min_diff:
                    """
                    while arr[orig_end] - arr[end] <= diff - min_diff
                    while arr[end] >= arr[orig_end] + min_diff - diff
                    """
                    #threshold = arr[end] + min_diff - diff
                    # while end > start and arr[end] >= threshold:
                    #     end -= 1

                    end -= 1

                elif diff < 0:
                    closest = s
                    min_diff = -diff
                    start += 1
                elif diff > 0:
                    closest = s
                    min_diff = diff
                    end -= 1
                else:
                    return s
        
        return closest

"""
Solution 1c: sort, then use 2 pointers w/o bisect.  Simple version.

Don't skip duplicates:
Runtime: 256 ms, faster than 28.86% of Python3 online submissions
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions

Skip duplicates:
Runtime: 184 ms, faster than 36.18% of Python3 online submissions
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions
"""
class Solution1c:
    def threeSumClosest(self, arr: List[int], target: int) -> int:
        arr.sort()
        
        n = len(arr)
        min_diff = closest = float('inf')
        
        for i in range(n-2):
            # Skip duplicates of values that have already been considered.
            if i > 0 and arr[i] == arr[i-1]:
                continue

            x = arr[i]
            start = i + 1
            end = n - 1

            while start < end:
                s = x + arr[start] + arr[end]
                diff = s - target

                if diff <= -min_diff:
                    start += 1
                elif diff >= min_diff:
                    end -= 1
                else:
                    closest = s
                    min_diff = abs(diff)
        
        return closest

###############################################################################
"""
Solution 2: brute force

O(n^3) time
TLE
"""
class Solution2:
    def threeSumClosest(self, arr: List[int], target: int) -> int:
        n = len(arr)
        closest = float('inf')

        for i in range(n-2):
            x = arr[i]

            for j in range(i+1, n-1):
                y = arr[j]

                for k in range(j+1, n):
                    s = x + y + arr[k]
                    if abs(s - target) < abs(closest - target):
                        closest = s

        return closest


"""
Solution 2b: brute force using itertools.combinations()

O(n^3) time
TLE
"""
class Solution2b:
    def threeSumClosest(self, arr: List[int], target: int) -> int:
        closest = float('inf')
        
        for p in itertools.combinations(arr, 3):
            s = sum(p)
            if abs(s - target) < abs(closest - target):
                closest = s

        return closest

"""
Solution 2c: brute force with some optimizations.

Fails if sort array and use "seen" set...
But passes (and much faster) if don't sort array and use "seen" set.
Probably missing test cases on LeetCode.

With sorting and no "seen" set:
Runtime: 2216 ms, faster than 5.02% of Python3 online submissions
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions
"""
class Solution2c:
    def threeSumClosest(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        
        closest = min_diff = float('inf')
        #seen = set()
        
        for i in range(n-2):
            if i > 0 and arr[i] == arr[i-1]:
                continue
            x = arr[i]

            for j in range(i+1, n-1):
                y = arr[j]
#                 if x + y in seen:
#                     continue
                    
#                 seen.add(x+y)

                for k in range(j+1, n):
                    s = x + y + arr[k]
                    diff = abs(s - target)
                    if diff == 0:
                        return s
                    elif diff < min_diff:
                        closest = s
                        min_diff = diff

        return closest

###############################################################################

if __name__ == "__main__":
    def test(arr, target, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(arr)
        print(f"target = {target}")

        res = sol.threeSumClosest(arr, target)

        print(f"\nres = {res}\n")


    sol = Solution() # use 2 pointers
    
    #sol = Solution2()
    #sol = Solution2b()

    comment = "LC example; answer = 2"
    arr = [-1,2,1,-4]
    target = 1
    test(arr, target, comment)

    comment = "LC test case; answer = 3"
    arr = [1,1,1,1]
    target = 0
    test(arr, target, comment)

    comment = "LC test case; answer = 82"
    arr = [1,2,4,8,16,32,64,128]
    target = 82
    test(arr, target, comment)
