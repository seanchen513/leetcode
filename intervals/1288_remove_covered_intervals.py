"""
1288. Remove Covered Intervals
Medium

Given a list of intervals, remove all intervals that are covered by another interval in the list. Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

After doing so, return the number of remaining intervals.

Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2

Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.

Constraints:

1 <= intervals.length <= 1000
0 <= intervals[i][0] < intervals[i][1] <= 10^5
intervals[i] != intervals[j] for all i != j
"""

from typing import List


###############################################################################
"""
Solution: sort by increasing left endpoint, then by decreasing right endpoint.

*** Sorted in this way, no interval can cover a previous interval.

This solution is the same as sol 2, but we don't have to track or check
"left" here. Ie, we don't have to worry about case 2 in sol 2, where the 
prior interval is extended.

Whenever current right most bound < next interval's right bound, it means 
current interval can NOT cover next interval. So update right most bound and 
increase counter by 1.

        right
1---------3
     2-----------4
                 b

        right
1---------3
     2----3   COVERED
          b

If consecutive left endpoints are equal, then right endpoints are decreasing,
so we cannot have a new interval. This is why we sort by dec right endpt.

        right
1---------3
1----2
     b

O(n log n) time: for sorting
O(1) extra space: if sort in-place
"""
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        right = -1
        count = 0
        
        intervals.sort(key=lambda a: (a[0], -a[1]))

        for _, b in intervals:
            if b > right:
                count += 1
                right = b

        return count

###############################################################################
"""
Solution 2: sort by left endpoint, then right endpoint (ie, regular sort).

[a,b), [x,y]

Assume a <= x (in particular, if these are consecutive intervals in sorted
list of intervals).

(1) If y <= b, then [x,y) is covered by [a,b). New interval covered by old.
Variables "left" and "right" are not updated.

Suppose b < y:

(2) If a = x, then [a,b) is covered by [x, y). Old interval covered by new.
Variable "left" stays the same, but "right" is updated.

(3) If a < x, then neither interval covers the other.
Variables "left" and "right" are both updated.

So 3 cases (some overlap):
(1) a <= x and y <= b: new interval coverd by old
(2) a = x  and b < y: old interval covered by new
(3) a < x  and b < y: neither interval covers the other; have a new uncovered interval.

Variable "left" is updated only when a new uncovered interval is found
(and not because an old one is extended). It isn't always the max seen so far.

Variable "right" is updated in the previous case as well as when an old
interval is extended. It is always updated to be the max seen so far.

Examples for (1):

          right
1-----------4
    2---3       left is not updated!

1-----------4
    2-------4   left is not updated!

Example for (2):

      right
1-------3
1-----------4   right is updated
            b

Example for (3):

      right
1-------3
    2-------4   left and right are updated
            b

O(n log n) time: for sorting
O(1) extra space: if sort in-place
"""
class Solution2:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        left = -1 # left endpoint of previous interval
        right = -1 # right endpoint of previous interval

        intervals.sort()
        count = 0

        for a, b in intervals:
            if a > left and b > right:
                count += 1
                left = a
            
            right = max(right, b)

        return count

###############################################################################
"""
Solution 3: brute force. Check every pair of intervals. Use a set to track
intervals that are covered by another interval.

O(n^2) time
O(n) extra space: for set
"""
class Solution3:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        covered = set()

        for i in range(n):
            if i in covered:
                continue

            a, b = intervals[i]

            for j in range(i+1, n):
                if j in covered:
                    continue

                x, y = intervals[j]

                if a <= x and y <= b:
                    covered.add(j)
                if x <= a and b <= y:
                    covered.add(i)

        return n - len(covered)

###############################################################################

if __name__ == "__main__":
    def print_interval(interval):
        a, b = interval # assume small non-negative integers
        if b < a:
            return

        for i in range(b+1):
            if i < a:
                print(f"   ", end="")
            elif i == a:
                print(f"{a}--", end="")
            elif i < b:
                print(f"---", end="")
            else: # i == b
                #print(f"{b}", end="")
                print(f"{b}")

    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\narr = {arr}\n")

        print("Sorted:\n")
        #arr2 = sorted(arr) # for sol 2
        arr2 = sorted(arr, key=lambda a: (a[0], -a[1])) # for sol 1
        for x in arr2:
            print_interval(x)

        res = sol.removeCoveredIntervals(arr)

        print(f"\nres = {res}\n")

    
    sol = Solution() # sort by inc left endpt, then by dec right endpt
    #sol = Solution2() # sort by inc left endpt, then by inc right endpt
    #sol = Solution3() # brute force; use set to track covered intervals

    comment = "LC ex; answer = 2"
    arr = [[1,4],[3,6],[2,8]]
    test(arr, comment)

    """
    1--------4
    1------------------8
          3-------6
       2---------------8
    """
    comment = "; answer = 1"
    arr = [[1,4],[1,8],[3,6],[2,8]]
    test(arr, comment)

    comment = "; answer = 1"
    arr = [[1,2],[1,3]]
    test(arr, comment)

    comment = "; answer = 1"
    arr = [[1,3],[1,8],[5,8]]
    test(arr, comment)

    comment = "; answer = 1"
    arr = [[1,4],[1,8],[3,6],[2,8]]
    test(arr, comment)
