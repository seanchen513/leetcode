"""
973. K Closest Points to Origin
Medium

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]

Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
 
Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
"""

from typing import List
import heapq
import random

###############################################################################
"""
Solution 1: sort by distance (squared) then return first k elements.

O(n log n) time due to sorting.
O(k) extra space for copied list that is returned.

Runtime: 616 ms, faster than 100.00% of Python3 online submissions
Memory Usage: 18.1 MB, less than 7.24% of Python3 online submissions
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # def dist(p):
        #     x = p[0]
        #     y = p[1]
        #     return x*x + y*y

        #points.sort(key=lambda x: x[0]**2 + x[1]**2) # SLOWER
        points.sort(key=lambda x: x[0]*x[0] + x[1]*x[1])
        #points.sort(key=dist)

        return points[:k]

###############################################################################
"""
Solution 2: use min heap with tuple of distance (squared) and point.

O(k log n): for k pops from heap, each pop being O(log n).  Building the heap
costs O(n).

O(n) extra space for heap.
"""
class Solution2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = [] # heap
        
        for x, y in points:
            heapq.heappush(h, (x*x + y*y, [x, y]) )
            
        res = []
        for _ in range(k):
            res.append(heapq.heappop(h)[1])            

        return res

###############################################################################
"""
Solutio 3: use max heap to maintain heap size of k.

O(n log k) time: for building heap of max size k
O(k) extra space for heap and result
"""
class Solution3:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = [] # heap
        
        for x, y in points:
            if len(h) == k:
                heapq.heappushpop(h, (-x*x - y*y, [x, y]) )
            else:
                heapq.heappush(h, (-x*x - y*y, [x, y]) )
            
        # res = []
        # for _ in range(k):
        #     res.append(heapq.heappop(h)[1])            
        # return res

        # Since heap h has exactly k elements, we can safely take them all.
        return [p for _, p in h]

###############################################################################
"""
Solution 4: use heapq.nsmallest()

O(n log k) time ? -- don't know how heapq.nsmallest() is implemented.
"""
class Solution4:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return heapq.nsmallest(k, points, key=lambda x: x[0]*x[0] + x[1]*x[1])
    
###############################################################################
"""
Solution 5: divide & conquer using quick select.

"We want an algorithm faster than n log n. Clearly, the only way to do this is
to use the fact that the k elements returned can be in any order--otherwise we
would be sorting which is at least n log n."

O(n) time avg, O(n^2) worst case due to quick select.
O(n) time worst case possible if use median-of-medians to pick initial
pivot for quick select.

O(n) extra space for augmented points list.
O(k) extra space for return list.

Other implementations:
https://leetcode.com/problems/k-closest-points-to-origin/solution/
https://leetcode.com/problems/k-closest-points-to-origin/discuss/268190/python-quick-select-O(n)

Runtime: 656 ms, faster than 95.87% of Python3 online submissions
Memory Usage: 18.7 MB, less than 5.80% of Python3 online submissions
"""
class Solution5:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def partition(a, left, right): # "right" is inclusive
            pv = a[right] # pivot value

            i = left

            for j in range(left, right):
                if a[j] < pv:
                    a[i], a[j] = a[j], a[i]
                    i += 1
            
            a[i], a[right] = a[right], a[i]

            return i # pivot value is now at index i

        # Don't care about return value of (k+1)st smallest elt.  Just want
        # side effect of first k+1 elements being smallest k+1 elts in "a".
        def select(a, left, right, k): # k is 0-based
            # invalid args, or left == right
            if k < 0 or k >= len(a) or left >= right:
                return

            while left < right:
                # Pick random initial pivot to feed into partition().
                # Swap it to position at "right" index.
                p = random.randint(left, right) # inclusive
                a[p], a[right] = a[right], a[p]

                p = partition(a, left, right) # pivot index
                if p > k:
                    right = p - 1
                elif p < k:
                    left = p + 1
                else:
                    return

        # Build augmented points list with squared distances.
        a = [(x*x + y*y, x, y) for x, y in points]
        
        # Throw away return value since we just care that first k elements
        # of "a" become sorted and smallest in "a".
        select(a, 0, len(a)-1, k-1)
        
        return [[x, y] for _, x, y in a[:k]]

"""
Solution 5b: same as sol 5, but instead of doing quick select on
augmented points list with squared distances, the partition() function
uses a distance function to compare distance values.

This is actually slower, especially using a lambda, and even more so
if using exponentiation.

Using dist() function:
Runtime: 708 ms, faster than 65.88% of Python3 online submissions
Memory Usage: 18.1 MB, less than 7.24% of Python3 online submissions
"""
class Solution5b:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def partition(a, left, right): # "right" is inclusive
            #pv = a[right] # pivot value
            pv = dist(right) # pivot value

            i = left

            for j in range(left, right):
                #if a[j] < pv:
                if dist(j) < pv:
                    a[i], a[j] = a[j], a[i]
                    i += 1
            
            a[i], a[right] = a[right], a[i]

            return i # pivot value is now at index i

        # Don't care about return value of (k+1)st smallest elt.  Just want
        # side effect of first k+1 elements being smallest k+1 elts in "a".
        def select(a, left, right, k): # k is 0-based
            # invalid args, or left == right
            if k < 0 or k >= len(a) or left >= right:
                return

            while left < right:
                # Pick random initial pivot to feed into partition().
                # Swap it to position at "right" index.
                p = random.randint(left, right) # inclusive
                a[p], a[right] = a[right], a[p]

                p = partition(a, left, right) # pivot index
                if p > k:
                    right = p - 1
                elif p < k:
                    left = p + 1
                else:
                    return

        #dist = lambda i: points[i][0]**2 + points[i][1]**2 # SLOW
        dist = lambda i: points[i][0]*points[i][0] + points[i][1]*points[i][1]
        
        #def dist(i):
        #    x = points[i][0]
        #    y = points[i][1]
        #    return x*x + y*y

        # Throw away return value since we just care that first k elements
        # of "a" become sorted and smallest in "a".
        select(points, 0, len(points)-1, k-1)
        
        return points[:k]

"""
Solution 5c: same as sol 5, but more Pythonic.
"""
class Solution5b:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pass

###############################################################################

if __name__ == "__main__":
    def test(points, k, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(f"\npoints = {points}")
        print(f"\nk = {k}")
        
        res = sol.kClosest(points, k)
        print(f"\nres = {res}")


    sol = Solution() # use sorting
    #sol = Solution2() # use min heap
    sol = Solution3() # use max heap to maintain size k heap
    sol = Solution4() # use heapq.nsmallest()
    sol = Solution5() # divide & conquer using quick select
    #sol = Solution5b() # same as sol 6, but using lambda or dist()

    comment = "LC ex1; answer = [[-2,2]]"
    points = [[1,3],[-2,2]]
    k = 1
    test(points, k, comment)
    
    comment = "LC ex2; answer = [[3,3],[-2,4]]"
    points = [[3,3],[5,-1],[-2,4]]
    k = 2
    test(points, k, comment)

    comment = "LC test case"
    points = [[0,1],[1,0]]
    k = 2
    test(points, k, comment)
    
    comment = "LC test case; answer = [[-5,4],[4,6]]"
    points = [[-5,4],[-6,-5],[4,6]]
    k = 2
    test(points, k, comment)

    comment = "LC test case; answer = [[-4,-7],[-4,-8],[-2,10]]"
    points = [[-2,10],[-4,-8],[10,7],[-4,-7]]
    k = 3
    test(points, k, comment)

    comment = "LC test case; answer = [[17,7],[-2,-42],[53,20],[-36,-57],[-69,-8]]"
    points = [[-95,76],[17,7],[-55,-58],[53,20],[-69,-8],[-57,87],[-2,-42],[-10,-87],[-36,-57],[97,-39],[97,49]]
    k = 5
    test(points, k, comment)
