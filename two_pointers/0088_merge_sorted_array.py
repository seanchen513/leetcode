"""
88. Merge Sorted Array
Easy

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""

from typing import List

###############################################################################
"""
Solution 1: use two pointers, starting from ends.

O(m+n) time
O(1) extra space
"""
class Solution:
	def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
		"""
		Do not return anything, modify nums1 in-place instead.
		"""
		x = m - 1
		y = n - 1
		
		#for i in range(m+n-1, -1, -1):
		i = m + n - 1
		while x >= 0 and y >= 0:
			if nums1[x] > nums2[y]:
				nums1[i] = nums1[x]
				x -= 1
			else:
				nums1[i] = nums2[y]
				y -= 1
				
			i -= 1
			
		if y >= 0:
			nums1[:y+1] = nums2[:y+1]

###############################################################################
"""
Solution 2: copy nums2 to free space in nums1, then sort.

O((m+n) log(m+n)) time
O(1) extra space
"""	
class Solution2:
	def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
		nums1[m:] = nums2
		nums1.sort()

###############################################################################

if __name__ == "__main__":
	def test(nums1, m, nums2, n, comment=None):
		print("="*80)
		if comment:
			print(comment, "\n")

		print(f"\nnums1 = {nums1}")
		print(f"m = {m}")
		print(f"\nnums2 = {nums2}")
		print(f"n = {n}")

		sol.merge(nums1, m, nums2, n)

		print(f"\nnums1 AFTER merge: {nums1}\n")


	sol = Solution()
	sol = Solution2()

	comment = "LC example; answer = [1,2,2,3,5,6]"
	nums1 = [1,2,3,0,0,0]
	m = 3
	nums2 = [2,5,6]
	n = 3
	test(nums1, m, nums2, n, comment)
