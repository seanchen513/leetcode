"""
66. Plus One
Easy

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""

from typing import List

###############################################################################
"""
Solution 1: Process input list and create result list digit-by-digit, using
carries.
"""
class Solution:
	def plusOne(self, digits: List[int]) -> List[int]:
		res = []
		c = 1 # carry; start with 1 since we are adding one
		
		for d in reversed(digits): # start with units digit
			d += c
			if d > 9:
				d -= 10
				c = 1
			else:
				c = 0
			res.append(d)

		if c == 1:
			res.append(1)
			
		return res[::-1]

###############################################################################
"""
Solution 2: Convert to integer, add one, then take digits.
"""
class Solution2:
	def plusOne(self, digits: List[int]) -> List[int]:
		n = 0
		p10 = 1

		for d in reversed(digits):
			n += d * p10
			p10 *= 10

		return [int(d) for d in str(n+1)]

"""
Solution 2b: same as sol #2b, but using map().
"""
class Solution2b:
	def plusOne(self, digits: List[int]) -> List[int]:
		# n = int(''.join(map(str, digits)))
		# return map(int, str(n+1))
		
		#return map(int, str(int(''.join(map(str, digits)))+1))
		return list(map(int, str(int(''.join(map(str, digits)))+1)))

###############################################################################

if __name__ == "__main__":
	def test(arr, comment=None):
		print("="*80)
		if comment:
			print(comment)

		print()
		print(f"{arr}")
		
		res = sol.plusOne(arr)
		print(f"\nres = {res}")

	sol = Solution() # process digit by digit and use carries
	sol = Solution2() # convert to int, add one, take digits
	sol = Solution2b() # same as #2, but use map()

	comment = "LC ex1; answer = [1,2,4]"
	arr = [1,2,3]
	test(arr, comment)

	comment = "LC ex2; answer = [4,3,2,2]"
	arr = [4,3,2,1]
	test(arr, comment)
