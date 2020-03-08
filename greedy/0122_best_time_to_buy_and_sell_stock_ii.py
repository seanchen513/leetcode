"""
122. Best Time to Buy and Sell Stock II
Easy

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.

Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

from typing import List

###############################################################################
"""
Solution 1: Add up all price increases.

O(n) time
O(1) extra space
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0

        for i in range(1, n):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]

            #profit += max(0, prices[i] - prices[i-1])

        return profit

class Solution1b:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(prices[i+1] - prices[i], 0) for i in range(len(prices) - 1))

class Solution1c:
    def maxProfit(self, prices: List[int]) -> int:
        return sum([b - a for a, b in zip(prices, prices[1:]) if b - a > 0])

###############################################################################
"""
Solution 2: greedy approach.  Buy at valleys, just before first increase.
Sell at peaks, just before first decrease or at end.

O(n) time
O(1) extra space
"""
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        end = len(prices) - 1
        profit = 0
        i = 0

        while i < end:
            # Buy just before first increase (virtual buy at end).
            while i < end and prices[i] >= prices[i+1]:
                i += 1

            buy_price = prices[i]

            # Sell just before first decrease or at end.
            while i < end and prices[i] <= prices[i+1]:
                i += 1
            
            profit += prices[i] - buy_price

        return profit

###############################################################################
"""
Solution 3: greedy approach.  Buy at every valley (other than end) and sell at
first peak after each buy.  Check if previous transaction was a buy.

If a valley is part of a plateau (eg, 6, 2, 2, 4), buy at the right-most
point of the plateau.  If a peak is part of a plateau (eg, 2, 4, 4, 1), sell
at the right-most point of the plateau.

O(n) time
O(1) extra space
"""
class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        profit = 0
        buy_price = None
        
        for i, p in enumerate(prices):
            # Buy 1st price if 2nd price is greater.
            if i == 0 and p < prices[i+1]:
                print(f"Buy for {p}")
                buy_price = p

            # Buy at end of valley if previous transaction was not a buy.
            if 0 < i < n-1 and p <= prices[i-1] and p < prices[i+1]:
                if buy_price == None:
                    print(f"Buy for {p}")
                    buy_price = p

            # Sell at end of peak if previous transaction was a buy.
            if (i > 0 and p >= prices[i-1]) and (i == n-1 or p > prices[i+1]):
                if buy_price != None: # could be 0
                    profit += p - buy_price
                    buy_price = None
                    print(f"Sell for {p}")

        return profit

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\ns = {arr}")
        
        res = sol.maxProfit(arr)

        print(f"\nres = {res}\n")
        

    sol = Solution() # add up price increases (every interval)
    #sol = Solution2() # buy at valleys, sell at peaks
    #sol = Solution3() # buy at valleys, sell at peaks

    comment = "LC ex1; answer = 7"
    arr = [7,1,5,3,6,4]
    test(arr, comment)

    comment = "LC ex2; answer = 4"
    arr = [1,2,3,4,5]
    test(arr, comment)

    comment = "LC ex2; answer = 0"
    arr = [7,6,4,3,1]
    test(arr, comment)

    comment = "LC test case; answer = 7"
    arr = [6,1,3,2,4,7]
    test(arr, comment)

    comment = "LC test case; answer = 0"
    arr = [1]
    test(arr, comment)

    comment = "LC test case; answer = 3"
    arr = [2,2,5]
    test(arr, comment)

    comment = "LC test case; answer = 20"
    arr = [5,2,3,2,6,6,2,9,1,0,7,4,5,0]
    test(arr, comment)

    comment = "LC test case; answer = 0"
    arr = [3,3]
    test(arr, comment)

    comment = "LC test case; answer = 8"
    arr = [0,5,5,6,2,1,1,3]
    test(arr, comment)

    comment = "LC test case; answer = 0"
    arr = []
    test(arr, comment)
    