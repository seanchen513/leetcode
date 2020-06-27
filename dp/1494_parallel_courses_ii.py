"""
1494. Parallel Courses II
Hard

Given the integer n representing the number of courses at some university labeled from 1 to n, and the array dependencies where dependencies[i] = [xi, yi]  represents a prerequisite relationship, that is, the course xi must be taken before the course yi.  Also, you are given the integer k.

In one semester you can take at most k courses as long as you have taken all the prerequisites for the courses you are taking.

Return the minimum number of semesters to take all courses. It is guaranteed that you can take all courses in some way.

Example 1:

Input: n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2
Output: 3 
Explanation: The figure above represents the given graph. In this case we can take courses 2 and 3 in the first semester, then take course 1 in the second semester and finally take course 4 in the third semester.

Example 2:

Input: n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2
Output: 4 
Explanation: The figure above represents the given graph. In this case one optimal way to take all courses is: take courses 2 and 3 in the first semester and take course 4 in the second semester, then take course 1 in the third semester and finally take course 5 in the fourth semester.

Example 3:

Input: n = 11, dependencies = [], k = 2
Output: 6

Constraints:

    1 <= n <= 15
    1 <= k <= n
    0 <= dependencies.length <= n * (n-1) / 2
    dependencies[i].length == 2
    1 <= xi, yi <= n
    xi != yi
    All prerequisite relationships are distinct, that is, dependencies[i] != dependencies[j].
    The given graph is a directed acyclic graph.

"""

from typing import List
import collections

###############################################################################
"""
Solution: bit manipulation

n = number of bits, each representing a course
n2 - 1 = (1 << n) - 1 = mask of all 1's (n in total)

...

Based on JOHNKRAM, rank 1, Q4 (C++):
https://leetcode.com/contest/biweekly-contest-29/ranking/1/

Runtime: 2800 ms, faster than 6.67% of Python3 online submissions
Memory Usage: 14 MB, less than 40.00% of Python3 online submissions
"""
class Solution:
    #def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
    def minNumberOfSemesters(self, n: int, dep: List[List[int]], k: int) -> int:
        # pre[i] = bit rep of all prereqs/dependencies of course i
        pre = [0] * n
        for x, y in dep: # y depends on x, or x is a prereq of y
            pre[y-1] |= (1 << (x-1)) # subtract 1 to make the courses 0-based indices

        n2 = (1 << n)
        
        # Precalculate the number of set bits in index, rather than having to
        # call popcount() repeatedly.
        n_setbits = [0] * n2
        for i in range(n2):
            n_setbits[i] = n_setbits[i >> 1] + (i & 1)
        
        """
        i = bit rep of a combination of courses
        dp[i] = minimum number of semesters to complete all courses associated with i.

        Initializing with a number > n speeds this up significantly because of
        the condition "if dp[i] <= n" within the loop for i below.
        In this problem 1 <= n <= 15, so we can initialize with any number > 15.
        """
        n1 = n + 1
        dp = [n1] * n2
        #dp = [16] * n2 
        dp[0] = 0

        for i in range(n2):
            if dp[i] <= n:
                ex = 0
                for j in range(n):
                    if (not ((i >> j) & 1)) and (pre[j] & i == pre[j]):
                        ex |= (1 << j)

                # Enumerate all the submasks (bit 1 combinations) of ex.
                s = ex
                while s:
                    if n_setbits[s] <= k:
                        dp[i | s] = min(dp[i | s], dp[i] + 1)

                    s = (s - 1) & ex

        return dp[n2 - 1]

"""
Solution1b: bit manipulation

Almost same as sol 1, except:
- uses popcount() instead of precalculating it.
- doesn't use the condition "if dp[i] <= n:" within the loop for i.
- doesn't use the condition "not ((i >> j) & 1)" within the inner loop for j.
- does "ex &= ~i"

Based on Heltion, rank 6, Q4 (C++):
https://leetcode.com/contest/biweekly-contest-29/ranking/1/

See a comment for this post to see comments for Heltion's code:
https://leetcode.com/problems/parallel-courses-ii/discuss/708263/Can-anyone-explain-the-bit-mask-method

See a comment here (in Chinese):
https://leetcode-cn.com/circle/discuss/zPlu04/

Runtime: 6708 ms, faster than 6.67% of Python3 online submissions
Memory Usage: 16.3 MB, less than 6.67% of Python3 online submissions
"""
import functools
class Solution1b:
    #def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
    def minNumberOfSemesters(self, n: int, dep: List[List[int]], k: int) -> int:
        @functools.lru_cache(None)
        def popcount(x): # returns number of 1-bits in x
            count = 0
            while x:
                count += 1
                x &= (x-1)
            return count

        pre = [0] * n # pre[i] = bit rep of all prerequisites/dependencies of course i
        for x, y in dep:
            pre[y-1] |= (1 << (x-1))

        n2 = (1 << n)

        # In following, i is the bit rep of a combination of courses.
        # dp[i] = minimum number of semesters to complete all courses associated with i.

        dp = [n] * n2
        dp[0] = 0 # base case: it takes 0 semesters to complete 0 courses

        # Range of i is from 000..0 to 111..1, which is (1 << n) - 1.
        for i in range(n2):
            # "ex" is bit rep of all courses that can be taken if all the courses
            # of i are completed. We will be calculating it.
            ex = 0 # we will find bit rep of all courses that we can study NOW

            # Since we know i and pre[j], we know course j can be taken now
            # if i contains all its prereqs.
            for j in range(n):
                if i & pre[j] == pre[j]: # ie, pre[j] is a subset of i
                    ex |= (1 << j)

            ex &= ~i # remove i from "ex" to avoid duplication; ie, remove courses already taken

            # Enumerate all the submasks (bit 1 combinations) of ex.
            # This is a typical method to enumerate all subsets of a bit rep.
            # Ie, look at all possible combinations of at most k courses that we
            # can take now.
            s = ex
            while s:
                if popcount(s) <= k: # only consider combos of <= k courses
                    # i | s = courses in i completed, plus courses in s to be taken
                    dp[i | s] = min(dp[i | s], dp[i] + 1)

                s = (s - 1) & ex

        return dp[n2 - 1] # dp[-1]

"""
Solution 1c: bit manipulation

...

Based on: cuiaoxiang, rank 59, Q4 (C++):
https://leetcode.com/contest/biweekly-contest-29/ranking/3/

Runtime: 9784 ms, faster than 6.67% of Python3 online submissions
Memory Usage: 15.4 MB, less than 6.67% of Python3 online submissions

With functools.lru_cache() on popcount():
Runtime: 5032 ms, faster than 6.67% of Python3 online submissions
Memory Usage: 17.4 MB, less than 6.67% of Python3 online submissions
"""
import functools
class Solution1c:
    #def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
    def minNumberOfSemesters(self, n: int, dep: List[List[int]], k: int) -> int:
        @functools.lru_cache(None)
        def popcount(x): # returns number of 1-bits in x
            count = 0
            while x:
                count += 1
                x &= (x-1)
            return count

        pre = [0] * n
        for x, y in dep:
            pre[y-1] |= (1 << (x-1))

        n2 = (1 << n)

        valid = [False] * n2
        for i in range(n2):
            valid[i] = (popcount(i) <= k)

        ### This isn't used.
        # pre2 = [0] * n2
        # for i in range(n2):
        #     for j in range(n):
        #         if i & (1 << j):
        #             pre2[i] |= pre[j]

        dp = [1e9] * n2
        dp[0] = 0
       
        for s in range(1, n2):
            u = n2 -1 - s
            can = []
            v = 0

            for i in range(n):
                if ((u & pre[i]) == pre[i]) and (s & (1 << i)):
                    can.append(i)
                    v |= (1 << i)

            m = len(can)

            if m <= k:
                dp[s] = 1 + dp[s ^ v]
            else:
                for i in range(1 << m):
                    if popcount(i) != k:
                        continue

                    t = 0
                    for j in range(m):
                        if i & (1 << j):
                            t |= (1 << can[j])
                    
                    dp[s] = min(dp[s], 1 + dp[s ^ t])
        
        return dp[n2 - 1]

###############################################################################
""" 
NOT a solution: customized topological sorting of DAG. Each semester, greedily
take the classes that are the prereq of the most classes first.

In each iteration, we take the whole queue or the first k elements, whichever
is smaller.

At each level, we sort the queue by decreasing outdegree of each node.
Ie, each semester, we take the courses that are the prereq of the most classes
first. (greedy)

https://leetcode.com/problems/parallel-courses-ii/discuss/708081/Python3-Topological-sort-%2B-outdegree
(DELETED)

Originally passed LeetCode's online judge during and shortly after contest B29
on 6/27/20.

"""
class SolutionNOT:
    #def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
    def minNumberOfSemesters(self, n: int, dep: List[List[int]], k: int) -> int:        
        graph = collections.defaultdict(list)

        # Courses are indices 1 to n. Ignore index 0.
        in_degree = [0] * (n+1)
        out_degree = [0] * (n+1)

        for x, y in dep:
            graph[x].append(y)
            in_degree[y] += 1
            out_degree[x] += 1

        # Initialize queue with nodes that have in-degree 0.
        q = []

        for i in range(1, n+1):
            if in_degree[i] == 0:
                q.append(i)

        level = 0

        while q:
            # Sort by decreasing out-degree.
            q.sort(key=lambda i: -out_degree[i])

            sz = len(q)
            end = min(sz, k)

            for i in range(end):
                cur = q.pop(0)
                #print(f"level={level}, cur={cur}")

                for nxt in graph[cur]:
                    in_degree[nxt] -= 1

                    if in_degree[nxt] == 0:
                        q.append(nxt)

            level += 1

        return level

###############################################################################

if __name__ == "__main__":
    def test(n, dep, k, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\nn = {n}")
        print(f"dependencies = {dep}")
        print(f"k = {k}")

        res = sol.minNumberOfSemesters(n, dep, k)

        print(f"\nres = {res}\n")


    sol = Solution() # bits; based on JOHNKRAM
    #sol = Solution1b() # bits; based on Heltion

    #sol = Solution1c() # bits; based on aoxiang
    
    #sol = SolutionNOT() # greedy choose courses with higher out-degree first

    comment = "LC ex1; answer = 3"
    n = 4
    dep = [[2,1],[3,1],[1,4]]
    k = 2
    test(n, dep, k, comment)

    comment = "LC ex2; answer = 4"
    n = 5
    dep = [[2,1],[3,1],[4,1],[1,5]]
    k = 2
    test(n, dep, k, comment)

    comment = "LC ex3; answer = 6"
    n = 11
    dep = []
    k = 2
    test(n, dep, k, comment)

    comment = "LC TC; answer = 3"
    n = 8
    dep = [[1,6],[2,7],[8,7],[2,5],[3,4]]
    k = 3
    test(n, dep, k, comment)

    comment = "LC TC; answer = 4"
    n = 15
    dep = [[2,1]]
    k = 4
    test(n, dep, k, comment)

    comment = "LC TC; answer = 2"
    n = 15
    dep = [[8,9],[11,1],[2,9]]
    k = 14
    test(n, dep, k, comment)

    """
    Courses 5, 4, 3, 2 have out-degrees 1.

    5 -> 3 -> 1
         ^    ^
         4    2

    Take 4 and 5 first.
    Then 2 and 3.
    Then 1.
    """
    comment = "; answer = 3" # NOT sol gives 4
    n = 5
    dep = [[5,3],[4,3],[2,1],[3,1]]
    k = 2
    test(n, dep, k, comment)

    comment = "; answer = 3" # NOT sol gives 4
    n = 5
    dep = [[1,2],[3,5],[4,5],[5,2]]
    k = 2
    test(n, dep, k, comment)

    """
    2 components
    component 1 has starting nodes with higher outdegree (2).
    component 2 has starting node with smaller outdegree (1) but is a long chain.

    1 -> (3, 4)
    2 -> (3, 4)

    5 -> 6 -> 7 -> 8

    Shows that greedily taking courses with higher out-degree does NOT work.
    """
    comment = "; answer = 4" # NOT sol gives 5
    n = 8
    dep = [[1,3],[1,4],[2,3],[2,4],[5,6],[6,7],[7,8]]
    k = 2
    test(n, dep, k, comment)

    """
    """
    comment = "; answer = 5" # NOT sol gives 5
    n = 9
    dep = [[1,4],[1,5],[2,5],[2,6],[3,6],[3,7],[8,4],[8,5],[9,6],[9,7]]
    k = 2
    test(n, dep, k, comment)

    """
    """
    comment = "; answer = 3" # NOT sol gives 4
    n = 9
    dep = [[1,4],[1,5],[3,5],[3,6],[2,6],[2,7],[8,4],[8,5],[9,6],[9,7]]
    k = 3
    test(n, dep, k, comment)

    """
    """
    comment = "; answer = 6" # NOT sol gives 7
    n = 12
    dep = [[1,2],[1,3],[4,5],[4,6],[7,8],[8,9],[9,10],[10,11],[11,12]]
    k = 2
    test(n, dep, k, comment)

    """
    """
    comment = "; answer = 5" # NOT sol gives 6
    n = 10
    dep = [[1,5],[1,6],[1,7],[2,5],[2,6],[2,7],[9,10],[10,5],[10,6],[10,7],[10,8],[3,5],[3,6],[4,5],[4,6]]
    k = 2
    test(n, dep, k, comment)

    """
    """
    comment = "; answer = 3" # NOT sol gives 3
    n = 6
    dep = [[2,5],[1,5],[3,5],[3,4],[3,6]]
    k = 2
    test(n, dep, k, comment)
