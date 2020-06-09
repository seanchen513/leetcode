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
import collections

"""
This is an unbounded knapsack problem.
The standard way to solve it is using memoized recursion or DP tabulation.
However, there are branch & bound solutions that are much faster.

Note that using a pure greedy method (choose as many of the larger coins
as possible) does not work for arbitrary coin denominations.
"""

###############################################################################
"""
Solution: DP tabulation w/ 1d table.

dp[amt] = min coins needed to make "amt" of money.

dp is initialized for the cases of using just 1 coin.
This allows the loop for "amt" to start at min_coin + 1 rather than min_coin.

This also means the main loop never makes use of dp[0].
So we don't need to initialize dp[0] = 0, as long as we take care of
the trivial case amount = 0 by checking it at the start.
Alternatively, we could set dp[0] = 0 for the sole purpose of dealing with
the trivial case amount = 0, even though the main loop never makes use of it.

O(amount * len(coins)) time
O(amount) extra space

Runtime: 1420 ms, faster than 52.43% of Python3 online submissions
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: # necessary if we don't set dp[0] = 0.
            return 0

        min_coin = min(coins)
        INF = float('inf')

        dp = [INF] * (amount + 1)
        
        # Initialize dp for the cases where amount == some coin value.
        for c in coins:
            if c <= amount:
                dp[c] = 1

        for amt in range(min_coin + 1, amount + 1): # amount of money
            for c in coins:
                if c < amt: # don't need <= because of initialization above
                    dp[amt] = min(dp[amt], 1 + dp[amt - c])

        return dp[amount] if dp[amount] < INF else -1

"""
Solution 1b: same, but incorporate the cases of 1 coin into loop.

This is why we use "c <= amt" rather than "c < amt".
We also need to initialize dp[0] = 0 (0 coins to make amount 0).

"""
class Solution1b:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float('inf')
        min_coin = min(coins) # optional

        dp = [0] + [INF] * amount
        
        #for amt in range(1, amount + 1):
        for amt in range(min_coin, amount + 1): # starting from min_coin is optional
            for c in coins:
                if c <= amt: # <= required rather than <
                    dp[amt] = min(dp[amt], 1 + dp[amt - c])

        return dp[amount] if dp[amount] < INF else -1

"""
Solution 1c: same, but reverse order of loops.

Note how we don't need an "if" statement within the nested loops. 
Instead, "amt" in the inner loop starts at "c".

Runtime: 1216 ms, faster than 82.21% of Python3 online submissions for Coin Change.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Coin Change.
"""
class Solution1c:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float('inf')

        dp = [0] + [INF] * amount

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
        def rec(amt):
            if amt < 0:
                return INF
            if amt == 0:
                return 0

            # min_coins = INF
            # for c in coins:
            #     min_coins = min(min_coins, rec(amt - c))

            # return 1 + min_coins

            return 1 + min(rec(amt - c) for c in coins)

        INF = float('inf')
        
        min_coins = rec(amount)

        return min_coins if min_coins < INF else -1

###############################################################################
"""
Solution 3: recursion w/ memoization via @functools.lru_cache(None)

Runtime: 1320 ms, faster than 66.48% of Python3 online submissions
Memory Usage: 43.9 MB, less than 5.55% of Python3 online submissions
"""
import functools
class Solution3:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @functools.lru_cache(None)
        def rec(amt):
            if amt < 0:
                return INF
            if amt == 0:
                return 0

            # min_coins = INF
            # for c in coins:
            #     min_coins = min(min_coins, rec(amt - c))

            # return 1 + min_coins

            return 1 + min(rec(amt - c) for c in coins)

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
        def rec(amt):
            if amt in memo:
                return memo[amt]

            if amt < 0:
                memo[amt] = INF
                return INF

            # min_coins = INF
            # for c in coins:
            #     min_coins = min(min_coins, rec(amt - c))

            # memo[amt] = 1 + min_coins

            memo[amt] = 1 + min(rec(amt - c) for c in coins)

            return memo[amt]

        INF = float('inf')
        memo = {0: 0} # if a==0: return 0
        
        min_coins = rec(amount)

        return min_coins if min_coins < INF else -1

###############################################################################
"""
Solution 5: BFS using queue.

https://leetcode.com/problems/coin-change/discuss/280435/Python-BFS-Queue-(Branch-and-Bound)

"""
class Solution5:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0 
        
        q = collections.deque([amount])
        count = 0 
        seen = set()
        
        coins.sort(reverse=True) # not necessary without bounds checking

        while q:
            count += 1 
            n = len(q)
            
            for _ in range(n):
                amt = q.popleft()
                
                if amt not in seen:
                    # key point (simple branch and bound)
                    seen.add(amt)
                    
                    for c in coins:
                        if c == amt:
                            return count
                        elif c < amt:
                            q.append(amt - c)
                            
        return -1

###############################################################################
""" 
Solution 6: branch and bound, v1. (much faster than DP or BFS)

Pruned DFS.
Sorting makes the pruning much faster (closer to the root of DFS tree).

Based on:
https://leetcode.com/problems/coin-change/discuss/77454/Fast-python-branch-and-bound-solution-beaten-99-python-submissions

Use the general check "if amt % coin == 0" rather than "if amt == coin"
or "if amt == 0". This helps deal with situations like:
    coins = [10], amount = 1234560

Runtime: 68 ms, faster than 99.27% of Python3 online submissions
Memory Usage: 13.9 MB, less than 74.93% of Python3 online submissions
"""
import functools
class Solution6:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #@functools.lru_cache(None)
        def bb_search(i, amt, n_coins): # i = index in coins
            nonlocal min_coins

            coin = coins[i]

            # LHS = lower bound on number of coins, achieved using the current coin
            # Return early since we can't possibly achieve original "amount"
            # along this path.
            # This is key to why this solution is so fast.
            if n_coins + (amt + coin - 1) / coin > min_coins:
                return
            
            if amt % coin == 0: # original "amount" achieved
                min_coins = min(min_coins, n_coins + amt // coin)
                return
            
            # try to use the current coin again
            if amt > coin:
                bb_search(i, amt - coin, n_coins + 1)
            
            # try to use the next smaller coin
            if i + 1 < len(coins):
                bb_search(i + 1, amt, n_coins)

        if amount == 0: # necessary
            return 0
        
        # try biggest coins first
        coins = sorted(coins, reverse=True)

        ### Upper bound on number of coins (+1 to represent the impossible case).
        ### coins[-1] = smallest coin value.
        #upper_bound = (amount + coins[-1] - 1) / coins[-1] + 1

        min_coins = float('inf')
        #min_coins = upper_bound
        
        bb_search(0, amount, 0)

        return min_coins if min_coins < float('inf') else -1
        #return min_coins if min_coins < upper_bound else -1

###############################################################################
""" 
Solution 7: branch & bound, v2.

BEST SOLUTION: much faster than DP, and covers cases better than
other branch & bound solutions here.

Based on: ("improved DFS")
https://leetcode.com/problems/coin-change/discuss/114993/Four-kinds-of-solutions%3A-DP-BFS-DFS-improved-DFS

But also includes the extra, optional check
"if n_coins + (amt + coin - 1) / coin > min_coins".

Runtime: 52 ms, faster than 99.86% of Python3 online submissions
Memory Usage: 13.8 MB, less than 95.33% of Python3 online submissions
"""
class Solution7:
    def coinChange(self, coins, amount):
        def dfs(start, amt, n_coins):
            nonlocal min_coins

            coin = coins[start]

            # LHS = lower bound on number of coins, achieved using the current coin
            # Return early since we can't possibly achieve original "amount"
            # along this path.
            # For this particular solution, this check isn't necessarily,
            # since there is another check within the loop below. However, it
            # speeds up the solution. Better to have this check before the
            # "amt == 0" check below.
            if n_coins + (amt + coin - 1) / coin > min_coins:
                return

            div = amt // coin
            n_coins += div
            amt %= coin
            
            if amt == 0:
                min_coins = min(min_coins, n_coins)
                return
            
            if start < len_coins:
                # use as many of current coin as possible, and try next smaller coin
                dfs(start + 1, amt, n_coins)

                # Always greedily taking as many of biggest coins as possible doesn't work.
                # "Backtrack" by using 1 less of current coin per iteration, and
                # trying the next smaller coin.

                next_coin = coins[start + 1]
                
                for _ in range(div):
                    amt += coin 
                    n_coins -= 1
                    
                    if (min_coins - n_coins) * next_coin > amt: # hope still exists
                        dfs(start + 1, amt, n_coins)
                    else:
                        break
        
        len_coins = len(coins) - 1
        
        # try biggest coins first
        coins.sort(reverse=True)
        
        min_coins = float('inf')

        dfs(0, amount, 0)
        
        return min_coins if min_coins < float('inf') else -1

###############################################################################
"""
Solution 8: branch and bound, v3.

https://leetcode.com/problems/coin-change/discuss/77416/Python-11-line-280ms-DFS-with-early-termination-99-up

Runtime: 144 ms, faster than 97.69% of Python3 online submissions
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions
"""
class Solution8:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def rec(start_coin, coin_count, amt):
            nonlocal min_coins

            if amt == 0:
                min_coins = min(min_coins, coin_count)
                return
                #return min(min_coins, coin_count)

            coins_diff = min_coins - coin_count

            for i in range(start_coin, len_coins): # largest to smallest coins
                if coins[i] <= amt:
                    max_amt_poss = coins[i] * coins_diff

                    #if coins[i] <= amt < max_amt_poss:
                    if amt < max_amt_poss:
                        rec(i, coin_count + 1, amt - coins[i])

        len_coins = len(coins)
        min_coins = float('inf')

        # try biggest coins first
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
        print(f"\nres = {res}\n")


    sol = Solution() # DP tabulation w/ 1d table
    sol = Solution1b() # initialize within loop
    #sol = Solution1c() # loop through coins first, then amt

    #sol = Solution2() # recursion
    #sol = Solution3() # memoization via @functools.lru_cache(None)
    #sol = Solution4() # memoization
    
    #sol = Solution5() # BFS
    
    #sol = Solution6() # branch and bound v1

    sol = Solution7() # branch & bound v2; BEST solution
    
    #sol = Solution8() # branch and bound v3, slower

    import sys
    #recursion_limit = sys.getrecursionlimit() # I get 1000
    sys.setrecursionlimit(5000)

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

    comment = "LC test case; answer = 8"
    coins = [474,83,404,3]
    amount = 264
    test(coins, amount, comment)

    comment = "LC test case; answer = 20"
    coins = [186,419,83,408]
    amount = 6249
    test(coins, amount, comment)

    # only solution7 works
    # as well as solution6 with single modif for "if amt % coin == 0"
    # https://leetcode.com/problems/coin-change/discuss/114993
    comment = "answer = 123456"
    coins = [10]
    amount = 1234560
    test(coins, amount, comment)

    # only solution7 works
    # solution6 with single mod doesn't work...
    # https://leetcode.com/problems/coin-change/discuss/114993
    comment = " recursion limit; answer = 128254"
    coins = [26,12,75,53,7,9,25,3,96,44,39,79,20,61,57,95,89,10,62,73,94,59,52,87,40,78,28,37]
    amount = 12312312
    test(coins, amount, comment)
