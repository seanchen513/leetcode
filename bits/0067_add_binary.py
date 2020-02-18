"""
67. Add Binary
Easy

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

###############################################################################
"""
Solution 1: use int(x, base) and format().
"""
class Solution:
	def addBinary(self, a: str, b: str) -> str:
		return '{:b}'.format( int(a, base=2) + int(b, base=2) )

###############################################################################
"""
Solution 2: add bit by bit with carries.
"""
class Solution2:
	def addBinary(self, a: str, b: str) -> str:
		n = max(len(a), len(b))
		a, b = a.zfill(n), b.zfill(n)

		res = []
		s = 0 # sum
		
		for i in range(n-1, -1, -1):
			if a[i] == '1': s += 1
			if b[i] == '1': s += 1

			if s & 1: # ie, odd, or equal to 1 or 3
				res.append('1')
			else:
				res.append('0')

			s >>= 1 # keep the carry part

		if s: # there's a carry left over
			res.append('1')

		return ''.join(reversed(res))

###############################################################################
"""
Solution 3: bit manipulation without using +.

O(n+m) time, where n and m are lengths of input strings.
O(max(n,m)) extra space: for answer.
"""
class Solution3:
	def addBinary(self, a: str, b: str) -> str:
		x = int(a, base=2)
		y = int(b, base=2)

		while y:
			x, y = x ^ y, (x & y) << 1 # sum ignoring carry, and carry

		return f"{x:b}"
		#return bin(x)[2:]


###############################################################################

if __name__ == "__main__":
	def test(a, b, comment=None):
		print("="*80)
		if comment:
			print(comment)

		print()
		print(f"{a}")
		print(f"{b}")
		
		res = sol.addBinary(a, b)
		print(f"\nres = {res}")

	sol = Solution()
	sol = Solution2() # add bit by bit with carries
	#sol = Solution3() # bit manipulation

	comment = 'LC ex1; answer = "100"'
	a = "11"
	b = "1"
	test(a, b, comment)

	comment = 'LC ex2; answer = 10101"'
	a = "1010"
	b = "1011"
	test(a, b, comment)
