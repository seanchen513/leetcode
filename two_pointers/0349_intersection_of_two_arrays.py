"""
349. Intersection of Two Arrays
Easy

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
"""

from typing import List

###############################################################################
"""
Solution 1: use 2 sets.

O(n + m) time
O(n + m) extra space: for sets
"""
class Solution:
	def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
		return list(set(nums1) & set(nums2))


"""
Solution 1b: same idea as sol #1, but use one set.

Build set from smaller list.  This way, lookups will be faster.
Also, we will break out of the loop more quickly as the set will become 
empty more quickly.
"""
class Solution1b:
	def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
		# This is to optimize the loop by having the "if not s" check done
		# only after removing an element from the set "s".  Otherwise,
		# we would loop through all the elements in num2, checking against
		# an empty set.  Alternatively, we don't have to have this initial
		# check on nums1 and nums2 (or an initial check on "s"), but would 
		# have to do the check for an empty set on every iteration.
		if not nums1 or not nums2:
			return []

		# Create set from smaller list.
		if len(nums1) > len(nums2):
			nums1, nums2 = nums2, nums1

		s = set(nums1)
		res = []

		for x in nums2:
			if x in s:
				res.append(x)
				s.remove(x)			
				if not s:
					break

		return res

###############################################################################
"""
https://leetcode.com/problems/intersection-of-two-arrays/solution/

This is a Facebook interview question.
They ask for the intersection, which has a trivial solution using a hash or a set.

Then they ask you to solve it under these constraints:
O(n) time and O(1) space (the resulting array of intersections is not taken 
into consideration).
You are told the lists are sorted.

Cases to take into consideration include:
duplicates, negative values, single value lists, 0's, and empty list arguments.
Other considerations might include sparse arrays.
"""

###############################################################################
"""
Solution 2: use two pointers.  No sets/dicts.

O(n log n + m log m) time: due to sorting
O(n + m) time other than sorting

O(1) extra space other than result
"""
class Solution2:
	def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
		nums1.sort()
		nums2.sort()

		res = []
		p1 = 0 # index/pointer for nums1
		p2 = 0 # index/pointer for nums2
		len1 = len(nums1)
		len2 = len(nums2)

		# This loop isn't entered if either input lists is empty.
		while p1 < len1 and p2 < len2:
			x2 = nums2[p2]
			while p1 < len1 and nums1[p1] < x2:
				p1 += 1

			if p1 >= len1:
				break

			x1 = nums1[p1]
			while p2 < len2 and nums2[p2] < x1:
				p2 += 1

			if p2 >= len2:
				break

			if x1 == nums2[p2]:
				res.append(x1)
				
				# Skip over duplicates.				
				while p1 < len1 and nums1[p1] == x1:
					p1 += 1

				while p2 < len2 and nums2[p2] == x1:
					p2 += 1

		return res

"""
Solution 2b: same idea as sol #2, but use simplified loop that does one
increment at a time per list.
"""
class Solution2b:
	def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
		nums1.sort()
		nums2.sort()

		res = []
		p1 = 0 # index/pointer for nums1
		p2 = 0 # index/pointer for nums2
		len1 = len(nums1)
		len2 = len(nums2)

		# This loop isn't entered if either input lists is empty.
		while p1 < len1 and p2 < len2:
			x1 = nums1[p1]
			x2 = nums2[p2]

			if x1 < x2:
				p1 += 1
			elif x2 < x1:
				p2 += 1
			else: # x1 == x2
				res.append(x1)
				p1 += 1
				p2 += 1

		return res

###############################################################################

if __name__ == "__main__":
	def test(nums1, nums2, comment=None):
		print("="*80)
		if comment:
			print(comment)

		print()
		print(f"\nnums1 = {nums1}")
		print(f"\nnums2 = {nums2}")

		res = sol.intersection(nums1, nums2)

		print(f"\nres = {res}\n")


	sol = Solution() # use 2 sets
	#sol = Solution1b() # use 1 set
	#sol = Solution2() # 2 pointers
	#sol = Solution2b() # 2 pointers, simplified loop

	comment = "LC ex1; answer = [2]"
	nums1 = [1,2,2,1]
	nums2 = [2,2]
	test(nums1, nums2, comment)

	comment = "LC ex1; answer = [9,4]"
	nums1 = [4,9,5]
	nums2 = [9,4,9,8,4]
	test(nums1, nums2, comment)

	comment = "LC test case; answer = [7]"
	nums1 = [9,3,7]
	nums2 = [6,4,1,0,0,4,4,8,7]
	test(nums1, nums2, comment)

	comment = "LC test case; answer = [3]"
	nums1 = [7,2,2,4,7,0,3,4,5]
	nums2 = [3,9,8,6,1,9]
	test(nums1, nums2, comment)

	comment = "One empty list; answer = []"
	nums1 = [1, 1, 2, 2, 3, 4, 5]
	nums2 = []
	test(nums1, nums2, comment)

	comment = "Both empty lists; answer = []"
	nums1 = []
	nums2 = []
	test(nums1, nums2, comment)
