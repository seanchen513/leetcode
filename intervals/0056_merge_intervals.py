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
Solution 1: sort intervals. Traverse intervals and compare left endpoint
to previous right endpoint.

O(n log n) time: for sorting
O(n) extra space: for output
O(1) extra space needed for sorting in-place
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort()
        res = [] # merged intervals
        
        # endpoints of current merged interval being built up
        left, right = intervals[0] 

        for a, b in intervals:
            if a <= right: # intervals overlap
                right = max(right, b)
            
            else: # output final merged interval, and start new interval
                res.append([left, right])
                left = a
                right = b
        
        # output final merged interval
        res.append([left, right])

        return res

"""
Solution 1b: another way to write same sol. Avoids using "left" and "right"
variables to track endpoints of merged intervals.
"""
class Solution1b:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort()
        res = [intervals[0]]

        for a, b in intervals:
            if res[-1][1] < a: # no overlap, so start new interval
                res.append([a, b])

            else: 
                # interval overlaps previous interval, so set the right 
                # endpoint of the merged interval accordingly
                res[-1][1] = max(res[-1][1], b)

        return res
        
###############################################################################
"""
Solution 2: use sorting. In-place version, modifies "intervals", using it
to store the output of merged intervals.

O(n log n) time: for sorting
O(1) extra space
"""
class Solution2:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort()
        
        # endpoints of current merged interval being built up
        left, right = intervals[0]
        i = 0 # index for merged intervals

        for a, b in intervals:
            if a <= right: # intervals overlap
                right = max(right, b)
            
            else:  # output final merged interval, and start new interval
                intervals[i] = [left, right]
                left = a
                right = b
                i += 1

        # output final merged interval
        intervals[i] = [left, right]
        
        # remove the unneeded intervals at the end
        n_pop = len(intervals) - i - 1
        for _ in range(n_pop):
            intervals.pop()

        return intervals

"""
Solution 2b: another way to write same sol. Avoids using "left" and "right"
variables to track endpoints of merged intervals.
"""
class Solution2b:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 0 # index for merged intervals

        for a, b in intervals:
            if a <= intervals[i][1]: # intervals overlap
                intervals[i][1] = max(intervals[i][1], b)

            else: 
                # current interval doesn't overlap previous merged interval
                # so start new interval
                i += 1
                intervals[i] = [a, b]
        
        # remove the unneeded intervals at the end
        n_pop = len(intervals) - i - 1
        for _ in range(n_pop):
            intervals.pop()

        return intervals

###############################################################################
"""
(NOT) Solution 3: brute force (no sorting)

NOT A SOLUTION. Example of how a naive brute-force attempt doesn't work.

Counter-example:
arr = [[2,3],[4,5],[6,7],[8,9],[1,10]]
answer = [[1,10]]
This attempt outputs: [[1,10], [4,5], [6,7], [8,9]]

O(n^2) time
O(n) extra space
"""
class Solution3:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        merged = set()
        res = []

        for i in range(n):
            if i in merged:
                continue

            left, right = intervals[i]

            for j in range(i+1, n):
                if j in merged:
                    continue

                a, b = intervals[j]

                if (left <= a <= right or left <= b <= right or
                    a <= left <= b or a <= right <= b
                    ):
                    left = min(left, a)
                    right = max(right, b)
                    merged.add(j)
                    merged.add(i)
                    
            print(merged)
            res.append([left, right])

        return res

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):       
        print("="*80)
        if comment:
            print(comment)

        print(f"\n{arr}")
        
        res = s.merge(arr)

        print(f"\nresult = {res}\n")


    s = Solution()   # sorting
    s = Solution1b() # rewrite
    
    #s = Solution2()  # sorting; in-place, merging intervals within input
    #s = Solution2b() # rewrite
    
    s = Solution3() # brute force

    comment = "LC ex1; answer = [[1,6],[8,10],[15,18]]"
    arr = [[1,3],[2,6],[8,10],[15,18]]
    test(arr, comment)
   
    comment = "LC ex2; answer = [[1,5]]"
    arr = [[1,4],[4,5]]
    test(arr, comment)

    comment = "LC TC; answer = [[0,4]]"
    arr = [[1,4],[0,1]]
    test(arr, comment)

    comment = "LC TC; answer = [[1,4]]"
    arr = [[1,4],[2,3]]
    test(arr, comment)

    comment = "LC TC; answer = []"
    arr = []
    test(arr, comment)

    """
    Counter-example to a brute-force attempt.
    """
    comment = "LC TC; answer = [[1,10]]"
    arr = [[2,3],[4,5],[6,7],[8,9],[1,10]]
    test(arr, comment)
