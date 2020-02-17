"""
780. Reaching Points
Hard

A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).

Given a starting point (sx, sy) and a target point (tx, ty), return True if and only if a sequence of moves exists to transform the point (sx, sy) to (tx, ty). Otherwise, return False.

Examples:
Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: True

Explanation:
One series of moves that transforms the starting point to the target is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)

Input: sx = 1, sy = 1, tx = 2, ty = 2
Output: False

Input: sx = 1, sy = 1, tx = 1, ty = 1
Output: True

Note:

sx, sy, tx, ty will all be integers in the range [1, 10^9].
"""

###############################################################################
"""
Solution 1: work backwards naively.

TLE on test cases like:
	sx, sy = 1, 1
	tx, ty = 1000000000, 1

Note: simply changing from subtraction to modulo with no other changes
doesn't work.

O(max(tx, ty)) time: eg, if ty is 1, we could be subtracting tx times
O(1) extra space
"""
class Solution:
	def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
		while tx >= sx and ty >= sy:
			if tx == sx and ty == sy:
				return True

			if tx > ty:
				tx -= ty
			else:
				ty -= tx
			
		return False

###############################################################################
"""
Solution 2: work backwards smartly using modulo.

Note that to have a possible solution, we must have tx >= sx and ty >= sy.
If either of these are equalities, it is easy to check if there is a
solution.  If tx > sx and ty > sy, we keep taking modulos.  

Subtracting also works, but is slower.  However, this solution won't TLE
with subtraction, unlike sol #1.

O(log(max(tx, ty)))  - similar to Euclidean algo
O(1) extra space

Runtime: 20 ms, faster than 96.67% of Python3 online submissions
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
	def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
		while tx > sx and ty > sy:
			if tx > ty:
				#tx -= ty
				tx %= ty
			else:
				#ty -= tx
				ty %= tx

		if tx == sx:
			if ty == sy:
				return True
			elif ty > sy:
				return (ty - sy) % sx == 0

		if ty == sy and tx > sx:
			return (tx - sx) % sy == 0

		return False

###############################################################################

if __name__ == "__main__":
	def test(sx, sy, tx, ty, comment=None):
		print("="*80)
		if comment:
			print(comment)

		print()
		print(f"sx, sy = {sx}, {sy}")
		print(f"tx, ty = {tx}, {ty}")

		res = sol.reachingPoints(sx, sy, tx, ty)
		print(f"\nres = {res}")


	sol = Solution()
	sol = Solution2()
	
	comment = "LC ex1; answer = True"
	sx, sy = 1, 1
	tx, ty = 3, 5
	test(sx, sy, tx, ty, comment)

	comment = "LC ex2; answer = False"
	sx, sy = 1, 1
	tx, ty = 2, 2
	test(sx, sy, tx, ty, comment)

	comment = "LC ex1; answer = True"
	sx, sy = 1, 1
	tx, ty = 1, 1
	test(sx, sy, tx, ty, comment)

	comment = "LC test case; TLE danger; answer = True"
	sx, sy = 1, 1
	tx, ty = 1000000000, 1
	test(sx, sy, tx, ty, comment)

	comment = "LC test case; answer = True"
	sx, sy = 3, 3
	tx, ty = 12, 9
	test(sx, sy, tx, ty, comment)

	comment = "LC test case; answer = False"
	sx, sy = 9, 5
	tx, ty = 12, 8
	test(sx, sy, tx, ty, comment)

	comment = "LC test case; answer = True"
	sx, sy = 9, 10
	tx, ty = 9, 19
	test(sx, sy, tx, ty, comment)

	comment = "answer = True"
	sx, sy = 5, 10
	tx, ty = 25, 20
	test(sx, sy, tx, ty, comment)

	comment = "answer = True"
	sx, sy = 15, 10
	tx, ty = 25, 10
	test(sx, sy, tx, ty, comment)