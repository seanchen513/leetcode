"""
322. Coin Change
Medium

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""

from typing import List
import functools

###############################################################################
"""
Solution: DP tabulation.

O(amount * len(coins)) time: ignore sorting coins...
O(amount) extra space

Runtime: 1788 ms, faster than 23.93% of Python3 online submissions
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
	def coinChange(self, coins: List[int], amount: int) -> int:
		if amount == 0:
			return 0

		coins.sort()

		dp = [-1]*(amount+1) # min coins needed to make amount that is index
		for c in coins:
			if c <= amount:
				dp[c] = 1

		for i in range(coins[0], amount + 1): # amount of money
			for c in coins:
				if i - c >= 0 and dp[i-c] >= 1:
					if dp[i] >= 1:
						dp[i] = min(dp[i], 1 + dp[i-c])
					else:
						dp[i] = 1 + dp[i-c]

		return dp[amount]

"""
Solution 1b: same as sol 1, but use default INF instead of -1 for dp values.

Runtime: 1420 ms, faster than 52.43% of Python3 online submissions
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions
"""
class Solution1b:
	def coinChange(self, coins: List[int], amount: int) -> int:
		if amount == 0:
			return 0

		coins.sort()
		INF = float('inf')

		dp = [INF]*(amount+1) # min coins needed to make amount that is index
		for c in coins:
			if c <= amount:
				dp[c] = 1

		for i in range(coins[0], amount + 1): # amount of money
			for c in coins:
				if i - c >= 0:
					dp[i] = min(dp[i], 1 + dp[i-c])

		return dp[amount] if dp[amount] < INF else -1

"""
Solution 1c: same as sol 1b, but loop over coins first, and incorporate the
cases of 1 coin into the loop.

Notes:
- Don't need initial check for amount 0
- Initialize dp[0] = 0

Runtime: 1216 ms, faster than 82.21% of Python3 online submissions for Coin Change.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Coin Change.
"""
class Solution1c:
	def coinChange(self, coins: List[int], amount: int) -> int:
		coins.sort(reverse=True)
		INF = float('inf')

		dp = [0] + [INF]*amount # min coins needed to make amount that is index

		for c in coins:
			for amt in range(c, amount + 1):
				dp[amt] = min(dp[amt], 1 + dp[amt - c])

		return dp[amount] if dp[amount] < INF else -1

###############################################################################
"""
Solution 2: recursion

TLE on coins = [1,2,5], amount = 100.
"""
class Solution2:
	def coinChange(self, coins: List[int], amount: int) -> int:
		def rec(a):
			if a < 0:
				return INF
			if a == 0:
				return 0

			min_coins = INF
			for c in coins:
				min_coins = min(min_coins, rec(a-c))

			return 1 + min_coins

		INF = float('inf')
		
		min_coins = rec(amount)

		return min_coins if min_coins < INF else -1

###############################################################################
"""
Solution 3: recursion w/ memoization via @functools.lru_cache(None)

Runtime: 1320 ms, faster than 66.48% of Python3 online submissions
Memory Usage: 43.9 MB, less than 5.55% of Python3 online submissions
"""
class Solution3:
	def coinChange(self, coins: List[int], amount: int) -> int:
		@functools.lru_cache(None)
		def rec(a):
			if a < 0:
				return INF
			if a == 0:
				return 0

			min_coins = INF
			for c in coins:
				min_coins = min(min_coins, rec(a-c))

			return 1 + min_coins

		INF = float('inf')
		
		min_coins = rec(amount)

		return min_coins if min_coins < INF else -1

###############################################################################
"""
Solution 4: recursion w/ memoization.

Runtime: 1688 ms, faster than 29.60% of Python3 online submissions
Memory Usage: 45.8 MB, less than 5.55% of Python3 online submissions
"""
class Solution4:
	def coinChange(self, coins: List[int], amount: int) -> int:
		def rec(a):
			if a in memo:
				return memo[a]

			if a < 0:
				memo[a] = INF
				return INF

			min_coins = INF
			for c in coins:
				min_coins = min(min_coins, rec(a-c))

			memo[a] = 1 + min_coins

			return memo[a]

		INF = float('inf')
		memo = {0: 0} # if a==0: return 0
		
		min_coins = rec(amount)

		return min_coins if min_coins < INF else -1

###############################################################################
"""
Solution 5: branch and bound.

https://leetcode.com/problems/coin-change/discuss/77454/Fast-python-branch-and-bound-solution-beaten-99-python-submissions

Runtime: 72 ms, faster than 98.34% of Python3 online submissions
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions
"""
class Solution5:
	def coinChange(self, coins: List[int], amount: int) -> int:		
		# start = index in coins list to start with
		def bb_search(coins, start, amount, n_coins):
			nonlocal min_coins

			coin = coins[start]

			# lower bound on number of coins, achieved using the current coin
			lowerBound = n_coins + (amount + coin - 1) / coin

			if lowerBound > min_coins:
				return
			
			# if amount matches the biggest coin, that is the solution
			if amount == coin and n_coins + 1 < min_coins:
				min_coins = n_coins + 1
				return
			
			# try to use the current coin again
			if amount > coin:
				bb_search(coins, start, amount - coin, n_coins + 1)
			
			# try to use the next smaller coin
			if start + 1 < len(coins):
				bb_search(coins, start + 1, amount, n_coins)

		if amount == 0:
			return 0
		
		# try biggest coins first
		coins = sorted(coins, reverse=True)

		# upper bound on number of coins (+1 to represent the impossible case)
		#upperBound = (amount + coins[-1] - 1) / coins[-1] + 1

		min_coins = float('inf') # upperBound
		
		bb_search(coins, 0, amount, 0)

		return min_coins if min_coins < float('inf') else -1

"""
Solution 5b: recursion w/ early returns.  Branch and bound.

https://leetcode.com/problems/coin-change/discuss/77416/Python-11-line-280ms-DFS-with-early-termination-99-up

Runtime: 144 ms, faster than 97.69% of Python3 online submissions
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions
"""
class Solution5b:
	def coinChange(self, coins: List[int], amount: int) -> int:
		def rec(start_coin, coin_count, amt):
			nonlocal min_coins

			if amt == 0 and coin_count < min_coins:
				min_coins = coin_count
				return
				#return min(min_coins, coin_count)

			coins_diff = min_coins - coin_count

			for i in range(start_coin, len_coins): # largest to smallest
				if coins[i] <= amt:
					max_amt_poss = coins[i] * coins_diff

					#if coins[i] <= amt < max_amt_poss:
					if amt < max_amt_poss:
						rec(i, coin_count + 1, amt - coins[i])

		len_coins = len(coins)
		min_coins = float('inf')

		coins.sort(reverse=True)
		
		#min_coins = rec(0, 0, amount)
		rec(0, 0, amount)

		return min_coins if min_coins < float('inf') else -1

###############################################################################

if __name__ == "__main__":
	def test(coins, amount, comment=None):
		print("="*80)
		if comment:
			print(comment)

		print()
		print(f"\ncoins = {coins}")
		print(f"amount = {amount}")
		
		res = sol.coinChange(coins, amount)
		print(f"\nres = {res}")

	sol = Solution() # tabulation
	sol = Solution1b()
	sol = Solution1c()
	#sol = Solution2() # recursion
	#sol = Solution3() # memoization via @functools.lru_cache(None)
	#sol = Solution4() # memoization
	sol = Solution5() # branch and bound
	sol = Solution5b() # branch and bound #2, slower

	comment = 'LC ex1; answer = 3'
	coins = [1,2,5]
	amount = 11
	test(coins, amount, comment)

	comment = 'LC ex2; answer = -1'
	coins = [2]
	amount = 3
	test(coins, amount, comment)

	comment = 'LC test case; answer = 0'
	coins = [1]
	amount = 0
	test(coins, amount, comment)

	comment = "LC test case; TLE's basic recursion; answer = 20"
	coins = [1,2,5]
	amount = 100
	test(coins, amount, comment)

	comment = "LC test case; answer = 2"
	coins = [1,2147483647]
	amount = 2
	test(coins, amount, comment)

	comment = "LC test case; answer = 20"
	coins = [186,419,83,408]
	amount = 6249
	test(coins, amount, comment)
