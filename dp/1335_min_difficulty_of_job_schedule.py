"""
1335. Minimum Difficulty of a Job Schedule
Hard

You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the i-th job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done in that day.

Given an array of integers jobDifficulty and an integer d. The difficulty of the i-th job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.

Example 1:

Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7
Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7 

Example 2:

Input: jobDifficulty = [9,9,9], d = 4
Output: -1
Explanation: If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.

Example 3:

Input: jobDifficulty = [1,1,1], d = 3
Output: 3
Explanation: The schedule is one job per day. total difficulty will be 3.

Example 4:

Input: jobDifficulty = [7,1,7,1,7,1], d = 3
Output: 15

Example 5:

Input: jobDifficulty = [11,111,22,222,33,333,44,444], d = 6
Output: 843

Constraints:

1 <= jobDifficulty.length <= 300
0 <= jobDifficulty[i] <= 1000
1 <= d <= 10
"""

from typing import List

###############################################################################
"""
Solution 0: basic recursion, most naive version to show idea

How to partition n elts into d groups so sum of max in each group is minimum?
"""
class Solution0:
    #def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
    def minDifficulty(self, arr: List[int], d: int) -> int:
        def rec(arr, d):
            n = len(arr) # assume >= 1

            if n < d: # too few jobs to allocate to d days
                return -1
            if n == d: # one job per day
                return sum(arr)
            if d == 1: # all jobs on the same day
                return max(arr)

            # Now n > d.
            # Want to split n jobs into d days.

            min_diffic = float('inf')
            m = n - d + 1 # max number of jobs in one day
            # because the remaining (d-1) days can sitll have 1 job each.
            # n - (d-1)*1 = n -d + 1

            for i in range(1, m+1): # number of jobs to do today
                # For today, do jobs 0 to i-1, and recurse to find difficulty
                # for remaining jobs i, .., n with remaining d-1 days.
                diffic = max(arr[:i]) + rec(arr[i:], d - 1)

                min_diffic = min(min_diffic, diffic)
            
            return min_diffic
        
        return rec(arr, d)

###############################################################################
"""
Solution 1: basic recursion with some improvements.

Avoid some array copying (list slicing).
1 To get rid of slicing in "rec(arr[i:], d - 1)" within the loop, pass the 
start index "i" to the recursive function instead of a copied array.

2. To get rid of slicing in "max(arr[:i])", now "max(arr[start:i+1])", in the
loop, we can either cache these values or introduce another loop and index.
This is what memoization and tabulation would do, respectively.  Here, we
use a pre-calculated cache.

This still TLE's on LeetCode.
"""
class Solution:
    #def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
    def minDifficulty(self, arr: List[int], d: int) -> int:
        def rec(d, start=0):
            nonlocal maxes

            n = n_total - start # assume >= 1

            if n == d: # one job per day
                return sum(arr[start:])
            if d == 1: # all jobs on the same day
                #return max(arr[start:])
                return maxes[start, n_total-1]

            # Now n > d.
            # Want to split n jobs into d days.

            min_diffic = INF
            m = n - d + 1 # max number of jobs in one day

            for i in range(start, start + m):
                #diffic = max(arr[:i]) + rec(arr[i:], d - 1)
                #diffic = max(arr[start:i+1]) + rec(d - 1, i + 1)
                diffic = maxes[start, i] + rec(d - 1, i + 1)

                min_diffic = min(min_diffic, diffic)
            
            return min_diffic
        
        n_total = len(arr)
        if n_total < d: # too few jobs to allocate to d days
            return -1

        INF = float('inf')

        maxes = {} # maxes[i,j] is max of arr[i] to arr[j], inclusive
        for i in range(n_total):
            mx = arr[i]
            maxes[i, i] = mx

            for j in range(i+1, n_total):
                mx = max(mx, arr[j])
                maxes[i, j] = mx

        return rec(d)

###############################################################################
"""
Solution 2: memoization

Runtime: 1204 ms, faster than 44.30% of Python3 online submissions
Memory Usage: 61.5 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
    def minDifficulty(self, arr: List[int], d: int) -> int:
        def rec(d, start=0):
            nonlocal cache, sums, maxes
            if (d, start) in cache: return cache[d, start]

            n = n_total - start # assume >= 1

            if n == d: return sums[start] # one job per day
            if d == 1: return maxes[start, n_total-1] # all jobs on same day

            min_diffic = INF
            m = n - d + 1 # max number of jobs in one day

            for i in range(start, start + m):
                diffic = maxes[start, i] + rec(d - 1, i + 1)
                min_diffic = min(min_diffic, diffic)

            cache[d, start] = min_diffic
            return min_diffic

        n_total = len(arr)
        if n_total < d: return -1 # too few jobs to allocate to d days
        
        cache = {}
        INF = float('inf')
        
        s = 0
        sums = {} # sums[i] is sum from arr[i] to end of array
        for i in range(n_total-1, -1, -1):
            s += arr[i]
            sums[i] = s

        maxes = {} # maxes[i,j] is max of arr[i] to arr[j], inclusive
        for i in range(n_total):
            mx = arr[i]
            maxes[i, i] = mx

            for j in range(i+1, n_total):
                mx = max(mx, arr[j])
                maxes[i, j] = mx

        return rec(d)

###############################################################################
"""
Solution 3: with @functools.lru_cache

This is much faster and uses much less space than memoization.

Runtime: 776 ms, faster than 86.89% of Python3 online submissions
Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions

Use "if" instead of "max" and "min" 
and replacing start+m with end=start+n-d+1=n_total-d+1:
Runtime: 416 ms, faster than 97.82% of Python3 online submissions
"""
import functools

class Solution3:
    def minDifficulty(self, arr: List[int], d: int) -> int:
        
        @functools.lru_cache(None)
        def rec(d, start=0):
            n = n_total - start # assume >= 1

            #if n < d:  return -1 # too few jobs to allocate to d days
            if n == d: return sum(arr[start:]) # one job per day
            if d == 1: return max(arr[start:]) # all jobs on same day

            min_diffic = INF
            #m = n - d + 1 # max number of jobs in one day
            # note: start + m = start + (n - d + 1) = n_total - d + 1
            end = n_total - d + 1

            maxd = 0
            #for i in range(start, start + m):
            for i in range(start, end):
                maxd = max(maxd, arr[i])
                diffic = maxd + rec(d - 1, i + 1)
                min_diffic = min(min_diffic, diffic)

            return min_diffic

        n_total = len(arr)
        if n_total < d:  return -1 # too few jobs to allocate to d days
        
        INF = float('inf')

        return rec(d)

###############################################################################
"""
Solution 4: tabulation using 2d table.

Try to get rid of recursion in the memoization solution.  

We want to start with smaller values of d.
    Case d = 0 is impossible (no solutions).
    Case d = 1 is trivial (sum all relevant values).
    Case d = 2: decide how to split a list into two nonempty sublists.
    Cases d >= 3: decide the first sublist, then use a dp table to look up
    the solution for the rest of the list.

Our recursive function was rec(d, start=0), and was called using rec(d-1, i+1).
Convert rec(d-1, i+1) to a table lookup dp[days-1][end+1].  The state variables:

    days: the number of days left to allocate jobs for
    start: the start index of the array of jobs to start considering

Our recursive relation is:

    dp[days][start] = min( max(arr[start:end+1]) + dp[days-1][end+1] )
    for end=start..end, where end=start+(n-d+1)

Consider diffic = maxes[start, end] + dp[days-1][end+1].

Boundary cases: days=1 or days-1=0
    We want diffic to be just maxes[start, end].  So dp[0][end+1] should be 0.
    This is only for the whole array, so start=0 and end=n-1, so dp[0][n]=0.
    If it's not the whole array, then diffic=-1 (given by problem statement),
    but for calculation purposes with max, let it be float('inf').  
    So dp[0][i] = float('inf) for i=0..n-1.

O(dnn) time
O(dn) extra space

LeetCode: if using "max" and "min" instead of "if", lookup using "maxes" was faster 
than calculating it smartly within the loops, but used much more memory (but still 
much less than memoization).  In both cases, time was a little faster than using 
memoization, but used much less space.  

Runtime: 1024 ms, faster than 56.62% of Python3 online submissions
Memory Usage: 20.7 MB, less than 100.00% of Python3 online submissions

Precalculate "maxes" and use "if" instead of "max" and "min":
Runtime: 652 ms, faster than 93.71% of Python3 online submissions
Memory Usage: 20.7 MB, less than 100.00% of Python3 online submissions

Dont precalculate "maxes" and use "if" instead of "max" and "min":
Runtime: 464 ms, faster than 97.12% of Python3 online 
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions
"""
class Solution4:
    def minDifficulty(self, arr: List[int], d: int) -> int:        
        n = len(arr)
        INF = float('inf')
        dp = [[INF]*n + [0] for _ in range(d+1)] # dp[days][start]

        ### precalculate maxes
        maxes = {} # maxes[i,j] is max of arr[i] to arr[j], inclusive
        for i in range(n):
            mx = arr[i]
            maxes[i, i] = mx

            for j in range(i+1, n):
                mx = max(mx, arr[j])
                maxes[i, j] = mx

        for days in range(1, d+1):
            m = n - days + 1 # max number of jobs in one day
            
            for start in range(m): # was recursive parameter
                #maxd = 0
                min_diffic = INF

                for end in range(start, m): # was index i in recursion
                    #maxd = max(maxd, arr[end])
                    #diffic = maxd + dp[days-1][end+1]
                    
                    diffic = maxes[start, end] + dp[days-1][end+1]

                    #dp[days][start] = min(dp[days][start], diffic)
                    min_diffic = min(min_diffic, diffic)

                dp[days][start] = min_diffic

        #for row in dp: print(row)

        # d days left, starting with job 0
        return dp[d][0] if dp[d][0] < INF else -1

###############################################################################
"""
Solution 5: tabulation using 1d table.

Recurrence relation from tabulation for 2d table:
dp[days][start] = maxes[start, end] + dp[days-1][end+1]

Note that row "days" for dp table only depended on the previous row.

O(dnn) time as for tabulation using 2d table, but uses less space:
O(n) extra space

Runtime: 928 ms, faster than 67.76% of Python3 online submissions
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions

Using "if" instead of "max" and "min":
Runtime: 384 ms, faster than 97.90% of Python3 online submissions
"""
class Solution5:
    def minDifficulty(self, arr: List[int], d: int) -> int:
        n = len(arr)
        if n < d: return -1
        INF = float('inf')

        dp = [INF]*n + [0] # for days = 0

        for days in range(1, d+1):
            m = n - days + 1 # max number of jobs in one day
            
            for start in range(m):
                maxd = 0
                min_diffic = INF

                for end in range(start, m):
                    maxd = max(maxd, arr[end])
                    min_diffic = min(min_diffic, maxd + dp[end+1])

                dp[start] = min_diffic

        return dp[0]

###############################################################################
"""
Solution 6: use contiguous partitions of given list into d sublists.
"""
class Solution6:
    def partitions_contig(self, n):
        if n == 1: return [[[0]]]
    
        parts = self.partitions_contig(n-1)
        new_parts = []
        # new element is n-1

        for p in parts: # eg, [[0,1],[1,2]]
            # add single-element list [n-1] to all sublists in "parts"
            new_parts.append(p + [[n-1]])

            new_p = []
            for s in p: # look for the sublist that contains n-2
                if n-2 in s: # eg, s = [0,1,2] when n = 4
                    # want to create copy of p such that s has n-1 appended
                    new_p.append(s + [n-1])
                else:    
                    new_p.append(s)
                
            new_parts.append(new_p)
        
        return new_parts

    def minDifficulty(self, arr: List[int], d: int) -> int:       
        n = len(arr)

        # Want to generate all partitions of arr into d subsets.
        parts = [p for p in self.partitions_contig(n) if len(p)==d]
        #print(parts)
        min_diffic = float('inf')
        
        for p in parts:
            diffic = 0
            for s in p: # eg, [0,1,2]
                diffic += max(arr[i] for i in s)
            
            if diffic < min_diffic:
                min_diffic = diffic

        return min_diffic if min_diffic < float('inf') else -1

###############################################################################
"""
Solution 7: use DP + monotone stack

dp[i] table holds increasing values

stack


O(dn) time
O(n) extra space

https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/discuss/495000/C%2B%2B-0ms!-O(d*n)-time-O(n)-space.-DP-%2B-MonotonicMinimum-Stack

Runtime: 48 ms, faster than 100.00% of Python3 online submissions
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions
"""
class Solution7:
    def minDifficulty(self, arr: List[int], d: int) -> int:      
        n = len(arr)
        if n < d: return -1
        
        # for 
        dp = [0]*n
        dp[0] = arr[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1], arr[i]) # max so far up to index i
        print(f"dp = {dp}")

        # day = 1:
        for day in range(1, d):
            stack = [] # holds tuples (imax_d, min_d)
            t = dp[day-1] # max up to previous day
            print("="*80)
            print(f"day = {day}")

            for j in range(day, n):
                m = t # max up to previous day
                t = dp[j] # max up to current day (j)
                print("\n=====")
                print(f"j = {j}, arr[j] = {arr[j]}, m = {m}, t = {t}")

                # Found a higher diffic job, so pop all the jobs with
                # lower difficulty.
                # while max diffic of job on top of stack <= curr diffic
                while stack and arr[stack[-1][0]] <= arr[j]:
                    m = min(m, stack[-1][1])
                    print(f"pop {stack[-1]}")
                    stack.pop()
                    

                if stack:
                    # take min diffic b/w (1) taking all jobs up to local
                    # max this segment ??? and (2) all prev jobs in one day
                    # and today's job in the next day
                    dp[j] = min(dp[stack[-1][0]], m + arr[j])
                else:
                    dp[j] = m + arr[j] # add prev max and current value

                # j = index of max complexity job this segment
                # m = local min this segment
                stack.append((j, m))
                print(f"push ({j}, {m})")
                print(f"stack = {stack}")
                print(f"\ndp = {dp}")

        return dp[-1]

###############################################################################

if __name__ == "__main__":
    def test(arr, d, comment=None):
        min_diffic = s.minDifficulty(arr, d)
        
        print("="*80)
        if comment:
            print(comment)
            
        print(f"\n{arr}")
        print(f"d = {d}")
        print(f"\nmin difficulty = {min_diffic}")

    #s = Solution0() # basic recursion
    #s = Solution() # basic recursion
    #s = Solution2() # memoization
    #s = Solution3() # use @functool.lru_cache
    #s = Solution4() # tabulation using 2d table
    #s = Solution5() # tabulation using 1d table
    #s = Solution6() # partitions using contiguous sublists
    s = Solution7() # use DP + monotonic/minimum stack

    # comment = "LC ex1; answer = 7"    
    # arr = [6,5,4,3,2,1]
    # d = 2
    # test(arr, d, comment)

    # comment = "LC ex2; answer = -1"
    # arr = [9,9,9]
    # d = 4
    # test(arr, d, comment)

    # comment = "LC ex3; answer = 3"
    # arr = [1,1,1]
    # d = 3
    # test(arr, d, comment)
    
    # comment = "LC ex4; answer = 15"
    # arr = [7,1,7,1,7,1]
    # d = 3
    # test(arr, d, comment)
    
    comment = "LC ex5; answer = 843"
    arr = [11,111,22,222,33,333,44,444]
    d = 6
    test(arr, d, comment)

    # comment = "LC test case; TLE's basic recursion; answer = 3807"
    # arr = [380,302,102,681,863,676,243,671,651,612,162,561,394,856,601,30,6,257,921,405,716,126,158,476,889,699,668,930,139,164,641,801,480,756,797,915,275,709,161,358,461,938,914,557,121,964,315]
    # d = 10
    # test(arr, d, comment)

