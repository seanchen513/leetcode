"""
812. Largest Triangle Area
Easy

You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation: 
The five points are show in the figure below. The red triangle is the largest.

Notes:

3 <= points.length <= 50.
No points will be duplicated.
 -50 <= points[i][j] <= 50.
Answers within 10^-6 of the true value will be accepted as correct.
"""

from typing import List
import itertools

###############################################################################
"""
Solution: use the Shoelace formula

signed area = 1/2 * det(M)
area = 1/2 * abs(det(M))

where M is the matrix:

1   1  1
x1 x2 x3
y1 y2 y3

* FASTER than using Heron's formula.

Runtime: 116 ms, faster than 89.84% of Python3 online submissions
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
	def largestTriangleArea(self, p: List[List[int]]) -> float:
		n = len(p)
		res = 0
		
		for i in range(n-2):
			x1, y1 = p[i][0], p[i][1]
			
			for j in range(i+1, n-1):
				x2, y2 = p[j][0], p[j][1]
				
				c = x1*y2 - x2*y1
					
				for k in range(j+1, n):
					x3, y3 = p[k][0], p[k][1]
					
					b = x1*y3 - x3*y1
					a = x2*y3 - x3*y2

					res = max(res, abs(a - b + c))

		return res * 0.5

"""
Solution 1b: same as sol #1, but using itertools.combinations().

Runtime: 108 ms, faster than 91.02% of Python3 online submissions
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions
"""
class Solution1b:
	def largestTriangleArea(self, points: List[List[int]]) -> float:
		res = 0
		
		for (x1, y1), (x2, y2), (x3, y3) in itertools.combinations(points, 3):
			# c = x1*y2 - x2*y1			
			# b = x1*y3 - x3*y1
			# a = x2*y3 - x3*y2
			# res = max(res, abs(a - b + c))

			#res = max(res, abs(x2*y3 - x3*y2 - x1*y3 + x3*y1 + x1*y2 - x2*y1))
			#res = max(res, abs(x1*y2 + x2*y3 + x3*y1 - x3*y2 - x1*y3 - x2*y1))
			
			res = max(res, abs( x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2) ))

		return res * 0.5

###############################################################################
"""
Solution 2: use Heron's formula:

area = sqrt(s(s-a)(s-b)(s-c))
where s = (a+b+c)/2

O(n^3) time
O(1) extra space

Runtime: 260 ms, faster than 32.03% of Python3 online submissions
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
	def largestTriangleArea(self, p: List[List[int]]) -> float:
		n = len(p)
		res = 0
		
		for i in range(n-2):
			x0, y0 = p[i][0], p[i][1]
			
			for j in range(i+1, n-1):
				x1, y1 = p[j][0], p[j][1]
				
				dx = x1 - x0
				dy = y1 - y0
				a = (dx*dx + dy*dy)**0.5

				for k in range(j+1, n):
					x2, y2 = p[k][0], p[k][1]

					dx2 = x2 - x0
					dy2 = y2 - y0

					if dx * dy2 == dx2 * dy: # collinear
						continue
					
					b = (dx2*dx2 + dy2*dy2)**0.5
					c = ((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))**0.5
					
					s = (a+b+c)/2
					res = max(res, s*(s-a)*(s-b)*(s-c))
		
		return res**0.5

"""
Solution 2b: same as sol #1, but use itertools.combinations().

Runtime: 232 ms, faster than 33.98% of Python3 online submissions
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions
"""
class Solution2b:
	def largestTriangleArea(self, points: List[List[int]]) -> float:
		res = 0
		
		for (x0, y0), (x1, y1), (x2, y2) in itertools.combinations(points, 3):				
			dx = x1 - x0
			dy = y1 - y0

			dx2 = x2 - x0
			dy2 = y2 - y0

			if dx * dy2 == dx2 * dy: # collinear
				continue
			
			a = (dx*dx + dy*dy)**0.5
			b = (dx2*dx2 + dy2*dy2)**0.5
			c = ((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))**0.5
			
			s = (a+b+c)/2
			res = max(res, s*(s-a)*(s-b)*(s-c))
		
		return res**0.5

###############################################################################
"""
Solution 3: find convex hull first.  Then use Shoelace formula on points on it.

On LC, this is about 10 times faster than not using the convex hull.

https://en.wikibooks.org/wiki/Algorithm_Implementation/Geometry/Convex_hull/Monotone_chain#Python

Runtime: 28 ms, faster than 100.00% of Python3 online submissions
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions
"""
class Solution3:
	def largestTriangleArea(self, points: List[List[int]]) -> float:
		def boundary(points):
			## Use set() to remove duplicates.
			## Convert each point from list to tuple to make them hashable,
			## so that set() can be applied.  Convert set to list so we
			## can use reversed(points) for building upper hull.
			#points = list(set(map(tuple, points)))
			
			# Replaced line above because it's slow on LC, probably because
			# of huge number of points in some test cases.  It might be ok
			# if the input was given as a list of tuples instead.
			# Apply set() in return statement instead.
			points = sorted(points)

			## Don't need this part for LC812 since len(points) >= 3
			#if len(points) <= 1:
			#	return points

			# 2D cross product of OA and OB vectors, ie, z-component of
			# their 3D cross product.  Positive if OAB is CCW, negative if
			# CW, and 0 if collinear.
			def cross(o, a, b): 
				return (o[0]-a[0]) * (o[1]-b[1]) - (o[1]-a[1]) * (o[0]-b[0])
			
			# Build lower hull.
			lower = []
			for p in points:
				while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0: 
					lower.pop()
				lower.append(tuple(p))
			
			# Build upper hull.
			upper = []
			for p in reversed(points):
				while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0: 
					upper.pop()
				upper.append(tuple(p))
			
			## Last point of each list is omitted because it's repeated at
			## the beginning of the other list.
			#return lower[:-1] + upper[:-1]

			# Use set() to remove duplicate points.
			return set(lower[:-1] + upper[:-1]) # or convert to list if needed

		p = boundary(points)
		res = 0
		
		for (x1, y1), (x2, y2), (x3, y3) in itertools.combinations(p, 3):			
			res = max(res, abs( x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2) ))
			
		return res * 0.5

###############################################################################

if __name__ == "__main__":
	def test(arr, comment=None):
		print("="*80)
		if comment:
			print(comment)

		print()
		print(f"\npoints = {arr}")

		res = sol.largestTriangleArea(arr)

		print(f"\nlargest triangle area = {res}")


	sol = Solution() # Shoelace formula
	sol = Solution() # Shoelace formula, itertools.combinations
	#sol = Solution2() # Heron's formula
	#sol = Solution2b() # Heron's formula, itertools.combinations
	sol = Solution3() # use Shoelace formula on convex hull

	comment = "LC example; answer = 2"
	arr = [[0,0],[0,1],[1,0],[0,2],[2,0]]
	test(arr, comment)
