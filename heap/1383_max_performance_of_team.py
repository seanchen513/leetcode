"""
1383. Maximum Performance of a Team
Hard

There are n engineers numbered from 1 to n and two arrays: speed and efficiency, where speed[i] and efficiency[i] represent the speed and efficiency for the i-th engineer respectively. Return the maximum performance of a team composed of at most k engineers, since the answer can be a huge number, return this modulo 10^9 + 7.

The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers. 

Example 1:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
Output: 60
Explanation: 
We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.

Example 2:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
Output: 68
Explanation:
This is the same example as the first but k = 3. We can select engineer 1, engineer 2 and engineer 5 to get the maximum performance of the team. That is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.

Example 3:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
Output: 72
 
Constraints:
1 <= n <= 10^5
speed.length == n
efficiency.length == n
1 <= speed[i] <= 10^5
1 <= efficiency[i] <= 10^8
1 <= k <= n
"""

from typing import List
import itertools
import heapq

###############################################################################
"""
Solution: first, reverse sort engineers by efficiency.  Iterate through
engineers by decreasing efficiency, and use min heap to track the top k 
fastest engineers by speed.

O(n log n) time: due to sorting
O(k) extra space

Runtime: 416 ms, faster than 77.78% of Python3 online submissions
Memory Usage: 28.9 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        h = [] # min heap of size k
        res = 0
        sum_speed =  0
        
        for eff, sp in sorted(zip(efficiency, speed), reverse=True):
            heapq.heappush(h, sp)
            sum_speed += sp
            
            if len(h) > k: # keep only top k speeds seen so far
                sum_speed -= heapq.heappop(h)
                
            res = max(res, sum_speed * eff)
            
        return res % (10**9 + 7)

###############################################################################
"""
Solution 2: brute force using itertools.combinations().

TLE
"""

class Solution2:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mx = 0

        for i in range(1, k+1):
            for p in itertools.combinations(range(n), i):
                perf = sum(speed[j] for j in p) * min(efficiency[j] for j in p)
                mx = max(mx, perf)

        return mx % (10**9 + 7)

"""
Solution 2b: same as sol 2, but use zip(speed, efficiency)

TLE
"""
class Solution2b:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        eng = list(zip(speed, efficiency))
        mx = 0
        
        for i in range(1, k+1):
            for p in itertools.combinations(eng, i):  
                unzipped = list(zip(*p))
                perf = sum(unzipped[0]) * min(unzipped[1])
                mx = max(mx, perf)

        return mx % (10**9 + 7)

###############################################################################

if __name__ == "__main__":
    def test(n, speed, eff, k, comment=None):
        print("="*80)
        if comment:
            print(comment)
        
        print()
        
        print(f"n = {n}")
        print(f"speed = {speed}")
        print(f"eff = {eff}")
        print(f"k = {k}")

        res = sol.maxPerformance(n, speed, eff, k)

        print(f"\nres = {res}\n")


    sol = Solution() # reverse sort by (eff, speed); use heap

    #sol = Solution2() # brute force using itertools.combinations()
    #sol = Solution2b() # same as sol 2, but use zip(speed, efficiency)

    comment = "LC ex1; answer = 60"
    n = 6
    speed = [2,10,3,1,5,8]
    eff = [5,4,3,9,7,2]
    k = 2
    """
    k=1: 40
    k=2: 60
    k=3: 68
    k=4: 72
    k=5: 72
    k=6: 72
    """
    test(n, speed, eff, k, comment)

    comment = "LC ex2; answer = 68"
    k = 3
    test(n, speed, eff, k, comment)

    comment = "LC ex3; answer = 72"
    k = 4
    test(n, speed, eff, k, comment)

    comment = "LC test case; answer = 84"
    n = 4
    speed = [8,9,5,9]
    eff = [1,2,6,9]
    k = 2
    test(n, speed, eff, k, comment)

    comment = "LC test case; answer = 32"
    n = 6
    speed = [10,5,1,7,4,2]
    eff = [2,1,1,1,7,3]
    k = 6
    test(n, speed, eff, k, comment)
    """
    k=1: 28
    k=2: 28
    k=3: 32
    k=4: 32
    k=5: 32
    k=6: 32
    """
