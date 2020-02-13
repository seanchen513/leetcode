"""
78. Subsets
Medium

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

from typing import List
import itertools

###############################################################################
"""
Solution 1: recursion.

Runtime: 32 ms, faster than 68.34% of Python3 online submissions
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
	def subsets(self, arr: List[int]) -> List[List[int]]:
		def rec(index=0, subset=[]):
			if index == n:
				res.append(subset)
				return

			rec(index + 1, subset)
			rec(index + 1, subset + [arr[index]])

		n = len(arr)
		res = []

		rec()
		return res

###############################################################################
"""
Solution 2: iteration.

Runtime: 28 ms, faster than 88.45% of Python3 online submissions
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
	def subsets(self, arr: List[int]) -> List[List[int]]:
		res = [[]]

		for x in arr:
			res.extend([subset + [x] for subset in res])

		return res

###############################################################################
"""
Solution 3: bits.
"""
class Solution3:
	def subsets(self, arr: List[int]) -> List[List[int]]:
		k = len(arr) # k bits
		n = 2**k # number of subsets
		res = []

		# Each i represents a subset via its pattern of k bits.
		for i in range(n):
			# Loop through bits of a copy of i.
			i2 = i
			subset = []
			for b in range(k): # bit index
				if i2 & 1:
					subset += [arr[b]]
				i2 >>= 1

			res.append(subset)

		return res

"""
Solution 3b: same as sol #3, but more concise.
"""
class Solution3b:
	def subsets(self, arr: List[int]) -> List[List[int]]:
		k = len(arr) # k bits
		n = 2**k # number of subsets
		res = []

		# Each i represents a subset via its pattern of k bits.
		for i in range(n):
			res.append( [arr[b] for b in range(k) if (i >> b) & 1] )

		return res

"""
Solution 3c: same as sol #3b, but using bit string.
"""
class Solution3c:
	def subsets(self, arr: List[int]) -> List[List[int]]:
		k = len(arr) # k bits
		n = 2**k # number of subsets
		res = []

		# Each i represents a subset via its pattern of k bits.
		for i in range(n):		
			bit_str = f"{i:{k}b}"
			res.append( [arr[b] for b in range(k) if bit_str[b] == '1'] )

		return res

###############################################################################
"""
Solution 4: use itertools.combinations()
"""
class Solution4:
	def subsets(self, arr: List[int]) -> List[List[int]]:
		end = len(arr) + 1
		res = []

		for k in range(0, end):
			#res.extend( [list(combo) for combo in itertools.combinations(arr, k)] )
			res.extend( map(list, itertools.combinations(arr, k)) )

		return res

"""
Solution 4b: same as sol #4b. but using itertools.chain.from_iterable() as well.
"""
class Solution4b:
	def subsets(self, arr: List[int]) -> List[List[int]]:
		end = len(arr) + 1
		res = itertools.chain.from_iterable(itertools.combinations(arr, k) for k in range(0, end))

		return list(map(list, res))

###############################################################################

if __name__ == "__main__":
	def test(arr, comment=None):
		print("="*80)
		if comment:
			print(comment, "\n")

		print(f"{arr}")

		res = sol.subsets(arr)
		print(f"\nSolution: {res}\n")


	sol = Solution() # recursion
	#sol = Solution2() # iteration
	#sol = Solution3() # bits
	#sol = Solution3b() # bits, more concise
	#sol = Solution3c() # bits, using bit string
	#sol = Solution4() # use itertools.combinations()
	#sol = Solution4b() # use itertools.combinations() and itertools.chain.from_iterable()

	comment = "Trivial case: no elements"
	arr = []
	test(arr, comment)

	comment = "One element"
	arr = [1]
	test(arr, comment)

	comment = "LC example: 3 elements"
	arr = [1,2,3]
	test(arr, comment)
	