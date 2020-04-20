"""
56. Merge Intervals
Medium

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""

from typing import List

###############################################################################
"""
Solution 1: use sorting; assume "intervals" can't be modified

O(n log n) time: for sorting
O(n) extra space
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        s = sorted(intervals)
        merged = []
        
        prev_start, prev_end = s[0]

        for start, end in s:
            if start <= prev_end:
                prev_end = max(prev_end, end)
            else:
                merged.append([prev_start, prev_end])
                prev_start = start
                prev_end = end

        merged.append([prev_start, prev_end])

        return merged

# another way to write this
class Solution1b:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #if not intervals:
        #    return []

        s = sorted(intervals)
        merged = []

        for interval in s:
            # first interval, or start of interval > end of previous interval
			# so there is no overlap
            if (not merged) or (merged[-1][1] < interval[0]):
                merged.append(interval)

            else: # interval overlaps previous interval, so set the end
				# of the interval accordingly
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
        
###############################################################################
"""
Solution 2: use sorting; in-place version, modifies "intervals"

O(n log n) time: for sorting
O(1) extra space
"""
class Solution2:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort()
        
        prev_start, prev_end = intervals[0]
        count = 0 # index for merged intervals

        for start, end in intervals:
            if start <= prev_end:
                prev_end = max(prev_end, end)
            else:
                intervals[count] = [prev_start, prev_end]
                prev_start = start
                prev_end = end
                count += 1

        intervals[count] = [prev_start, prev_end]
        
        # remove the unneeded intervals at the end
        n_pop = len(intervals) - count - 1
        for _ in range(n_pop):
            intervals.pop()

        return intervals

# another way to write it
class Solution2b:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #if not intervals:
        #    return []

        intervals.sort()
        i = 0 # index for merged intervals

        for interval in intervals:
            # if intervals overlap
            # if start <= end of previous interval, set the end...
            if interval[0] <= intervals[i][1]:
                intervals[i][1] = max(intervals[i][1], interval[1])
            else: # no overlap
                i += 1
                intervals[i] = interval
        
        # remove the unneeded intervals at the end
        n_pop = len(intervals) - i - 1
        for _ in range(n_pop):
            intervals.pop()

        return intervals

###############################################################################
"""
Solution 3: Connected components...

NOT DONE
"""
class Solution3:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        pass

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):       
        print("="*80)
        if comment:
            print(comment)

        print(f"\n{arr}")
        
        res = s.merge(arr)

        print(f"\nresult = {res}")


    s = Solution()   # sorting
    s = Solution1b() # rewrite
    #s = Solution2()  # sorting; in-place
    #s = Solution2b() # rewrite
    #s = Solution3() # connected components; NOT DONE

    comment = "LC ex1; answer = [[1,6],[8,10],[15,18]]"
    arr = [[1,3],[2,6],[8,10],[15,18]]
    test(arr, comment)
   
    comment = "LC ex2; answer = [[1,5]]"
    arr = [[1,4],[4,5]]
    test(arr, comment)

    comment = "LC test case; answer = [[0,4]]"
    arr = [[1,4],[0,1]]
    test(arr, comment)

    comment = "LC test case; answer = [[1,4]]"
    arr = [[1,4],[2,3]]
    test(arr, comment)

    comment = "LC test case; answer = []"
    arr = []
    test(arr, comment)
