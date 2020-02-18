"""
1351. Count Negative Numbers in a Sorted Matrix
Easy

Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

Return the number of negative numbers in grid.

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0

Example 3:

Input: grid = [[1,-1],[-1,-1]]
Output: 3

Example 4:

Input: grid = [[-1]]
Output: 1
 
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100
"""

from typing import List
import bisect

###############################################################################
"""
Solution 1: Iterate smartly w/o bisection.

Smartly means we start with the last row, count the number of positive
numbers skipped, and add the calculated number of negative numbers in that row.
The "c" index that we stopped with can be used as the starting column index
for the next row iteration.

O(max(n,m)) time

Runtime: 120 ms, faster than 94.14% of Python3 online submissions
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
	def countNegatives(self, grid: List[List[int]]) -> int:
		n_cols = len(grid[0])

		r = len(grid) - 1
		c = 0
		count = 0

		while r >= 0:
			while c < n_cols and grid[r][c] >= 0:
				c += 1

			count += n_cols - c
			r -= 1

		return count

###############################################################################
"""
Solution 2: brute force

O(nm) time

Runtime: 132 ms, faster than 42.75% of Python3 online submissions
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
	def countNegatives(self, grid: List[List[int]]) -> int:
		return sum(x < 0 for row in grid for x in row)


###############################################################################
"""
Solution 3: use binary search on each row

O(m log n) time for m by n matrix.

Runtime: 112 ms, faster than 99.69% of Python3 online submissions
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions
"""
class Solution3:
	def countNegatives(self, grid: List[List[int]]) -> int:	
		n_cols = len(grid[0])

		r = len(grid) - 1
		c = n_cols # if using "c = bisect.bisect_left(grid[r][:-c-1:-1], 0)"
		count = 0

		while r >= 0:
			# Find first column index that has a negative grid value.
			#c = bisect.bisect_left(grid[r][::-1], 0)
			c = bisect.bisect_left(grid[r][:-c-1:-1], 0)
			#print(f"row = {grid[r][:-c-1:-1]}")
			#print(c)
			
			count += c
			r -= 1

		return count

"""
row: 3 2 1 0 -1 -2
n_cols = 6
index of first negative = 4
number of negatives = 2 = 6 - 4 = n_cols - c

grid[r][::-1] = -2 -1 0 1 2 3
index of 0 = 2
number of negatives = 2 = index of 0

Suppose we start with initial index c = ...

"""

###############################################################################

if __name__ == "__main__":
	def test(grid, comment=None):
		print("="*80)
		if comment:
			print(comment)

		print()
		
		for row in grid:
			print(row)

		res = sol.countNegatives(grid)
		print(f"\nres = {res}")

	sol = Solution() # iterate smartly
	sol = Solution2() # brute force
	sol = Solution3() # use bisect()

	comment = "LC ex1; answer = 8"
	grid = [
		[4,3,2,-1],
		[3,2,1,-1],
		[1,1,-1,-2],
		[-1,-1,-2,-3]]
	test(grid, comment)

	comment = "LC ex2; answer = 0"
	grid = [[3,2],[1,0]]
	test(grid, comment)

	comment = "LC ex3; answer = 3"
	grid = [[1,-1],[-1,-1]]
	test(grid, comment)

	comment = "LC ex4; answer = 1"
	grid = [[-1]]
	test(grid, comment)
	