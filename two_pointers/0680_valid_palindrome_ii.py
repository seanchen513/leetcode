"""
680. Valid Palindrome II
Easy

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""

##############################################################################
"""
Solution: brute force.

O(n^2) time
O(n) extra space

TLE
"""
class Solution:
	def validPalindrome(self, s: str) -> bool:
		if s == s[::-1]:
		 	return True

		# deletes 1st char, ..., deletes last char
		for i in range(len(s)):
			t = s[:i] + s[i+1:]
			print(t)
			if t == t[::-1]:
				return True

		return False

##############################################################################
"""
Solution 2: Check if palindrome first.  If not, find the substring bounded by
the outermost mismatch, and test the substring with each of left or right 
char deleted.

O(n) time
O(n) extra space

Runtime: 52 ms, faster than 99.45% of Python3 online submissions
Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
	def validPalindrome(self, s: str) -> bool:
		if s == s[::-1]:
			return True

		left = 0
		right = len(s) - 1

		while s[left] == s[right]:
			left += 1
			right -= 1

		# The chars at "left" and "right" indices don't match.

		t = s[left:right] # delete right char
		if t == t[::-1]:
			return True

		t = s[left+1:right+1] # delete left char
		if t == t[::-1]:
			return True

		return False

##############################################################################
"""
Solution 3: While checking if palindrome, if come across a mismatch, test the 
substring with each of left or right char deleted.  Don't do initial quick
check "if s == s[::-1]".

O(n) time
O(n) extra space

Runtime: 100 ms, faster than 83.04% of Python3 online submissions
Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions
"""
class Solution3:
	def validPalindrome(self, s: str) -> bool:
		left = 0
		right = len(s) - 1

		while left < right and s[left] == s[right]:
			left += 1
			right -= 1

		if left >= right:
			return True

		t = s[left:right] # delete right char
		if t == t[::-1]:
			return True

		t = s[left+1:right+1] # delete left char
		if t == t[::-1]:
			return True
			
		return False

##############################################################################
"""
Solution 4: same as sol #2, but don't copy strings.

O(n) time
O(1) extra space

Runtime: 148 ms, faster than 62.51% of Python3 online submissions
Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions
"""
class Solution3:
	def validPalindrome(self, s: str) -> bool:
		def valid(left, right):
			n = (right - left + 1) // 2
			return all(s[left + k] == s[right - k] for k in range(n))

		n = len(s)//2
		for i in range(n):
			if s[i] != s[~i]: # ~i = -(i+1) = -i-1
				end = len(s) - i - 1
				return valid(i+1, end) or valid(i, end-1)

		return True

###############################################################################

if __name__ == "__main__":
	def test(s, comment=None):
		print("="*80)
		if comment:
			print(comment, "\n")

		print(f"\nstring = {s}")

		res = sol.validPalindrome(s)

		print(f"\nPalindrome, after deleting at most one char?:\n{res}\n")


	sol = Solution() # brute force
	sol = Solution2() # initial quick check
	sol = Solution3() # no initial quick check
	#sol = Solution4() # same as , but don't copy strings
		
	comment = "LC ex1; answer = True"
	s = "aba"
	test(s, comment)

	comment = "LC ex2; answer = True"
	s = "abca"
	test(s, comment)

	comment = "Delete at end; answer = True"
	s = "abcbaf"
	test(s, comment)

	comment = "LC test case; answer = True"
	s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
	test(s, comment)
		
	comment = "LC test case; answer = False"
	s = "abc"
	test(s, comment)
