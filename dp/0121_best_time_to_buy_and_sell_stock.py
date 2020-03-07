"""
121. Best Time to Buy and Sell Stock
Easy

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

from typing import List

###############################################################################
"""
Solution 1: keep track of low price so far, and max profit so far.

O(n) time
O(1) extra space
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = 0
        low = float('inf')

        for p in prices:
            if p < low:
                low = p
            elif p - low > mx:
                mx = p - low

        return mx

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\ns = {arr}")
        
        res = sol.maxProfit(arr)

        print(f"\nres = {res}\n")
        

    sol = Solution()

    comment = "LC ex1; answer = 5"
    arr = [7,1,5,3,6,4]
    test(arr, comment)

    comment = "LC ex2; answer = 0"
    arr = [7,6,4,3,1]
    test(arr, comment)
