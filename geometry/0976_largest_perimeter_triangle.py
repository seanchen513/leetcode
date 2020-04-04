"""
976. Largest Perimeter Triangle
Easy

Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.

If it is impossible to form any triangle of non-zero area, return 0.

Example 1:

Input: [2,1,2]
Output: 5

Example 2:

Input: [1,2,1]
Output: 0

Example 3:

Input: [3,2,3,4]
Output: 10

Example 4:

Input: [3,6,2,3]
Output: 8

Note:

3 <= A.length <= 10000
1 <= A[i] <= 10^6
"""

from typing import List
import bisect

###############################################################################
"""
Solution 1: sort in reverse.  Suppose c >= b >= a are adjacent values.
They form a valid triangle if c < a + b.

If this is the case (c < a + b), there is no reason to check lower values of 
a or b for fixed c, since even if they formed a valid triangle, they would 
have a smaller perimeter.

If this isn't the case, then c >= a + b.  This would still be the case
even if we chose smaller values of a and b for fixed c.  So we are forced
to choose a smaller value of c.

Suppose we have already found adjacent a, b, c that form a valid triangle.
What about smaller values of c with possibly larger a + b?  This isn't
possible since a, b, c are adjacent.

So the largest perimeter comes from the first adjacent triple that forms
a valid triangle.

O(n log n) time: for sorting; loop is O(n).
O(1) extra space: if sort is in-place.

Runtime: 196 ms, faster than 96.81% of Python3 online submissions
Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
	def largestPerimeter(self, A: List[int]) -> int:
		A.sort(reverse=True)
		n = len(A)
		
		for i in range(n-2):
			if A[i] < A[i+1] + A[i+2]:
				return A[i] + A[i+1] + A[i+2]

		return 0

###############################################################################
"""
Solution 2: brute force with triangle inequality.

Triangle inequality for side lengths a, b, c where c is greatest:
a + b > c

O(n^3) time

TLE
"""
class Solution2:
	def largestPerimeter(self, A: List[int]) -> int:
		A.sort()
		n = len(A)
		max_peri = 0

		for i in range(n):
			a = A[i]
			
			for j in range(i+1, n):
				c_limit = a + A[j]

				for k in range(j+1, n):
					c = A[k]
					if c >= c_limit:
						break

					max_peri = max(max_peri, c_limit + c)

		return max_peri

###############################################################################
"""
Solution 3: brute force with triangle inequality and bisection.

TLE
"""
class Solution3:
	def largestPerimeter(self, A: List[int]) -> int:
		A.sort()
		n = len(A)
		max_peri = 0

		for i in range(n-2):
			a = A[i]
			
			for j in range(i+1, n-1):
				c_limit = a + A[j]

				# Find index for rightmost value less than c_limit.
				k = bisect.bisect_left(A, c_limit, j+1) - 1
				#print(f"k = {k}")
				
				if j < k < n:
					max_peri = max(max_peri, c_limit + A[k])

		return max_peri

###############################################################################

if __name__ == "__main__":
	def test(arr, comment=None):
		print("="*80)
		if comment:
			print(comment)

		print()
		print(f"\npossible side lengths = {arr}")

		res = sol.largestPerimeter(arr)

		print(f"\nlongest perimeter = {res}")


	sol = Solution() # sort in reverse; check adjacent triplets
	#sol = Solution2() # brute force w/ triangle ineq.
	#sol = Solution3() # brute force w/ triangle ineq. and bisection
	
	comment = "LC ex1; answer = 5"
	arr = [2,1,2]
	test(arr, comment)

	comment = "LC ex2; answer = 0"
	arr = [1,2,1]
	test(arr, comment)

	comment = "LC ex3; answer = 10"
	arr = [3,2,3,4]
	test(arr, comment)

	comment = "LC ex4; answer = 8"
	arr = [3,6,2,3]
	test(arr, comment)
