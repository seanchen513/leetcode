"""
983. Minimum Cost For Tickets
Medium

In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.

Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11

Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total you spent $11 and covered all the days of your travel.

Example 2:

Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17

Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total you spent $17 and covered all the days of your travel.

Note:

1 <= days.length <= 365
1 <= days[i] <= 365
days is in strictly increasing order.
costs.length == 3
1 <= costs[i] <= 1000
"""

from typing import List
import collections

###############################################################################
"""
Solution 1: recursion w/ memoization, recursing on calendar days, starting from
first travel day.  Equivalent to iterating backwards for tabulation.

Recursion returns min cost to travel starting from given day.

See Approach 1 here:
https://leetcode.com/problems/minimum-cost-for-tickets/solution/

O(n) time, where n = number of calendar days.
O(n) extra space: for recursion and set(days).

Runtime: 28 ms, faster than 99.07% of Python3 online submissions
Memory Usage: 13.6 MB, less than 7.14% of Python3 online submissions
"""
import functools
class Solution:
    def mincostTickets(self, days, costs):
        dayset = set(days)
        cost1, cost7, cost30 = costs # costs of 1-, 7-, and 30-day passes
        #durations = [1, 7, 30]
        last_day = days[-1]
        
        @functools.lru_cache(None)
        def rec(day): # min cost to travel starting from given day
            if day > last_day:
                return 0
            elif day in dayset:
                return min(
                    rec(day + 1) + cost1,
                    rec(day + 7) + cost7,
                    rec(day + 30) + cost30)
                #return min(rec(day + d) + c
                #    for c, d in zip(costs, durations))
                
            else:
                return rec(day + 1)

        return rec(days[0])

"""
Solution 1b: same as sol #1, but recurse in the other direction.
"""
import functools
class Solution1b:
    def mincostTickets(self, days, costs):
        dayset = set(days)
        cost1, cost7, cost30 = costs
        #durations = [1, 7, 30]

        @functools.lru_cache(None)
        def rec(day): # min cost to travel ending on given day
            if day < 1:
                return 0
            elif day in dayset:
                return min(
                    rec(day - 1) + cost1,
                    rec(day - 7) + cost7,
                    rec(day - 30) + cost30)
                #return min(rec(day - d) + c
                #    for c, d in zip(costs, durations))
                
            else:
                return rec(day - 1)

        return rec(days[-1]) # start from last travel day

###############################################################################
"""
Solution 2: recursion w/ memoization, recursing on travel days (indices), 
starting from first travel day.

Recursion returns min cost to travel starting from given day.

See Approach 2 here:
https://leetcode.com/problems/minimum-cost-for-tickets/solution/

This seems to be same idea:
https://leetcode.com/problems/minimum-cost-for-tickets/discuss/227321/Top-down-DP-Logical-Thinking
"""
import functools
class Solution2:
    def mincostTickets(self, days, costs):
        n = len(days)
        cost1, cost7, cost30 = costs

        @functools.lru_cache(None)
        def rec(d): # return min cost starting from days[d]
            if d >= n: # d = index for (travel) days input list
                return 0

            today = days[d]            
            #ans = float('inf')
            
            # Find largest index j such that...
            # Ie, find next travel day (index) if bought a pass today.
            # Ie, skip all the travel days that can be covered by a 
            # pass bought today.
            j = d
            while j < n and days[j] < today + 1:
                j += 1
            j1 = j
            #ans = min(ans, rec(j) + cost1)

            # Continue with same j for 7-day pass
            while j < n and days[j] < today + 7:
                j += 1
            j7 = j
            #ans = min(ans, rec(j) + cost7)
            
            # Continue with same j for 30-day pass
            while j < n and days[j] < today + 30:
                j += 1
            #j30 = j
            #ans = min(ans, rec(j) + cost30)

            #print(f"j1,j7,j30 = {j1},{j7},{j}")
            return min(rec(j1) + cost1, rec(j7) + cost7, rec(j) + cost30)
            #return ans

        return rec(0) # start with first travel day index

"""
Solution 2b: same as sol #2, but recurse in the other direction.

Runtime: 40 ms, faster than 71.99% of Python3 online submissions
Memory Usage: 13.2 MB, less than 42.86% of Python3 online submissions
"""
import functools
class Solution2b:
    def mincostTickets(self, days, costs):
        cost1, cost7, cost30 = costs

        @functools.lru_cache(None)
        def rec(d): # return min cost ending on days[d]
            if d < 0: # d = index for (travel) days input list
                return 0
            
            today = days[d]
            ans = float('inf')
            
            # Find smallest index j such that...
            # Ie, skip all the days that can be covered by a pass bought
            # on day days[j] for final j.
            j = d
            while j >= 0 and days[j] > today - 1:
                j -= 1
            ans = min(ans, rec(j) + cost1)

            # Continue with same j for 7-day pass
            while j >= 0 and days[j] > today - 7:
                j -= 1
            ans = min(ans, rec(j) + cost7)
            
            # Continue with same j fpr 30-day pass
            while j >= 0 and days[j] > today - 30:
                j -= 1
            ans = min(ans, rec(j) + cost30)

            return ans

        return rec(len(days)-1) # start with last travel day index

"""
Solution 2c: same as sol #2, but extract out function next_travel_days(d).
"""
import functools
class Solution2c:
    def mincostTickets(self, days, costs):
        n = len(days)
        cost1, cost7, cost30 = costs

        @functools.lru_cache(None)
        def next_travel_days(d):
            today = days[d]
            j = d

            while j < n and days[j] < today + 1:
                j += 1
            j1 = j

            # Continue with same j for 7-day pass
            while j < n and days[j] < today + 7:
                j += 1
            j7 = j
            
            # Continue with same j for 30-day pass
            while j < n and days[j] < today + 30:
                j += 1

            return j1, j7, j

        @functools.lru_cache(None)
        def rec(d): # return min cost starting from days[d]
            if d >= n: # d = index for (travel) days input list
                return 0
            
            j1, j7, j30 = next_travel_days(d)

            #print(f"j1,j7,j30 = {j1},{j7},{j}")
            return min(rec(j1) + cost1, rec(j7) + cost7, rec(j30) + cost30)
            #return ans

        return rec(0) # start with first travel day index

"""
Solution 2d: same as sol #2, but precalculate next_travel_days[].
"""
import functools
class Solution2d:
    def mincostTickets(self, days, costs):
        n = len(days)
        cost1, cost7, cost30 = costs

        next_travel_days = []
        for d in range(n):
            today = days[d]
            j = d

            while j < n and days[j] < today + 1:
                j += 1
            j1 = j

            # Continue with same j for 7-day pass
            while j < n and days[j] < today + 7:
                j += 1
            j7 = j
            
            # Continue with same j for 30-day pass
            while j < n and days[j] < today + 30:
                j += 1

            next_travel_days.append((j1, j7, j))

        @functools.lru_cache(None)
        def rec(d): # return min cost starting from days[d]
            if d >= n: # d = index for (travel) days input list
                return 0
            
            j1, j7, j30 = next_travel_days[d]

            #print(f"j1,j7,j30 = {j1},{j7},{j}")
            return min(rec(j1) + cost1, rec(j7) + cost7, rec(j30) + cost30)
            #return ans

        return rec(0) # start with first travel day index


###############################################################################
"""
Solution 3: tabulation, iterating forward on calendar days.

Can move backward instead; just change the indexing; eg, return dp[1].  See:

https://leetcode.com/problems/minimum-cost-for-tickets/discuss/472937/A-comparison-between-the-forward-and-backward-approach

dp[i] = total cost to travel up to day i, where i = 1, ..., 365.
dp[0] = 0 is dummy value.

O(n) time, where n = number of days in a year.
O(n) extra space: for dp list and max size of day_set.

Runtime: 28 ms, faster than 99.07% of Python3 online submissions
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions
"""
class Solution3:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        day_set = set(days)
        cost1, cost7, cost30 = costs

        last_day = days[-1] + 1 # actually 1 past last day
        dp = [0] * last_day # 1st 0 is dummy value
        #dp = [0] * 366


        #for i in range(1, 366): # day index
        for i in range(1, last_day):
            if i in day_set:
                dp[i] = min(
                    dp[i-1] + cost1,
                    dp[max(i-7, 0)] + cost7, # use max() to keep index valid
                    dp[max(i-30, 0)] + cost30
                )
            else:
                dp[i] = dp[i-1]

        return dp[-1]

"""
Solution 3b: same as sol #3b, but optimized.

(1) Only track calendar days from first to last travel date,
ie, days[0] to days[-1].  This means the size and indexing of the
dp list changes.
(2) In the original solution, we only looked back 1, 7, or 30 days,
so we only need to keep track of dp values for the last 30 calendar days.

O(n) time, where n = number of calendar days.
O(n) extra space: for max size of day_set (but dp size is smaller now).

https://leetcode.com/problems/minimum-cost-for-tickets/discuss/226659/Two-DP-solutions-with-pictures

Runtime: 32 ms, faster than 96.38% of Python3 online submissions
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions
"""
class Solution3b:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        day_set = set(days)
        cost1, cost7, cost30 = costs

        dp = [0]*30 # rolling 30 days using mod

        for i in range(days[0], days[-1] + 1): # day index
            if i in day_set:
                dp[i % 30] = min(
                    dp[(i-1) % 30] + cost1,
                    dp[max(i-7, 0) % 30] + cost7, # use max() to keep index valid
                    dp[max(i-30, 0) % 30] + cost30
                )
            else:
                dp[i % 30] = dp[(i-1) % 30]

        return dp[days[-1] % 30]

###############################################################################
"""
Solution 4: track min cost for each travel day.

Process only travel days and store (day i, min cost to travel up to day i).
Keep queues that store info only for the last 7 and 30 days.

https://leetcode.com/problems/minimum-cost-for-tickets/discuss/226659/Two-DP-solutions-with-pictures

O(n) time, where n = number of travel days
O(38) extra space, where 38 = 1 + 7 + 30

Runtime: 32 ms, faster than 96.38% of Python3 online submissions
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions
"""
class Solution4:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cost1, cost7, cost30 = costs
        
        last7 = collections.deque([])
        last30 = collections.deque([])
        cost = 0

        for d in days:
            # Remove older elements from the queues.
            while last7 and last7[0][0] + 7 <= d:
                last7.popleft()

            while last30 and last30[0][0] + 30 <= d: 
                last30.popleft()

            # Add to the queues: (today, min cost to travel up to today)
            last7.append( (d, cost + cost7) )
            last30.append( (d, cost + cost30) )

            # calculate min cost to travel up to today (day d)
            cost = min(
                cost + cost1, # previous cost + buy 1-day ticket for today
                last7[0][1], # still using 7-day ticket (earliest possible)
                last30[0][1] # still using 30-day ticket (earliest possible)
            )

        return cost

###############################################################################

if __name__ == "__main__":
    def test(days, costs, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(f"\ndays = {days}")
        print(f"costs = {costs}")
        
        res = sol.mincostTickets(days, costs)
        print(f"\nres = {res}")


    sol = Solution() # memo, recurse on cal days, start from 1st travel day
    sol = Solution1b() # memo, recurse on cal days, start from last travel day
    
    sol = Solution2() # memo, recurse on travel day index, starting from 1st day
    #sol = Solution2b() # memo, recurse on travel day index, starting from last day
    sol = Solution2c() # same as sol #2, but extract out function next_travel_days(d).
    sol = Solution2d() # same as sol #2, but precalculate next_travel_days[]

    #sol = Solution3() # tabulation, going forward
    #sol = Solution3b() # ... optimized
    #sol = Solution4() # track min cost for travel days, use last7 and last30 queues

    comment = "LC ex1; answer = 11"
    days = [1,4,6,7,8,20]
    costs = [2,7,15]
    test(days, costs, comment)

    comment = "LC ex2; answer = 17"
    days = [1,2,3,4,5,6,7,8,9,10,30,31]
    costs = [2,7,15]
    test(days, costs, comment)

    comment = "LC test case; answer = 6"
    days = [1,4,6,7,8,20]
    costs = [7,2,15]
    test(days, costs, comment)

    comment = "LC test case; answer = 50"
    days = [1,2,3,4,6,8,9,10,13,14,16,17,19,21,24,26,27,28,29]
    costs = [3,14,50]
    test(days, costs, comment)

    comment = "LC test case; TLE danger; answer = 245"
    days = [1,2,4,5,6,8,9,10,11,12,14,15,16,18,19,21,22,25,28,29,30,31,35,36,37,38,39,40,41,42,44,45,47,48,50,52,54,56,59,60,62,63,64,67,68,69,70,72,74,76,77,79,80,82,83,84,86,87,91,95,96,98]
    costs = [5,20,86]
    test(days, costs, comment)

    comment = "LC test case; TLE danger; answer = 423"
    days = [1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,24,25,27,28,29,30,31,34,37,38,39,41,43,44,45,47,48,49,54,57,60,62,63,66,69,70,72,74,76,78,80,81,82,83,84,85,88,89,91,93,94,97,99]
    costs = [9,38,134]
    test(days, costs, comment)
    
    comment = "LC test case; TLE danger; answer = 3040"
    days = [6,9,10,14,15,16,17,18,20,22,23,24,29,30,31,33,35,37,38,40,41,46,47,51,54,57,59,65,70,76,77,81,85,87,90,91,93,94,95,97,98,100,103,104,105,106,107,111,112,113,114,116,117,118,120,124,128,129,135,137,139,145,146,151,152,153,157,165,166,173,174,179,181,182,185,187,188,190,191,192,195,196,204,205,206,208,210,214,218,219,221,225,229,231,233,235,239,240,245,247,249,251,252,258,261,263,268,270,273,274,275,276,280,283,285,286,288,289,290,291,292,293,296,298,299,301,303,307,313,314,319,323,325,327,329,334,339,340,341,342,344,346,349,352,354,355,356,357,358,359,363,364]
    costs = [21,115,345]
    test(days, costs, comment)
