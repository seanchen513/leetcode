"""
1401. Circle and Rectangle Overlapping
Medium

Given a circle represented as (radius, x_center, y_center) and an axis-aligned rectangle represented as (x1, y1, x2, y2), where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the rectangle.

Return True if the circle and rectangle are overlapped otherwise return False.

In other words, check if there are any point (xi, yi) such that belongs to the circle and the rectangle at the same time.

Example 1:

Input: radius = 1, x_center = 0, y_center = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
Output: true
Explanation: Circle and rectangle share the point (1,0) 

Example 2:

Input: radius = 1, x_center = 0, y_center = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
Output: true

Example 3:

Input: radius = 1, x_center = 1, y_center = 1, x1 = -3, y1 = -3, x2 = 3, y2 = 3
Output: true

Example 4:

Input: radius = 1, x_center = 1, y_center = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
Output: false
 
Constraints:

1 <= radius <= 2000
-10^4 <= x_center, y_center, x1, y1, x2, y2 <= 10^4
x1 < x2
y1 < y2
"""

import collections

###############################################################################
"""
Solution: 

Based on solution by Cygon here:
https://stackoverflow.com/questions/401847/circle-rectangle-collision-detection-intersection

Same as here:
https://www.jeffreythompson.org/collision-detection/circle-rect.php

See picture here:
https://leetcode.com/problems/circle-and-rectangle-overlapping/discuss/563341/4-lines-C%2B%2B-O(1)%3A-Test-shortest-distance-from-center-to-rect-(with-pics)
"""
class Solution:
    #def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
    def checkOverlap(self, r: int, cx: int, cy: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        ### Find closest point on rectangle's edge to circle
        x = cx
        y = cy

        # if x1 <= cx <= x2, then dx = 0 below
        if cx < x1:   x = x1
        elif cx > x2: x = x2

        # if y1 <= cx <= y2, then dy = 0 below
        if cy < y1:   y = y1
        elif cy > y2: y = y2

        ### Distance between this closest point and the circle's center.
        # If dx = 0 or dy = 0, then closest point on rect to circle is on the
        # edge and not a corner. The distance b/w the circle's center and the
        # edge is along the radius of the circle perpendiclar to the edge.
        # If dx != 0 and dy !=0, then closest point on rect to circle is a corner.
        dx = cx - x
        dy = cy - y

        # if this distance < circle's radius, then intersection occurs
        return dx*dx + dy*dy <= r*r

###############################################################################
"""
Solution 2: 

Assumes sides for rectangle are parallel to the axes.

Based on solution by e.James here:
https://stackoverflow.com/questions/401847/circle-rectangle-collision-detection-intersection

Can multiple variables by 2 to simplify things.
"""
class Solution2:
    #def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
    def checkOverlap(self, r: int, cx: int, cy: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # rectangle center
        rx = (x1 + x2) * 0.5
        ry = (y1 + y2) * 0.5

        # horizontal and vertical distance between centers of circle and rectangle
        dx = abs(cx - rx)
        dy = abs(cy - ry)

        # rectangle height and width
        h = y2 - y1
        w = x2 - x1

        # Check horizontal and vertical distance b/w centers.
        if dx > w/2 + r:
            return False
        if dy > h/2 + r:
            return False

        # Given the above checks pass, we know bounds for dx and dy.
        # If one of them is bounded even more, then we have an intersection.
        if dx <= w/2:
            return True
        if dy <= h/2:
            return True

        # More difficult case where circle may intersect a corner.
        # Calculate squared distance b/w center of circle and corner.
        # Effectively, we can let the center of the rectangle be at (0,0)
        # the corner be at (h/2, w/2), and the circle's center at (dx,dy).
        d_corner = (dx - w/2)**2 + (dy - h/2)**2

        return d_corner <= r**2

###############################################################################

if __name__ == "__main__":
    def test(r, cx, cy, x1, y1, x2, y2, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\nr = {r}")
        print(f"cx, cy = {cx}, {cy}")
        print(f"x1, y1 = {x1}, {y1}")
        print(f"x2, y2 = {x2}, {y2}")

        res = sol.checkOverlap(r, cx, cy, x1, y1, x2, y2)

        print(f"\nres = {res}\n")


    sol = Solution()
    #sol = Solution2()

    comment = "LC ex1; answer = True"
    r = 1 
    cx, cy = 0, 0
    x1, y1 = 1, -1
    x2, y2 = 3, 1
    test(r, cx, cy, x1, y1, x2, y2, comment)

    comment = "LC ex2; answer = True"
    r = 1 
    cx, cy = 0, 0
    x1, y1 = -1, 0
    x2, y2 = 0, 1
    test(r, cx, cy, x1, y1, x2, y2, comment)

    comment = "LC ex3; answer = True"
    r = 1 
    cx, cy = 1, 1
    x1, y1 = -3, -3
    x2, y2 = 3, 3
    test(r, cx, cy, x1, y1, x2, y2, comment)

    comment = "LC ex4; answer = False"
    r = 1 
    cx, cy = 1, 1
    x1, y1 = 1, -3
    x2, y2 = 2, -1
    test(r, cx, cy, x1, y1, x2, y2, comment)

    comment = "LC TC; answer = True"
    r = 10 
    cx, cy = 10, 1
    x1, y1 = 0, 0
    x2, y2 = 100, 100
    test(r, cx, cy, x1, y1, x2, y2, comment)
