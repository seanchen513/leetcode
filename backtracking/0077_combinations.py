"""
77. Combinations
Medium

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

from typing import List
import itertools

###############################################################################
"""
Solution 1: naive recursion, passing copied objects.

Runtime: 552 ms, faster than 49.56% of Python3 online submissions
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
	def combine(self, n: int, k: int) -> List[List[int]]:
		def rec(start=1, combo=[]):
			if len(combo) == k:
				res.append(combo)
				return

			for i in range(start, n+1):
				rec(i + 1, combo + [i])

		res = []
		rec()

		return res

"""
Solution 1b: naive recursion, passing mutable object directly.

Runtime: 532 ms, faster than 63.32% of Python3 online submissions
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions 
"""
class Solution1b:
	def combine(self, n: int, k: int) -> List[List[int]]:
		def rec(start=1, combo=[]):
			if len(combo) == k:
				res.append(combo[:])
				return

			for i in range(start, n+1):
				combo.append(i)
				rec(i + 1, combo)
				combo.pop()

		res = []
		rec()

		return res

###############################################################################
"""
Solution 2: recursion w/ smart range, passing copied objects

Runtime: 92 ms, faster than 89.30% of Python3 online submissions
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
	def combine(self, n: int, k: int) -> List[List[int]]:
		def rec(start=1, combo=[]):
			if len(combo) == k:
				res.append(combo)
				return

			end = n - k + len(combo) + 2
			#end = m + len(combo)
			for i in range(start, end):
				rec(i + 1, combo + [i])

		#m = n - k + 2
		res = []
		rec()

		return res
		
"""
Solution 2b: recursion w/ smart range, passing mutable objects directly.

Runtime: 84 ms, faster than 95.05% of Python3 online submissions
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions
"""
class Solution2b:
	def combine(self, n: int, k: int) -> List[List[int]]:
		def rec(start=1, combo=[]):
			if len(combo) == k:
				res.append(combo[:])
				return

			end = n - k + len(combo) + 2
			#end = m + len(combo)
			for i in range(start, end):
				combo.append(i)
				rec(i + 1, combo)
				combo.pop()

		#m = n - k + 2
		res = []
		rec()

		return res

"""
Solution 2c: recursion, passing copied objects, w/ smart range by passing 
"end" as well.

Runtime: 80 ms, faster than 97.20% of Python3 online submissions
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions
"""
class Solution2c:
	def combine(self, n: int, k: int) -> List[List[int]]:
		def rec(start=1, end=n-k+2, combo=[]):
			if len(combo) == k:
				res.append(combo)
				return

			for i in range(start, end):
				rec(i + 1, end + 1, combo + [i])

		res = []
		rec()

		return res

"""
Solution 2d: recursion, passing mutable objects directly, 
w/ smart range by passing "end" as well.

Runtime: 76 ms, faster than 98.80% of Python3 online submissions
Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions
"""
class Solution2d:
	def combine(self, n: int, k: int) -> List[List[int]]:
		def rec(start=1, end=n-k+2, combo=[]):
			if len(combo) == k:
				res.append(combo[:])
				return

			for i in range(start, end):
				combo.append(i)
				rec(i + 1, end + 1, combo)
				combo.pop()

		res = []
		rec()

		return res

###############################################################################
"""
Solution 3: iteration, generating combos in order.

Runtime: 832 ms, faster than 9.24% of Python3 online submissions
Memory Usage: 69.1 MB, less than 6.67% of Python3 online submissions
"""
class Solution3:
	def combine(self, n: int, k: int) -> List[List[int]]:
		res = [[]]

		for _ in range(k):
			next_res = []

			for combo in res:
				#start = max(combo) + 1 if combo else 1 # slower
				start = combo[-1] + 1 if combo else 1

				for j in range(start, n+1):
					next_res.append(combo + [j])
	
			res = next_res

		return res

"""
Solution 3b: iteration, generating combos in order, w/ smart range.

It should be possible to improve this by removing use of "next_res"...

Example: 12, 13, 14, 23, 24, 34

Runtime: 76 ms, faster than 98.80% of Python3 online submissions
Memory Usage: 14.8 MB, less than 100.00% of Python3 online submissions
"""
class Solution3b:
	def combine(self, n: int, k: int) -> List[List[int]]:
		res = [[]]

		#for len in range(k): # len = length of current combos in res
		for end in range(n - k + 2, n + 2): # iterates k times
			next_res = []
			#end = n - k + len + 2 # n-k+2 to n-k+(k-1)+2 = n+1

			for combo in res:
				start = combo[-1] + 1 if combo else 1
				#end = n - k + len(combo) + 2

				for j in range(start, end):
					next_res.append(combo + [j])
	
			res = next_res

		return res

"""
Solution 3c: iteration...

NOT DONE
"""
class Solution3c:
	def combine(self, n: int, k: int) -> List[List[int]]:
		pass

"""
Solution 3d: iteration, lexicographic (binary sorted)

Example: 12, 13, 23, 14, 24, 34
0011, 0101, 0110, 1001, 1010, 1100

https://leetcode.com/problems/combinations/solution/

Runtime: 76 ms, faster than 98.80% of Python3 online submissions
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions
"""
class Solution3d:
	def combine(self, n: int, k: int) -> List[List[int]]:
		# init first combination w/ sentinel n+1
		combo = list(range(1, k + 1)) + [n+1]

		res = []
		j = 0

		while j < k:
			# add current combination
			res.append(combo[:k])

			# increase first combo[j] by one
			# if combo[j] + 1 != combo[j + 1]
			j = 0
			while j < k and combo[j + 1] == combo[j] + 1:
				combo[j] = j + 1
				j += 1
				#print(combo)
				
			combo[j] += 1
 
		return res

###############################################################################
"""
Solution 4: use itertools.combinations()

Runtime: 80 ms, faster than 97.20% of Python3 online submissions
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions
"""
class Solution4:
	def combine(self, n: int, k: int) -> List[List[int]]:
		return list(map(list, itertools.combinations(range(1, n+1), k)))

###############################################################################

if __name__ == "__main__":
	def test(n, k, comment=None):
		print("="*80)
		if comment:
			print(comment, "\n")

		print(f"n, k = {n}, {k}")

		res = sol.combine(n, k)
		print(f"\nSolution: {res}\n")


	sol = Solution() # recursion, passing copied objects
	sol = Solution1b() # recursion, passing mutable objects directly
	
	#sol = Solution2() # recursion w/ smart range, passing copied objects
	#sol = Solution2b() # recursion w/ smart range, passing mutable objects directly
	sol = Solution2c() # recursion w/ smart range, passing "end"
	
	#sol = Solution3() # iteration
	#sol = Solution3b() # iteration w/ smart range
	#sol = Solution3c() # iteration... NOT DONE
	#sol = Solution3d() # iteration, lexicographic (binary sorted)
	
	#sol = Solution4() # use itertools.combinations()
	

	comment = "Trivial case"
	n, k = 1, 1
	test(n, k, comment)

	comment = ""
	n, k = 5, 1 
	test(n, k, comment)

	comment = ""
	n, k = 5, 5
	test(n, k, comment)

	comment = "LC example"
	n, k = 4, 2
	test(n, k, comment)
	
