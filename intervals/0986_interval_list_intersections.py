"""
986. Interval List Intersections
Medium

Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

Example 1:

Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.

Note:

0 <= A.length < 1000
0 <= B.length < 1000
0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""

from typing import List

###############################################################################
"""
Solution: use 2 pointers. If there is an intersection, increment the pointer
for A or B only if the endpoint of the intersection equals A[i] or B[j], resp.

O(m+n) time: in each iteration, at least one pointer is incremented.

O(m+n) extra space: for output list
O(1) extra space other than output
"""
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m = len(A)
        n = len(B)
        
        i = 0 # index for A
        j = 0 # index for B

        res = []

        while i < m and j < n:
            a1, a2 = A[i]
            b1, b2 = B[j]

            if a2 < b1: # don't intersect
                i += 1
            elif b2 < a1: # don't intersect
                j += 1
            else: # intersect
                end = min(a2, b2)
                res.append([max(a1, b1), end])

                if end == a2:
                    i += 1
                if end == b2:
                    j += 1

        return res

###############################################################################
"""
Solution 2: 

"""
class Solution2:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m = len(A)
        n = len(B)
        
        i = 0 # index for A
        j = 0 # index for B

        res = []

        while i < m and j < n:
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])

            if lo <= hi: # A[i] and B[j] intersect
                res.append([lo, hi])

            # Remove the interval with the smallest right endpoint.
            # If they're equal, we can discard both intervals (not done here).
            if A[i][1] < B[j][1]: 
                # A[i] cannot intersect any more intervals in B
                # ie, A[i] cannot intersect B[j+1], B[j+2], ...
                i += 1
            else:
                j += 1

        return res

###############################################################################

if __name__ == "__main__":
    def test(A, B, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\nA = {A}")
        print(f"B = {B}")

        res = sol.intervalIntersection(A, B)

        print(f"\nres = {res}\n")


    sol = Solution() # 
    sol = Solution2() # 

    comment = "LC example; answer = [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]"
    A = [[0,2],[5,10],[13,23],[24,25]]
    B = [[1,5],[8,12],[15,24],[25,26]]
    test(A, B, comment)
    