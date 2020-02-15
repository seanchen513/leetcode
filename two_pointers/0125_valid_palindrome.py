"""
125. Valid Palindrome
Easy

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""

import re
import string

###############################################################################

class Solution:
	def isPalindrome(self, s: str) -> bool:
		s = ''.join(ch for ch in s.lower() if ch.isalnum())

		n = len(s)
		for i in range(n//2):
			if s[i] != s[n-i-1]:
				return False

		return True

		#return s == s[::-1]

###############################################################################

class Solution2:
	def isPalindrome(self, s: str) -> bool:
		s = list(filter(lambda x: x.isalnum(), s.lower()))

		# n = len(s)
		# for i in range(n//2):
		# 	if s[i] != s[n-i-1]:
		# 		return False

		# return True

		return s == s[::-1]

###############################################################################

class Solution3:
	def isPalindrome(self, s: str) -> bool:
		pattern = re.compile('[\W_]+', re.UNICODE)
		s = pattern.sub('', s.lower())
		
		return s == s[::-1]


###############################################################################

class Solution4:
	def isPalindrome(self, s: str) -> bool:
		s = re.sub('[\W_]+', '', s.lower())
		
		return s == s[::-1]

###############################################################################

if __name__ == "__main__":
	def test(s, comment=None):
		print("="*80)
		if comment:
			print(comment, "\n")

		print(f"\nstring = {s}")

		res = sol.isPalindrome(s)

		print(f"\nPalindrome, considering only alphanumeric chars and ignoring case?:\n{res}\n")


	sol = Solution() # ''.join()
	sol = Solution2() # filter()
	#sol = Solution3() # compiled regex pattern with sub()
	#sol = Solution4() # re.sub()

	comment = "LC ex1; answer = True"
	s = "A man, a plan, a canal: Panama"
	test(s, comment)

	comment = "LC ex2; answer = False"
	s = "race a car"
	test(s, comment)
