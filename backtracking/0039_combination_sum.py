"""
39. Combination Sum
Medium

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

from typing import List
import itertools

###############################################################################
"""
Solution 1: recursion

Runtime: 48 ms, faster than 92.84% of Python3 online submissions
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		def rec(cand_index=0, tgt=target, combo=[]):
			if tgt == 0:
				res.append(combo)
				return

			for i in range(cand_index, n):
				c = candidates[i]
				if c > tgt:
					continue

				rec(i, tgt - c, combo + [c])

		n = len(candidates)
		res = []

		rec()

		return res
###############################################################################
"""
Solution 1b: recursion, using initial sort and early exit.

https://leetcode.com/problems/combination-sum/discuss/16510/Python-dfs-solution.
https://leetcode.com/problems/combination-sum/discuss/16554/Share-My-Python-Solution-beating-98.17

Runtime: 44 ms, faster than 97.40% of Python3 online submissions
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions
"""
class Solution1b:
	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		def rec(cand_index=0, tgt=target, combo=[]):
			if tgt == 0:
				res.append(combo)
				return

			for i in range(cand_index, n):
				c = cand[i]
				if c > tgt:
					break

				rec(i, tgt - c, combo + [c])

		cand = sorted(candidates)
		n = len(cand)
		res = []

		rec()

		return res


###############################################################################
"""
Solution 2: recursion, first attempt.

Runtime: 108 ms, faster than 28.20% of Python3 online submissions
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		def rec(cand_index=0, tgt=target, combo=[]):
			# This check must come before the next one, which checks cand_index.
			if tgt == 0:
				res.append(combo)
				return

			if cand_index >= n_candidates:
				return

			c = candidates[cand_index]

			for c_times in range(tgt//c + 1):
				rec(cand_index + 1, tgt - c * c_times, combo + [c] * c_times)

		res = []
		n_candidates = len(candidates)

		rec()

		return res

###############################################################################
"""
Solution 3: iteration, first attempt.

Runtime: 108 ms, faster than 28.20% of Python3 online submissions
Memory Usage: 13.8 MB, less than 6.06% of Python3 online submissions
"""
class Solution3:
	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		res = [(target, [])]

		for c in candidates:
			next_res = []

			for tgt, combo in res:

				for c_times in range(tgt // c + 1):
					next_res.append( (tgt - c * c_times, combo + [c] * c_times) )

			res = next_res

		return [combo for (tgt, combo) in res if tgt == 0]


###############################################################################
"""
Solution 4: brute force using itertools.combinations_with_replacement()

Runtime: 132 ms, faster than 19.13% of Python3 online submissions
Memory Usage: 18 MB, less than 6.06% of Python3 online submissions
"""
class Solution4:
	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		n = target // min(candidates) + 1
		combos = []

		for k in range(1, n):
			combos.extend( itertools.combinations_with_replacement(candidates, k) )

		return [list(combo) for combo in combos if sum(combo) == target]

###############################################################################

if __name__ == "__main__":
	def test(cand, target, comment=None):
		print("="*80)
		if comment:
			print(comment, "\n")

		print(f"candidates = {cand}")
		print(f"target = {target}")

		res = sol.combinationSum(cand, target)
		print(f"\nSolution: {res}\n")


	sol = Solution() # recursion
	sol = Solution1b() # recursion, using initial sort and early exit
	#sol = Solution2() # recursion, 1st attempt
	#sol = Solution3() # iterative, 1st attempt
	#sol = Solution4() # use itertools.combinations_with_replacement

	comment = "LC ex1"
	cand = [2,3,6,7]
	target = 7
	test(cand, target, comment)
	
	comment = "LC ex2"
	cand = [2,3,5]
	target = 8
	test(cand, target, comment)

	comment = "LC test case; recursion TLE's"
	cand = [48,22,49,24,26,47,33,40,37,39,31,46,36,43,45,34,28,20,29,25,41,32,23]
	target = 69
	test(cand, target, comment)

	comment = "LC test case; answer = [[2,2,3], [7]]"
	cand = [2,3,6,7]
	target = 7
	test(cand, target, comment)
