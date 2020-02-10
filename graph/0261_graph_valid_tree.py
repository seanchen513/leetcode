"""
261. Graph Valid Tree
Medium

Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true

Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.
"""

from typing import List

###############################################################################
"""
Solution 1: DFS recursion.
"""
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def is_cyclic(node, parent=-1):
            visited[node] = 1

            for nbr in graph[node]:
                if not visited[nbr]:
                    if is_cyclic(nbr, node):
                        return True
                #elif visited[nbr] == 1:
                elif nbr != parent:
                    return True

            return False

        graph = {i: [] for i in range(n)}
        for x, y in edges:
            graph[x] += [y]
            graph[y] += [x]

        visited = [0] * n

        # Undirected graph is acyclic if E < V, but we need to check if we
        # can visit all the nodes anyway...
        if is_cyclic(0):
            return False

        # Check that graph is connected by checking that all nodes were
        # visited from calling is_cyclic() from a single starting node.
        return all(visited[i] for i in range(n))

###############################################################################
"""
Solution 2: Check for cycles using E >= V first.  Then check if all nodes
can be visited from a single node.
"""
class Solution2:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def visit(node):
            visited[node] = 1

            for nbr in graph[node]:
                if not visited[nbr]:
                    visit(nbr)

        if len(edges) >= n:
            return False

        graph = {i: [] for i in range(n)}
        for x, y in edges:
            graph[x] += [y]
            graph[y] += [x]

        visited = [0] * n
        visit(0)

        # Check that graph is connected by checking that all nodes were
        # visited from calling is_cyclic() from a single starting node.
        return all(visited[i] for i in range(n))

###############################################################################

if __name__ == "__main__":
    def test(n, arr, comment):
        print("="*80)
        if comment:
            print(comment)

        res = s.validTree(n, arr)

        print(f"\nn = {n}")
        print(f"\n{arr}")

        print(f"\nresult = {res}")


    #s = Solution()
    s = Solution2()

    comment = "LC ex1; answer = True"
    n = 5
    edges = [[0,1], [0,2], [0,3], [1,4]]
    test(n, edges, comment)

    comment = "LC ex2; answer = False"
    n = 5
    edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
    test(n, edges, comment)

    comment = "LC hint; answer = False"
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    test(n, edges, comment)

    comment = "LC test case; answer = True"
    n = 2
    edges = [[1, 0]]
    test(n, edges, comment)

    comment = "LC test case; answer = True"
    n = 4
    edges = [[0,1],[2,3],[1,2]]
    test(n, edges, comment)
