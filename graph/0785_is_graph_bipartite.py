"""
785. Is Graph Bipartite?
Medium

Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation: 
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.

Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation: 
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.
 
Note:
graph will have length in range [1, 100].
graph[i] will contain integers in range [0, graph.length - 1].
graph[i] will not contain i or duplicate values.
The graph is undirected: if any element j is in graph[i], then i will be in graph[j].
"""

from typing import List
import collections


###############################################################################
"""
Solution 2: DFS.

O(n) time
O(n) extra space for "colors" array.

Faster than BFS, at least on LC. (164ms vs 340ms)
"""
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = {} # also used to check if a node has been visited

        # Wrap the DFS in this loop to deal with multiple components.
        for node in range(n):
            if node in colors:
                continue

            stack = [node]
            colors[node] = 0 # start with color 0 and alternate between 0 and 1

            while stack:
                curr = stack.pop()

                for nbr in graph[curr]:
                    if nbr not in colors:
                        colors[nbr] = colors[curr] ^ 1
                        stack.append(nbr)
                    elif colors[nbr] == colors[curr]:
                        return False

        return True

###############################################################################
"""
Solution: BFS.

O(n) time
O(n) extra space for "colors" array.
"""
class Solution2:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = {}  # also used to check if a node has been visited
        color = 0 # start with color 0 and alternate between 0 and 1
 
        # Wrap the BFS in this loop to deal with multiple components.
        for node in range(n):
            if node in colors:
                continue

            level = [node]

            while level:
                next_level = []

                for curr in level:
                    colors[curr] = color

                    for nbr in graph[curr]:
                        if nbr not in colors:
                            next_level.append(nbr)
                        elif colors[nbr] == color:
                            return False

                color ^= 1 # alternate between 0 and 1
                level = next_level

        return True

###############################################################################
"""
Same as sol #2, but using a deque instead of two lists.
"""
class Solution2b:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = {}
        color = 0 # start with color 0 and alternate between 0 and 1

        q = collections.deque([])

        # Wrap the BFS in this loop to deal with multiple components.
        for node in range(n):
            if node in colors:
                continue

            q.clear()
            q.append(node)

            while q:
                for _ in range(len(q)):
                    curr = q.popleft()
                    colors[curr] = color

                    for nbr in graph[curr]:
                        if nbr not in colors:
                            q.append(nbr)
                        elif colors[nbr] == color:
                            return False

                color ^= 1 # alternate between 0 and 1

        return True

###############################################################################

if __name__ == "__main__":
    def test(graph, comment):
        print("="*80)
        if comment:
            print(comment)
        print()
        print(graph)

        res = s.isBipartite(graph)
        
        print(f"\nresult = {res}")


    s = Solution() # DFS
    #s = Solution2() # BFS with 2 lists
    #s = Solution2b() # BFS with deque
    
    comment = "LC ex1; answer = True"
    graph = [[1,3], [0,2], [1,3], [0,2]]
    test(graph, comment)

    comment = "LC ex2; answer = False"
    graph = [[1,2,3], [0,2], [0,1,3], [0,2]]
    test(graph, comment)

    comment = "LC test case; answer = False"
    graph = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
    test(graph, comment)
