"""
739. Daily Temperatures
Medium

Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
"""

from typing import List
import collections

###############################################################################
"""
Solution: use non-increasing (monotonic decreasing) stack.

LC example:
 0  1  2  3  4  5  6  7
73 74 75 71 69 72 76 73

        stack       stack
i   val before      after
0   73  []          [73]
1   74  [73]        [74]        pop 73
2   75  [74]        [75]        pop 74  
3   71  [75]        [75,71]
4   69  [75,71]     [75,71,69]
5   72  [75,71,69]  [75,72]     pop 69, 71
6   76  [75,72]     [76]        pop 72, 75
7   73  [76]        [76,73]

O(n) time
O(n) extra space: for output and stack

Runtime: 472 ms, faster than 95.21% of Python3 online submissions
Memory Usage: 17.6 MB, less than 7.89% of Python3 online submissions
"""
class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        n = len(temps)
        res = [0]*n

        stack = [] # mono decreasing stack

        for i, t in enumerate(temps):
            while stack and stack[-1][0] < t:
                _, k = stack.pop()
                res[k] = i - k

            stack.append((t, i))

        return res

"""
Solution 1b: same, but stack stores indices only and not values.

Runtime: 468 ms, faster than 97.42% of Python3 online submissions
Memory Usage: 17.2 MB, less than 23.68% of Python3 online submissions
"""
class Solution1b:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        n = len(temps)
        res = [0]*n

        stack = [] # mono decreasing stack

        for i, t in enumerate(temps):
            while stack and temps[stack[-1]] < t:
                k = stack.pop()
                res[k] = i - k

            stack.append(i)

        return res

###############################################################################
"""
Solution 2: process temps in reverse, and use strictly decreasing stack.

Notice that when we traverse the array in reverse, if we find an element
that is larger than a previous element (higher index), then we can
disregard the previous element for setting the answer for elements
yet to be visited.

LC example:
 0  1  2  3  4  5  6  7
73 74 75 71 69 72 76 73

Stack stores indices, but we show temperatures here.

        stack       stack
i   val before      after       
7   73  []          [73]        
6   76  [73]        [76]        pop 73
5   72  [76]        [76,72]                     
4   69  [76,72]     [76,72,69]
3   71  [76,72,69]  [76,72,71]  pop 69
2   75  [76,72,71]  [76,75]     pop 71,72
1   74  [76,75]     [76,75,74]
0   73  [76,75,74]  [76,75,74,73]

This is approach 2 here:
https://leetcode.com/problems/daily-temperatures/solution/

O(n) time
O(w) extra space, where w is the range in temperatures, since the stack
represents strictly decreasing temperatures.

Runtime: 468 ms, faster than 97.42% of Python3 online submissions
Memory Usage: 17.3 MB, less than 18.42% of Python3 online submissions
"""
class Solution2:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        n = len(temps)
        res = [0]*n

        stack = [] # strictly increasing stack

        #for i, x in enumerate(temps):
        for i in range(n-1, -1, -1):
            # Get rid of smaller temperatures already visited.
            while stack and temps[i] >= temps[stack[-1]]:
                stack.pop()

            if stack: # stack[-1] has greater temperature than current temp[i]
                res[i] = stack[-1] - i

            stack.append(i)

        return res

###############################################################################
"""
Solution 3: process array in reverse, and use "next" array that maps
temperature to next index with that temperature.

This is approach 1 here:
https://leetcode.com/problems/daily-temperatures/solution/

O(n*w) time, where w is the range in temperatures.
O(n + w) extra space: for output and "next" array
"""
class Solution3:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        n = len(temps)
        res = [0] * n

        inf = float('inf')
        next = [inf] * 102

        for i in range(n-1, -1, -1):
            t = temps[i]
            warmer_idx = min(next[t] for t in range(t+1, 102))
            
            if warmer_idx < inf:
                res[i] = warmer_idx - i

            next[t] = i

        return res

###############################################################################
"""
Solution #4: use dict that maps temp to indices.

Temperatures in range [30, 100].  So at most 71 keys.
Use dict that maps each of these temperatures to a list of the days on which
they occured.  For each day, check the dict for all lower temperatures in the
past and calculate the difference in number of days.  Remove these entries
from the dict, so they aren't checked again in the future.

LC example:
 0  1  2  3  4  5  6  7
73 74 75 71 69 72 76 73

69: 4
71: 3
72: 5
73: 0, 7
74: 1
75: 2
76: 6

O(n*w) time, where w is range in temperatures
O(n) extra space: for output and dict

Runtime: 988 ms, faster than 11.51% of Python3 online submissions
Memory Usage: 17.2 MB, less than 21.05% of Python3 online submissions
"""
class Solution4:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        n = len(temps)
        res = [0]*n

        d = collections.defaultdict(list)

        for i, t in enumerate(temps):            
            # check all lower temperatures (in the past)
            for temp in range(30, t):
                if temp in d:
                    for day in d[temp]: # past days that had this temp < t
                        res[day] = i - day

                    # remove all these days since their answers have now been
                    # calculated, and we don't want to deal with them again
                    d[temp] = []

            d[t].append(i)

        return res

###############################################################################
"""
Solution 5: brute force

O(n^2) time
O(n) extra space: for output

TLE
"""
class Solution5:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        n = len(temps)
        res = [0]*n

        for i, x in enumerate(temps):
            for j in range(i+1, n):
                if temps[j] > x:
                    res[i] = j - i
                    break

        return res

###############################################################################

if __name__ == "__main__":
    def test_random():
        import random
        from timeit import default_timer as timer
        
        sols = [Solution(), Solution2(), Solution3(), Solution4(), Solution5()]
        n = len(sols)
        res = [0] * n
        times = [0] * n

        arr = [random.randint(30, 100) for _ in range(30000)]
        #arr = [30]*10000 # a worse-case scenario

        print("="*80)
        if len(arr) < 101:
            print(f"\ntemps = {arr}")

        print()
        for i, sol in enumerate(sols):
            start = timer()
            res[i] = sol.dailyTemperatures(arr)
            times[i] = timer() - start

            print(f"time {i}: {times[i]}")

        if len(arr) < 101:
            print()
            for i in range(n):
                print(f"res {i}: {res[i]}")

    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)
        
        print(f"\n{arr}")
        
        res = sol.dailyTemperatures(arr)

        print(f"\n{res}\n")


    sol = Solution() # mono decreasing stack
    sol = Solution1b() # same, but stack stores indices only

    #sol = Solution2() # process array in reverse; strictly inc stack
    
    sol = Solution3() # process array in reverse; use "next" array
    #sol = Solution4() # use dict
    #sol = Solution5() # brute force
    
    comment = "LC ex; answer = [1, 1, 4, 2, 1, 1, 0, 0]"
    arr = [73, 74, 75, 71, 69, 72, 76, 73]
    test(arr, comment)

    #test_random()
