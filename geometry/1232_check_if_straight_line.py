"""
1232. Check If It Is a Straight Line
Easy

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Example 1:

Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:

Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
 
Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
"""

from typing import List

###############################################################################
"""
Solution: check if all slopes between consecutive points are the same.

O(n) time
O(1) extra space

Slopes:
y / x = y0 / x0
y * x0 = y0 * x

"""
class Solution:
    def checkStraightLine(self, coords: List[List[int]]) -> bool:
        n = len(coords)
        
        p0 = coords[0]
        p1 = coords[1]
        
        # dy and dx of slope between points 0 and 1
        dy0 = p1[1] - p0[1]
        dx0 = p1[0] - p0[0]
        
        for i in range(2, n):
            # dy and dx of slope between points i and i-1
            dy = coords[i][1] - coords[i-1][1]
            dx = coords[i][0] - coords[i-1][0]
            
            if dy0 * dx != dy * dx0:
                return False
            
        return True
        
"""
Solution 1b: same, but use zip in loop.
"""
class Solution1b:
    def checkStraightLine(self, coords: List[List[int]]) -> bool:
        p0 = coords[0]
        p1 = coords[1]
        
        dy0 = p1[1] - p0[1]
        dx0 = p1[0] - p0[0]
        
        for p, p0 in zip(coords[2:], coords[1:]):
            dy = p[1] - p0[1]
            dx = p[0] - p0[0]
            
            if dy0 * dx != dy * dx0:
                return False
            
        return True

"""
Solution 1c: same, but first convert coords as list of points [x,y]
to two lists x and y of each coordinate.
"""
class Solution1c:
    def checkStraightLine(self, coords: List[List[int]]) -> bool:
        n = len(coords)
        x, y = zip(*coords)

        dy0 = y[1] - y[0]
        dx0 = x[1] - x[0]

        for i in range(2, n):
            dy = y[i] - y[i-1]
            dx = x[i] - x[i-1]

            if dy0 * dx != dy * dx0:
                return False
            
        return True
        