"""
1354. Construct Target Array With Multiple Sums
Hard

Given an array of integers target. From a starting array, A consisting of all 1's, you may perform the following procedure :

let x be the sum of all elements currently in your array.
choose index i, such that 0 <= i < target.size and set the value of A at index i to x.
You may repeat this procedure as many times as needed.
Return True if it is possible to construct the target array from A otherwise return False.

Example 1:

Input: target = [9,3,5]
Output: true
Explanation: Start with [1, 1, 1] 
[1, 1, 1], sum = 3 choose index 1
[1, 3, 1], sum = 5 choose index 2
[1, 3, 5], sum = 9 choose index 0
[9, 3, 5] Done

Example 2:

Input: target = [1,1,1,2]
Output: false
Explanation: Impossible to create target array from [1,1,1,1].

Example 3:

Input: target = [8,5]
Output: true
 
Constraints:

N == target.length
1 <= target.length <= 5 * 10^4
1 <= target[i] <= 10^9
"""

from typing import List
import heapq

###############################################################################
"""
Solution: Work backwards.  No heap.

Let mx == prev_sum, s == current sum, prev_val = previous value of mx.
Let "others" = sum of other terms (in either current or previous array).

Have two linear equations (parentheses for comments):
prev_val + others = mx
mx + others = s

So:
prev_val 
= mx - others
= mx - (s - mx)
= 2*mx - s

Runtime: 320 ms, faster than 20.00% of Python3 online submissions
Memory Usage: 18.4 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
	def isPossible(self, target: List[int]) -> bool:
		n = len(target)
		s = sum(target)
		if n == 1:
			return True if s == 1 else False

		# Values are always positive integers (they start that way, and
		# the loop returns False if any value turns non-positive).
		# Therefore, the sum is always >= n, with n being achieved
		# exactly when all values are 1.
		while s != n:
			mx = max(target)
			for mx_i, val in enumerate(target):
				if val == mx:
					break

			prev_val = 2*mx - s

			if prev_val < 1:
				return False

			target[mx_i] = prev_val 

			# For next iteration, the sum is the same as the current max
			s = mx
		
		return True

###############################################################################
"""
Solution 2: same as sol #1, but use max heap.

Runtime: 272 ms, faster than 93.47% of Python3 online submissions
Memory Usage: 18.1 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
	def isPossible(self, target: List[int]) -> bool:
		n = len(target)
		s = sum(target)
		if n == 1:
			return True if s == 1 else False

		h = [-x for x in target] # max heap
		heapq.heapify(h)
		
		while s != n:	
			mx = -heapq.heappop(h)
			mx2 = -h[0]

			prev_val = 2*mx - s
			
			if prev_val < 1:
				return False
			
			heapq.heappush(h, -prev_val)
			
			# For next iteration, the sum is the same as the current max
			s = mx

		return True

###############################################################################
"""
Solution 3: same as sol #2, using max heap, but add a nested loop to iterate 
prev_val until it becomes lower than the second largest element.

Not much of an improvement over sol #2.
"""
class Solution3:
	def isPossible(self, target: List[int]) -> bool:
		n = len(target)
		s = sum(target)
		if n == 1:
			return True if s == 1 else False

		h = [-x for x in target] # max heap
		heapq.heapify(h)
		
		while s != n:	
			mx = -heapq.heappop(h)
			mx2 = -h[0]

			prev_val = 2*mx - s
			while prev_val > mx2:
				s = mx
				mx = prev_val
				prev_val = 2*mx - s
			
			if prev_val < 1:
				return False
			
			heapq.heappush(h, -prev_val)
			
			# For next iteration, the sum is the same as the current max
			s = mx

		return True

###############################################################################
"""
Solution 4: same as sol #2, using max heap, but calculate prev_val (simulating
iteration on it) so that it is <= second largest value.

This is efficient for cases where they is a large difference between the
largest and second largest values.
"""
import math
class Solution4:
	def isPossible(self, target: List[int]) -> bool:
		n = len(target)
		s = sum(target)
		if n == 1: # [1] is only possible target
			return True if s == 1 else False
		if n == s: # all 1's
			return True

		h = [-x for x in target] # max heap
		heapq.heapify(h)
		
		while s != n: # ie, not all terms are 1
			mx = -heapq.heappop(h)
			mx2 = -h[0] # 2nd largest term before loop was entered.

			# Cannot have duplicates that are > 1.
			# We already returned from the case where all terms are 1,
			# so mx and mx2 cannot be 1 here.
			if mx == mx2:
				return False

			k = math.ceil( (mx - mx2) / (s - mx) ) # note: k > 0
			prev_val = mx - k * (s - mx) # this makes prev_val <= mx2

			if prev_val < 1:
				return False
			
			heapq.heappush(h, -prev_val)
			
			# For next iteration, the new sum is this.
			# All terms the same except mx replaced by prev_val.
			s += prev_val - mx 

		return True

###############################################################################
"""
Solution 5: same as sol #4, but include some quick checks.

LeetCode Feb 17, 2020:
Runtime: 256 ms, faster than 99.77% of Python3 online submissions
Memory Usage: 18.3 MB, less than 100.00% of Python3 online submissions
"""
class Solution5:
	def isPossible(self, target: List[int]) -> bool:
		n = len(target)
		s = sum(target)
		if n == 1: # [1] is only possible target
			return True if s == 1 else False
		if n == s: # all 1's
			return True

		if n == 2: # target only possible if terms are relatively prime
			x, y = target
			while y:
				x, y = y, x % y # note x % 1 == 0
				
			return x == 1
		
		## If n is odd, every term must be odd.
		## This check isn't necesary since it's included in the check below.
		#if n & 1:
		#	if any(x & 1 == 0 for x in target):
		#		return False

		# n >= 3 now
		# Every term has the form a = (n-1)k + 1 for some k >= 0.
		# So a - 1 = (n-1)k, so (a - 1) % (n - 1) == 0.
		# If n is odd, this implies every term is odd.
		n1 = n - 1
		if any((x-1) % n1 for x in target):
			return False

		# General case

		h = [-x for x in target] # max heap
		heapq.heapify(h)
		
		while s != n: # ie, not all terms are 1
			mx = -heapq.heappop(h)
			mx2 = -h[0] # 2nd largest term before loop was entered.

			# Cannot have duplicates that are > 1.
			# We already returned from the case where all terms are 1,
			# so mx and mx2 cannot be 1 here.
			if mx == mx2:
				return False

			k = math.ceil( (mx - mx2) / (s - mx) ) # note: k > 0
			prev_val = mx - k * (s - mx) # this makes prev_val <= mx2

			if prev_val < 1:
				return False
			
			heapq.heappush(h, -prev_val)
			
			# For next iteration, the new sum is this.
			# All terms the same except mx replaced by prev_val.
			s += prev_val - mx 

		return True

###############################################################################
"""
Solution 6: simplified version.  Removed quick checks.

Replaced:

k = math.ceil( (mx - mx2) / (s - mx) ) 
prev_val = mx - k * (s - mx)

with:

prev_val = mx % (s - mx) 

Reason:
prev_val = mx - others = mx - (s - mx)
Taking modulo is just repeated subtraction of (s - mx).

Runtime: 260 ms, faster than 99.32% of Python3 online submissions
Memory Usage: 18.1 MB, less than 100.00% of Python3 online submissions
"""
class Solution6:
	def isPossible(self, target: List[int]) -> bool:
		n = len(target)
		s = sum(target)
		
		h = [-x for x in target if x > 1] # max heap
		heapq.heapify(h)
		
		while s != n: # ie, not all terms are 1
			mx = -heapq.heappop(h)
			other = s - mx
			# if 2 * mx < 1 + s:
			if mx <= other: # in particular, mx cannot have duplicates
				return False

			# Now, 2*mx >= 1 + s		# or mx >= 1 + other
			# mx >= 1 + (s - mx).		# mx % other < other < mx
			# mx > s - mx.
			# mx % (s - mx) < s - mx < mx.

			# This check is necessary if we haven't dealt with the case
			# [1, mx] before the loop.  Eg, if didn't check the case n = 2.
			if other == 1:
				return True

			#prev_val = mx % (s - mx)
			prev_val = mx % other
			if prev_val < 1:
				return False

			heapq.heappush(h, -prev_val)
			
			# For next iteration, the new sum is this.
			# All terms the same except mx replaced by prev_val.
			s += prev_val - mx 

		return True

###############################################################################

if __name__ == "__main__":
	def test(target, comment=None):
		print("="*80)
		if comment:
			print(comment)

		print()
		print(f"target = {target}")

		res = sol.isPossible(target)
		print(f"\nres = {res}")

	def test2():
		for i in range(1, 11):
			for j in range(1, 11):
				target = [i, j]
				res = sol.isPossible(target)
				if res:
					print(f"{i}, {j}: {res}")

	def test3(i=3, j=5):
		for k in range(j, 20*j + 1):
			target = [i, j, k]
			res = sol.isPossible(target)
			if res:
				print(f"{target}: {res}    diffs = [{j-i},{k-j}]")


	sol = Solution()
	#sol = Solution2() # use max heap
	#sol = Solution3() # max heap, iterate prev_val
	#sol = Solution4() # max heap, calc prev_val
	#sol = Solution5() # same as sol #4, but with some quick checks
	sol = Solution6() # simplified version, using prev_val = mx % other

	#test2()
	#test3()
	#test3(3,5)
	#exit()
	
	comment = "LC ex1; answer = True"
	target = [9,3,5]
	test(target, comment)

	comment = "LC ex1; answer = False"
	target = [1,1,1,2]
	test(target, comment)

	comment = "LC ex3; answer = True"
	target = [8,5]
	test(target, comment)

	comment = "LC test case; answer = False"
	target = [9,9,9]
	test(target, comment)

	comment = "answer = False"
	target = [2, 2]
	test(target, comment)

	comment = "answer = False"
	target = [1,1,2]
	test(target, comment)

	comment = "answer = False"
	target = [2, 2]
	test(target, comment)

	comment = "answer = False"
	target = [5,7,9]
	test(target, comment)

	comment = "answer = True"
	target = [3,5,9]
	test(target, comment)

	comment = "answer = False"
	target = [3,5,64]
	test(target, comment)

	comment = "LC test case; answer = False"
	target = [1,1,1,6,11,16]
	test(target, comment)

	comment = "Value limit / 10 = 10^8; answer = True"
	target = [100000000,1]
	test(target, comment)

	#comment = "Value limit 10^9; answer = True"
	#target = [1000000000,1]
	#test(target, comment)

	
"""
- Case n=1: only [1] is True.

- Case n=2: True if and only if gcd of the two elts is 1.
- In particular, [1, x] is True for all x >= 1
- Cannot have duplicates, unless they are 1s.

- If n is odd, the initial sum is odd, so the next term is odd.  Then the
second sum is odd, so the next term is odd.  Etc.  If n is odd, all terms
must be odd.  This is actually a special case of a more general result.
"""

"""
- If n = len(target) >= 3, then target cannot contain 2, ..., n-1.
- Because of 2nd iteration, target cannot contain n+1, ..., 2n-2.
- Because of 3rd iteration, target cannot contain 2n, ..., 3n-3.
- Because of 4th iteration, target cannot contain 3n-1, ..., 4n-4.
- etc...
- Target can contain:
1, n, 2n-1, 3n-2, 4n-3, ..., n**2 - (n-1) = n**2 - n + 1.
- Ie, can have: k(n-1) + 1 for k=0,...,n.
- This actually generalizes for k > n.
- This might not be quite correct for higher iterations.
- Probably only useful to check for first one or two iterations:

Example: n = 3.
n**2 - n + 1 = 7.
Can have 1, 3, 5, 7.
Cannot have 2, 4, 6.
In fact, cannot have any even numbers since n is odd.

Example: n = 4.
n**2 - n + 1 = 13.
Can have 1, 4, 7, 10, 13.
Cannot have 2,3, 5,6, 8,9, 11, 12.

Example: n = 6.
n**2 - n + 1 = 31.
Can have 1, 6, 11, 16, 21, 26, 31.
Cannot have 2,3,4,5, 7,8,9,10, 12,13,14,15, ..., 27,28,29,30.
"""

"""
Every term has the form a = (n-1)k + 1 for some k >= 0.

So a - 1 = (n-1)k, so (a - 1) % (n - 1) == 0.

If n is odd, this implies every term is odd.
"""
