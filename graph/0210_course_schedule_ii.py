"""
210. Course Schedule II
Medium

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]

Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .

Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]

Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""

from typing import List
import collections

###############################################################################
"""
Solution: DFS using recursion and visited array w/ 3 states/colors.
"""
class Solution:
    def findOrder(self, n: int, prereqs: List[List[int]]) -> List[int]:
        def is_cyclic(node):
            nonlocal res

            visited[node] = 1 # 1 = GREY = visiting

            for nbr in graph[node]:
                if not visited[nbr]:
                    if is_cyclic(nbr):
                        return True
                elif visited[nbr] == 1:
                    return True

            visited[node] = 2 # 2 = BLACK = visited
            res += [node]

            return False
        
        # Note: prereqs give directions in reverse, but stack also appends to
        # results array in reverse order.  So the effects cancel out.
        graph = {i: [] for i in range(n)}
        for x, y in prereqs:
            graph[x] += [y]

        visited = [0] * n # 0 = WHITE = unvisited
        res = []

        for node in graph:
            if not visited[node]:
                if is_cyclic(node):
                    return []

        return res

###############################################################################
"""
Solution2: BFS using deque, front to end, back array instead of degree array.

Can do any combination of BFS or DFS, and front to end or end to front.

O(V+E) time: may visit every node, and for each node, look at all its nbrs.

O(V+E) extra space: "graph" adjacency list takes O(V) for keys, O(E) for
edges/values.  Deque takes O(V).
"""
class Solution2:
    def findOrder(self, n: int, prereqs: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(n)}
        back = collections.defaultdict(list)

        for x, y in prereqs: # note directions are reversed!
            graph[y] += [x]
            back[x] += [y]

        q = collections.deque([i for i in range(n) if not back[i]])
        res = []

        while q:
            node = q.popleft()
            res.append(node)

            for nbr in graph[node]:
                back[nbr].remove(node)

                if not back[nbr]:
                    q.append(nbr)

            back.pop(node) # back[node] is []

        return res if not back else []

###############################################################################

if __name__ == "__main__":
    def test(n, arr, comment):
        print("="*80)
        if comment:
            print(comment)

        res = s.findOrder(n, arr)

        print(f"\nn = {n}")
        print(f"\n{arr[:20]}")
        #print(f"\nlen(arr) = {len(arr)}")
        #if len(arr) > 20:
        #    print(" (only show at most 20 elements)")

        print(f"\nresult = {res}")


    s = Solution() # DFS recursion, visited array w/ 3 states/colors
    s = Solution2() # BFS w/ deque, front to end, back array

    comment = "LC ex1; answer = [0,1]"
    n = 2
    arr = [[1,0]]
    test(n, arr, comment)
    
    comment = "LC ex2; answer = [0,1,2,3] or [0,2,1,3]"
    n = 4
    arr = [[1,0],[2,0],[3,1],[3,2]]
    test(n, arr, comment)

    comment = "LC207 ex2; answer = []"
    n = 2
    arr = [[1,0],[0,1]]
    test(n, arr, comment)

    comment = "LC207 test case; answer = (0 before 1)"
    n = 3
    arr = [[1,0]]
    test(n, arr, comment)

    comment = "LC207 test case; answer = [0]"
    n = 1
    arr = []
    test(n, arr, comment)

    comment = "G4G example; answer = ..."
    n = 6
    arr = [[2,3],[3,1],[4,0],[4,1],[5,0],[5,2]]
    test(n, arr, comment)
