"""
1449. Form Largest Integer With Digits That Add up to Target
Hard

Given an array of integers cost and an integer target. Return the maximum integer you can paint under the following rules:

The cost of painting a digit (i+1) is given by cost[i] (0 indexed).
The total cost used must be equal to target.
Integer does not have digits 0.
Since the answer may be too large, return it as string.

If there is no way to paint any integer given the condition, return "0".

Example 1:

Input: cost = [4,3,2,5,6,7,2,5,5], target = 9
Output: "7772"

Explanation:  The cost to paint the digit '7' is 2, and the digit '2' is 3. Then cost("7772") = 2*3+ 3*1 = 9. You could also paint "997", but "7772" is the largest number.
Digit    cost
  1  ->   4
  2  ->   3
  3  ->   2
  4  ->   5
  5  ->   6
  6  ->   7
  7  ->   2
  8  ->   5
  9  ->   5

Example 2:

Input: cost = [7,6,5,5,5,6,8,7,8], target = 12
Output: "85"
Explanation: The cost to paint the digit '8' is 7, and the digit '5' is 5. Then cost("85") = 7 + 5 = 12.

Example 3:

Input: cost = [2,4,6,2,4,6,4,4,4], target = 5
Output: "0"
Explanation: It's not possible to paint any integer with total cost equal to target.

Example 4:

Input: cost = [6,10,15,40,40,40,40,40,40], target = 47
Output: "32211"

Constraints:

cost.length == 9
1 <= cost[i] <= 5000
1 <= target <= 5000
"""

from typing import List

###############################################################################
"""
Solution: DP memo.

Q: why do we need neg_inf ?

"""
import functools
class Solution1b:
    def largestNumber(self, cost: List[int], target: int) -> str:
        @functools.lru_cache(None)
        def rec(t):
            if t == 0:
                return 0

            mx = neg_inf

            for i, c in enumerate(cost): # digit = i + 1
                if c <= t:
                    mx = max(mx, rec(t - c) * 10 + i + 1)

            return mx

        neg_inf = float('-inf') # -1 also works

        res = rec(target)

        if res == neg_inf:
            return "0"

        return str(res)

"""
Solution 1b: same, but optimize by converting cost array to dict that maps
costs to digits.

If two digits share the same cost, only the larger digit is used.

"""
import functools
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        @functools.lru_cache(None)
        def rec(t):
            if t == 0:
                return 0

            mx = neg_inf

            for c, digit in d.items():
                if c <= t:
                    mx = max(mx, rec(t - c) * 10 + digit)

            return mx

        neg_inf = float('-inf') # -1 also works

        d = {c: i+1 for i, c in enumerate(cost)}

        res = rec(target)

        if res == neg_inf:
            return "0"

        return str(res)

###############################################################################
"""
Solution 2: DP tabulation...

O() time
O(target) extra space
"""
class Solution2:
    def largestNumber(self, cost: List[int], target: int) -> str:
        neg_inf = float('-inf') # -1 also works
        dp = [0] + [neg_inf] * (target)

        for t in range(1, target + 1):
            mx = neg_inf

            for i, c in enumerate(cost): # digit = i + 1
                if c <= t:
                    mx = max(mx, dp[t - c] * 10 + i + 1)

            dp[t] = mx

        if dp[target] == neg_inf:
            return "0"

        return str(dp[target])

"""
Solution 2b: same, but optimize by converting cost array to dict that maps
costs to digits.

If two digits share the same cost, only the larger digit is used.

"""
class Solution2b:
    def largestNumber(self, cost: List[int], target: int) -> str:
        neg_inf = float('-inf') # -1 also works
        dp = [0] + [neg_inf] * (target)

        d = {c: i+1 for i, c in enumerate(cost)}

        for t in range(1, target + 1):
            mx = neg_inf

            for c in d: # c = cost of digit d[c]
                if c <= t:
                    mx = max(mx, dp[t - c] * 10 + d[c])

            dp[t] = mx

        if dp[target] == neg_inf:
            return "0"

        return str(dp[target])

"""
Why do we always insert the new digit at the end?

Hard to explain.. Because we already add the biggest digits.

Because the previous number to be multiplied by 10 is already the maximum 
that you can get, which means the next digit cannot be greater than any digit
of the previous dp[t-c]

"""

"""
LC ex1
cost = [4,3,2,5,6,7,2,5,5]
target = 9

costs are c = 2, 3, 4, 5, 6, 7

7 has cost 2
2 has cost 3

answer = 7772

initial dp =
0  1  2  3  4  5  6  7  8  9
0 -1 -1 -1 -1 -1 -1 -1 -1 -1

t = 1
t - c = 1 - c <= -1 since c >= 2
c >= 2 so t - c

...

"""

###############################################################################
"""
Solution 3: DP tabulation. Don't assume Python's infinite length integers.

1. Use DP tabulation to find max number of digits needed to achieve target.

2. If no combo of digits can achieve target, return "0". (ie, if dp[target] < 0)

3. Construct the max integer that achieves the target by greedily choosing the
largest digit that if picked, leaves the most number of digits remaining to 
choose from.

Based on Q4 solutions here:
https://leetcode.com/contest/biweekly-contest-26/ranking/

O() time
O(target) extra space: for dp table
O() extra space: for string to return

"""
class Solution3:
    def largestNumber(self, cost: List[int], target: int) -> str:
        neg_inf = float('-inf')
        dp = [0] + [neg_inf] * target

        """
        1. First, use DP tabulation to find max number of digits needed to 
        achieve target.
        """
        for t in range(1, target + 1):
            mx = neg_inf

            for c in cost: # don't care what the actual digit is
                if c <= t:
                    #dp[t] = max(dp[t], dp[t - c] + 1)
                    mx = max(mx, dp[t - c] + 1)

            dp[t] = mx

        #print(dp)

        """ 
        2. If no combo of digits can achieve target, return "0".
        """
        if dp[target] < 0:
            return "0"
        
        """
        3. Now we know how many digits to use: dp[target].
        Construct the max number by greedily choosing the largest digit that if
        picked, leaves the most number of digits remaining to choose from.
        """
        res = ""

        while target > 0:
            for digit in range(9, 0, -1):
                c = cost[digit - 1]

                # Since we are picking exactly one digit, we know the following
                # equality has to hold.
                if c <= target and dp[target - c] == dp[target] - 1:
                    res += str(digit)
                    target -= c
                    break
            
        return res

"""
Solution 3b: same, but optimize by converting cost array to dict that maps
costs to digits.

If two digits share the same cost, only the larger digit is used.

"""
class Solution3b:
    def largestNumber(self, cost: List[int], target: int) -> str:
        neg_inf = float('-inf')
        dp = [0] + [neg_inf] * target

        d = {c: i+1 for i, c in enumerate(cost)}
        digits = sorted(d.values(), reverse=True) # for use in part 3

        """
        1. First, use DP tabulation to find max number of digits needed to 
        achieve target.
        """
        for t in range(1, target + 1):
            mx = neg_inf

            for c in d: # c = cost of digit d[c]; don't care what the actual digit is
                if c <= t:
                    #dp[t] = max(dp[t], dp[t - c] + 1)
                    mx = max(mx, dp[t - c] + 1)

            dp[t] = mx

        #print(dp)

        """ 
        2. If no combo of digits can achieve target, return "0".
        """
        if dp[target] < 0:
            return "0"
        
        """
        3. Now we know how many digits to use: dp[target].
        Construct the max number by greedily choosing the largest digit that if
        picked, leaves the most number of digits remaining to choose from.
        """
        res = ""

        while target > 0:
            for digit in digits: # in decreasing order
                c = cost[digit - 1]

                # Since we are picking exactly one digit, we know the following
                # equality has to hold.
                if c <= target and dp[target - c] == dp[target] - 1:
                    res += str(digit)
                    target -= c
                    break
            
        return res

###############################################################################

if __name__ == "__main__":
    def test(cost, target, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\ncost = {cost}")
        print(f"target = {target}")

        res = sol.largestNumber(cost, target)

        print(f"\nres = {res}\n")


    sol = Solution() # DP memo
    sol = Solution1b() # same, but use dict that maps costs to digits
    
    sol = Solution2() # DP tabulation
    sol = Solution2b() # same, but use dict that maps costs to digits

    sol = Solution3() # DP tabulation; don't assume Python's big integers
    sol = Solution3b() # same, but use dict that maps costs to digits

    comment = "LC ex1; answer = 7772"
    cost = [4,3,2,5,6,7,2,5,5]
    target = 9
    test(cost, target, comment)

    comment = "LC ex2; answer = 85"
    cost = [7,6,5,5,5,6,8,7,8]
    target = 12
    test(cost, target, comment)

    comment = "LC ex3; answer = 0"
    cost = [2,4,6,2,4,6,4,4,4]
    target = 5
    test(cost, target, comment)

    comment = "LC ex4; answer = 32211"
    cost = [6,10,15,40,40,40,40,40,40]
    target = 47
    test(cost, target, comment)
    
    comment = "LC TC; answer = 9,333,333"
    cost = [5,4,4,5,5,5,5,5,5]
    target = 29
    test(cost, target, comment)

    comment = "LC TC; answer = 77666666666666111111"
    cost = [37,73,100,81,51,35,48,64,97]
    target = 738
    test(cost, target, comment)

    comment = "LC TC; answer = 99977777777777777777776 ?"
    cost = [70,84,55,63,74,44,27,76,34]
    target = 659
    test(cost, target, comment)

    comment = "LC TC; answer = (many 6's and then one 5)"
    cost = [2,4,2,5,3,2,5,5,4]
    target = 739
    test(cost, target, comment)
