"""
1002. Find Common Characters
Easy

Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]

Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
"""

from typing import List
import collections

###############################################################################
"""
Solution: use 2 dicts and check keys.

Runtime: 48 ms, faster than 66.18% of Python3 online submissions
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
	def commonChars(self, A: List[str]) -> List[str]:
		d = collections.defaultdict(int)
		
		for ch in A[0]:
			d[ch] += 1

		n = len(A)
		d2 = collections.defaultdict(int)

		for i in range(1, n):
			d2.clear()

			for ch in A[i]:
				# Checking this isn't necessary, but makes "if ch in d2"
				# later faster.
				if ch in d:
					d2[ch] += 1

			for ch in d:
				# if ch in d2:
				# 	d[ch] = min( d[ch], d2[ch] )
				# else:
				# 	d[ch] = 0
				
				d[ch] = min( d[ch], d2[ch] ) if ch in d else 0
		
		res = []
		for ch in d:
			res.extend( [ch] * d[ch] )

		return res

"""
Solution 1b: same as sol #1, but delete entries from initial dict if
the chars don't appear in current dict.  This avoids having to check
these chars in future strings.

Runtime: 44 ms, faster than 80.72% of Python3 online submissions
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions
"""
class Solution1b:
	def commonChars(self, A: List[str]) -> List[str]:
		d = collections.defaultdict(int)
		for ch in A[0]:
			d[ch] += 1

		n = len(A)
		d2 = collections.defaultdict(int)

		for i in range(1, n):
			d2.clear()

			for ch in A[i]:
				# Checking this isn't necessary, but makes "if ch in d2"
				# later faster.
				if ch in d: 
					d2[ch] += 1
			
			# Otherwise get "RuntimeError: dictionary changed size during
			# iteration" if try to delete within the loop.
			ch_to_delete = [] 
			
			for ch in d:
				if ch in d2:
					d[ch] = min( d[ch], d2[ch] )
				else:
					ch_to_delete.append(ch)

			# Delete chars from "d" so they won't be checked in the future.
			for ch in ch_to_delete:
				del d[ch]

		res = []
		for ch in d:
			res.extend( [ch] * d[ch] )

		return res

"""
Solution 1c: same idea as sol #1, but use 3 dicts.  One of the dicts is
used to initialize the other dicts (one of them repeatedly).

Since there are only 26 possible chars (lowercase), and up to 100 strings, and
each string can be up to 100 chars, we initialize the dicts to avoid having to
check if keys exist in the dicts.

This doesn't seem to be faster than sol #1.

Runtime: 52 ms, faster than 46.84% of Python3 online submissions
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions
"""
class Solution1c:
	def commonChars(self, A: List[str]) -> List[str]:
		d0 = {}
		i0 = ord('a')
		for i in range(i0, i0+26):
			d0[chr(i)] = 0

		d = d0.copy()
		d2 = d0.copy()

		for ch in A[0]:
			d[ch] += 1

		n = len(A)

		for i in range(1, n):
			d2 = d0.copy()

			for ch in A[i]:
				d2[ch] += 1

			for ch in d:
				d[ch] = min( d[ch], d2[ch] )
				
		res = []
		for ch in d:
			res.extend( [ch] * d[ch] )

		return res

"""
Solution 1d: same as sol #1b, but use two dicts.  The second dict is
re-initialized by resetting its values to 0.

This doesn't seem to be faster than sol #1.
"""
class Solution1d:
	def commonChars(self, A: List[str]) -> List[str]:
		d = {}
		i0 = ord('a')
		for i in range(i0, i0+26):
			d[chr(i)] = 0

		d2 = d.copy()

		for ch in A[0]:
			d[ch] += 1

		n = len(A)

		for i in range(1, n):
			for ch in A[i]:
				d2[ch] += 1

			for ch in d:
				d[ch] = min( d[ch], d2[ch] )
				d2[ch] = 0
				
		res = []
		for ch in d:
			res.extend( [ch] * d[ch] )

		return res

###############################################################################
"""
Solution 2: use collections.Counter()

https://leetcode.com/problems/find-common-characters/discuss/247560/Python-1-Line

https://docs.python.org/3/library/collections.html#collections.Counter

& # intersection:  min(c[x], d[x]) 

The elements() method requires integer counts.
It ignores zero and negative counts.

Runtime: 44 ms, faster than 80.72% of Python3 online submissions
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
	def commonChars(self, A: List[str]) -> List[str]:
		c = collections.Counter(A[0])

		n = len(A)
		for i in range(1, n):
			c &= collections.Counter(A[i])

		return list(c.elements())

###############################################################################

if __name__ == "__main__":
	def test(A, comment=None):
		print("="*80)
		if comment:
			print(comment)

		print()
		print(f"\nA = {A}")

		res = sol.commonChars(A)

		print(f"\nres = {res}\n")


	sol = Solution() # use 2 dicts and check keys
	sol = Solution1b() # same, but del chars in initial dict
	#sol = Solution1c() # use 3 dicts, don't check keys; reinit by copying init dict
	#sol = Solution1d() # use 2 dicts, don't check keys; reinit by setting values to 0
	
	#sol = Solution2() # use collections.Counter()

	comment = 'LC ex1; answer = ["e","l","l"]'
	arr = ["bella","label","roller"]
	test(arr, comment)

	comment = 'LC ex2; answer = ["c","o"]'
	arr = ["cool","lock","cook"]
	test(arr, comment)
