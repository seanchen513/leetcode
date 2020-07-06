"""
1136. Parallel Courses
Hard

There are N courses, labelled from 1 to N.

We are given relations[i] = [X, Y], representing a prerequisite relationship between course X and course Y: course X has to be studied before course Y.

In one semester you can study any number of courses as long as you have studied all the prerequisites for the course you are studying.

Return the minimum number of semesters needed to study all courses.  If there is no way to study all the courses, return -1.

Example 1:

Input: N = 3, relations = [[1,3],[2,3]]
Output: 2
Explanation: 
In the first semester, courses 1 and 2 are studied. In the second semester, course 3 is studied.

Example 2:

Input: N = 3, relations = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: 
No course can be studied because they depend on each other.

Note:

1 <= N <= 5000
1 <= relations.length <= 5000
relations[i][0] != relations[i][1]
There are no repeated relations in the input.
"""

from typing import List
import collections

###############################################################################
"""
Solution: Kahn's algo for topological sorting. Instead of storing the nodes
in topological order, we count how many levels are in the sorting.

The attempted topological sort fails if the directed graph contains a cycle.
We check this by either:
(1) keeping a count of nodes visited and checking if it's == n, OR
(2) at the end, checking if any nodes still have in-degree > 0.

O(V+E) time
O(V) extra space: for the queue

"""
class Solution:
    #def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
    def minimumSemesters(self, n: int, dep: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        indegree = [0] * (n+1) # nodes are indices 1 to n; ignore index 0

        for x, y in dep:
            graph[x].append(y)
            indegree[y] += 1

        # Initialize a queue with the nodes having in-degree 0 (roots).
        q = collections.deque([i for i in range(1, n+1) if indegree[i] == 0])
        # q = collections.deque([])
        # for i in range(1, n+1):
        #     if indegree[i] == 0:
        #         q.append(i)

        levels = 0 # number of semesters, or levels in the topological sort
        count = 0

        while q:
            sz = len(q)

            for _ in range(sz): # for all nodes in the current level
                cur = q.popleft()
                count += 1

                for nbr in graph[cur]:
                    indegree[nbr] -= 1

                    if indegree[nbr] == 0:
                        q.append(nbr)

            levels += 1

        # for in_deg in indegree:
        #     if in_deg:
        #         return -1

        if count != n:
            return -1

        return levels

###############################################################################

if __name__ == "__main__":
    def test(n, dep, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\nn = {n}")
        print(f"dependencies = {dep}")

        res = sol.minimumSemesters(n, dep)

        print(f"\nres = {res}\n")


    sol = Solution()
    
    comment = "LC ex1; answer = 2"
    n = 3
    dep = [[1,3],[2,3]]
    test(n, dep, comment)

    comment = "LC ex2; answer = -1"
    n = 3
    dep = [[1,2],[2,3],[3,1]]
    test(n, dep, comment)

    comment = "; answer = 3" # LC1494 ex1
    n = 4
    dep = [[2,1],[3,1],[1,4]]
    test(n, dep, comment)

    comment = "; answer = 3" # LC1494 ex2
    n = 5
    dep = [[2,1],[3,1],[4,1],[1,5]]
    test(n, dep, comment)

    comment = "; answer = 1" # LC1494 ex3
    n = 11
    dep = []
    test(n, dep, comment)

    comment = "; answer = 2" # LC1494 TC
    n = 8
    dep = [[1,6],[2,7],[8,7],[2,5],[3,4]]
    test(n, dep, comment)
