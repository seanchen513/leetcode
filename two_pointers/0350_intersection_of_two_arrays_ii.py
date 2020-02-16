"""
350. Intersection of Two Arrays II
Easy

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""

from typing import List
import collections

###############################################################################
"""
Solution 1: use two dicts.

If the input lists are already sorted, we can make use of two pointers
(see other solutions).

If the length of nums1 is much smaller than the length of nums2, or vice versa,
then we can build the initial dict from the smaller list.  This way, checking
if values from the larger list are keys in the dict will be faster.

If memory is limited, load only a limited number of elements from p1 or p2 from
disk depending on their indices.  If result can be large, write partial result
to disk when its length gets too large and reset it.  Also have to deal with
dicts possibly being too large for memory.

O(n + m) time
O(min(n, m)) extra space: for dicts, determined by smaller list
"""
class Solution:
	def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
		d1 = collections.defaultdict(int)
		d2 = collections.defaultdict(int)
		res = []

		# Build the initial dict from the smaller list.
		if len(nums1) > len(nums2):
			nums1, nums2 = nums2, nums1

		for x in nums1:
			d1[x] += 1

		# The second dict only has keys that are also in the first dict.
		for x in nums2:
			if x in d1:
				d2[x] += 1

		for x, times in d2.items():
			res.extend( [x] * min(d1[x], times) )

		return res

"""
Solution 1b: same idea as sol #1, but use one dict.

This also means appending only one element at a time, which can be 
inefficient compared to using list's extend() if the element has a huge 
number of duplicates.
"""
class Solution1b:
	def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
		d1 = collections.defaultdict(int)
		res = []

		# Build the initial dict from the smaller list.
		if len(nums1) > len(nums2):
			nums1, nums2 = nums2, nums1

		for x in nums1:
			d1[x] += 1

		for x in nums2:
			if x in d1 and d1[x] > 0:
				res.append(x)
				d1[x] -= 1

		return res

###############################################################################
"""
Solution 2: use two pointers; no dicts/sets.

If the input lists are already sorted, we can make use of two pointers.

If the length of nums1 is much smaller than the length of nums2, or vice versa,
then the loop will end early.

If memory is limited, load only a limited number of elements from p1 or p2 from
disk depending on their indices.  If result can be large, write partial result
to disk when its length gets too large and reset it.

O(m + n) time other than sorting
O(1) extra space other than result
"""
class Solution2:
	def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
		nums1.sort()
		nums2.sort()

		res = []
		len1 = len(nums1)
		len2 = len(nums2)
		p1 = 0 # pointer/index for nums1
		p2 = 0 # pointer/index for nums2

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

			count = 0
			while p1 < len1 and p2 < len2 and x1 == nums1[p1] == nums2[p2]:
				count += 1
				p1 += 1
				p2 += 1
			 
			res.extend( [x1] * count )

		return res

"""
Solution 2b: same idea as sol #2b, but simplify the outer loop to do one
increment at a time per array.  

This also means appending only one element at a time, which can be 
inefficient compared to using list's extend() if the element has a huge 
number of duplicates.
"""
class Solution2b:
	def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
		nums1.sort()
		nums2.sort()

		res = []
		len1 = len(nums1)
		len2 = len(nums2)
		p1 = 0 # pointer/index for nums1
		p2 = 0 # pointer/index for nums2

		while p1 < len1 and p2 < len2:
			x1 = nums1[p1]
			if x1 < nums2[p2]:
				p1 += 1
			elif x1 > nums2[p2]:
				p2 += 1
			else:
				res.append(x1)
				p1 += 1
				p2 += 1

		return res

"""
Solution 2c: same idea as sol #2c, but overwrite nums1 instead of building
from a new list.  At the end, we end up making a copy of a sublist of nums1.

This is Approach 2 from:
https://leetcode.com/problems/intersection-of-two-arrays-ii/solution/
"""
class Solution2c:
	def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
		nums1.sort()
		nums2.sort()

		len1 = len(nums1)
		len2 = len(nums2)
		p1 = 0 # pointer/index for nums1
		p2 = 0 # pointer/index for nums2
		k = 0 # index for results sublist overwriting nums1

		while p1 < len1 and p2 < len2:
			x1 = nums1[p1]
			if x1 < nums2[p2]:
				p1 += 1
			elif x1 > nums2[p2]:
				p2 += 1
			else:
				nums1[k] = x1
				k += 1
				p1 += 1
				p2 += 1

		return nums1[:k]

###############################################################################

if __name__ == "__main__":
	def test(nums1, nums2, comment=None):
		print("="*80)
		if comment:
			print(comment)

		print()
		print(f"\nnums1 = {nums1}")
		print(f"\nnums2 = {nums2}")

		res = sol.intersect(nums1, nums2)

		print(f"\nres = {res}\n")


	sol = Solution() # use 2 dicts
	sol = Solution1b() # use 1 dict
	#sol = Solution2() # 2 pointers
	#sol = Solution2b() # 2 pointers, simplified loop
	#sol = Solution2c() # 2 pointers, simplified loop, overwrite nums1

	comment = "LC ex1; answer = [2,2]"
	nums1 = [1,2,2,1]
	nums2 = [2,2]
	test(nums1, nums2, comment)

	comment = "LC ex1; answer = [4,9]"
	nums1 = [4,9,5]
	nums2 = [9,4,9,8,4]
	test(nums1, nums2, comment)

	comment = "LC test case; answer = [1]"
	nums1 = [1,2]
	nums2 = [1,1]
	test(nums1, nums2, comment)
