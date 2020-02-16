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
Solution 1: use sets.

O(n + m) time
O(n + m) extra space: for sets
"""
class Solution:
	def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
		return list(set(nums1) & set(nums2))

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

		# This loop isn't entered if either input lists are empty.
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

		print(f"\nres = {res}")


	sol = Solution() # use sets
	sol = Solution2() # 2 pointers

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
