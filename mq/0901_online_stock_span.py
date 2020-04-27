"""
901. Online Stock Span
Medium

Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].

Example 1:

Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]

Output: [null,1,1,1,2,1,4,6]

Explanation: 
First, S = StockSpanner() is initialized.  Then:
S.next(100) is called and returns 1,
S.next(80) is called and returns 1,
S.next(60) is called and returns 1,
S.next(70) is called and returns 2,
S.next(60) is called and returns 1,
S.next(75) is called and returns 4,
S.next(85) is called and returns 6.

Note that (for example) S.next(75) returned 4, because the last 4 prices
(including today's price of 75) were less than or equal to today's price.

Note:

Calls to StockSpanner.next(int price) will have 1 <= price <= 10^5.
There will be at most 10000 calls to StockSpanner.next per test case.
There will be at most 150000 calls to StockSpanner.next across all test cases.
The total time limit for this problem has been reduced by 75% for C++, and 50% for all other languages.
"""

###############################################################################
"""
Solution 1: use decreasing stack of (price, weight), where weight is equal
to total pops (recursive in a way) + 1.

O(1) time amortized, O(n) worst case
O(n) extra space - for stack

Each price is pushed to the stack once, and popped at most once.  If we have
seen n prices so far, then there have been 2n total pushes and pops.
"""
class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        total_pops = 1 # is actually 1 + total number of pops

        while self.stack and price >= self.stack[-1][0]:
            _, pops = self.stack.pop()
            total_pops += pops
        
        self.stack.append((price, total_pops))

        return total_pops 

###############################################################################
"""
Solution 2: use decreasing stack, where elements in stack are indices
but it's their corresponding prices that are decreasing.  The class keeps
track of the current index.

After popping from the stack as needed, the last time the stock was at a 
higher value will be at the top of the stack.  So we can just take the
difference of indices to find the answer.

This is useful if we also want to track the price history of the stock.

https://leetcode.com/problems/online-stock-span/discuss/397583/Universal-idea-for-a-series-of-problems
"""
class StockSpanner2:
    def __init__(self):
        self.prices = []
        self.stack = []
        self.i = 0 # index/counter of prices; same as len(self.prices) - 1

    def next(self, price: int) -> int:
        self.prices.append(price)

        while self.stack and self.prices[self.stack[-1]] <= price:
            self.stack.pop()

        if not self.stack:
            val = self.i + 1
        else:
            val = self.i - self.stack[-1]

        self.stack.append(self.i)
        self.i += 1
        
        return val 

###############################################################################
"""
Solution 3: use decreasing stack of tuple (price, index).  The decreasing
property is with respect to prices only.  The class also tracks the index.
"""
class StockSpanner3:
    def __init__(self):
        self.stack = []
        self.i = 0 # index/counter of prices; same as len(self.prices) - 1

    def next(self, price: int) -> int:
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()

        if not self.stack:
            val = self.i + 1
        else:
            val = self.i - self.stack[-1][1]

        self.stack.append((price, self.i))
        self.i += 1
        
        return val 
    
###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        s = StockSpanner()
        #s = StockSpanner2()
        #s = StockSpanner3()

        res = []

        for price in arr:
            res += [s.next(price)]

        print("="*80)
        if comment:
            print(comment)
            
        print(f"\n{arr}")
        print(f"\nresult = {res}")


    comment = "LC ex1; answer = [1, 1, 1, 2, 1, 4, 6]"    
    arr = [100, 80, 60, 70, 60, 75, 85]
    test(arr, comment)

    comment = "LC test case; answer = [1, 2, 1, 2, 1]"
    arr = [29, 91, 62, 76, 51]
    test(arr, comment)

    comment = "trivial case"
    arr = [0]
    test(arr, comment)

    comment = "Constant prices"
    arr = [6,6,6,6,6,6]
    test(arr, comment)
