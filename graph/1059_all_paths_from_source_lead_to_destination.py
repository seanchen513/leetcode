"""
1059. All Paths from Source Lead to Destination
Medium

Given the edges of a directed graph, and two nodes source and destination of this graph, determine whether or not all paths starting from source eventually end at destination, that is:

At least one path exists from the source node to the destination node
If a path exists from the source node to a node with no outgoing edges, then that node is equal to destination.
The number of possible paths from source to destination is a finite number.
Return true if and only if all roads from source lead to destination.

Example 1:

Input: n = 3, edges = [[0,1],[0,2]], source = 0, destination = 2
Output: false
Explanation: It is possible to reach and get stuck on both node 1 and node 2.

Example 2:

Input: n = 4, edges = [[0,1],[0,3],[1,2],[2,1]], source = 0, destination = 3
Output: false
Explanation: We have two possibilities: to end at node 3, or to loop over node 1 and node 2 indefinitely.

Example 3:

Input: n = 4, edges = [[0,1],[0,2],[1,3],[2,3]], source = 0, destination = 3
Output: true

Example 4:

Input: n = 3, edges = [[0,1],[1,1],[1,2]], source = 0, destination = 2
Output: false
Explanation: All paths from the source node end at the destination node, but there are an infinite number of paths, such as 0-1-2, 0-1-1-2, 0-1-1-1-2, 0-1-1-1-1-2, and so on.

Example 5:

Input: n = 2, edges = [[0,1],[1,1]], source = 0, destination = 1
Output: false
Explanation: There is infinite self-loop at destination node.

Note:

The given graph may have self loops and parallel edges.
The number of nodes n in the graph is between 1 and 10000
The number of edges in the graph is between 0 and 10000
0 <= edges.length <= 10000
edges[i].length == 2
0 <= source <= n - 1
0 <= destination <= n - 1
"""

from typing import List

###############################################################################
"""
Solution: 
"""
class Solution:
    #def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    def leadsToDestination(self, n: int, edges: List[List[int]], src: int, dest: int) -> bool:
        def rec(x):
            if path_visited[x]: # cycle detected
                return False
            
            path_visited[x] = True
            
            if graph[x] == []:
                if x != dest: # node found that is a sink but is not the given destination
                    return False
                
                path_visited[x] = False
                return True
            
            for nbr in graph[x]:
                if not rec(nbr): # cycle detected or "bad" node found
                    return False
            
            path_visited[x] = False
            return True

        # Build adjacency list.
        graph = [[] for _ in range(n)]
        for x, y in edges:
            graph[x].append(y)
        
        # For checking if a node has been visited within a path (ie, recursion stack).
        path_visited = [False] * n
        
        # Not necessary to pass LeetCode OJ.
        if graph[dest] != []:
            return False
        
        return rec(src)
        
###############################################################################

if __name__ == "__main__":
    def test(n, edges, src, dest, comment=None):
        print("="*80)
        if comment:
            print(comment, "\n")

        print(f"n = {n}")
        print(f"edges = {edges}")
        print(f"src = {src}")
        print(f"dest = {dest}")

        res = sol.leadsToDestination(n, edges, src, dest)

        print(f"\nresult = {res}\n")


    sol = Solution()

    comment = "LC ex1; answer = False"
    n = 3
    edges = [[0,1],[0,2]]
    src = 0
    dest = 2
    test(n, edges, src, dest, comment)
    
    comment = "LC ex2; answer = False"
    n = 4
    edges = [[0,1],[0,3],[1,2],[2,1]]
    src = 0
    dest = 3
    test(n, edges, src, dest, comment)
    
    comment = "LC ex3; answer = True"
    n = 4
    edges = [[0,1],[0,2],[1,3],[2,3]]
    src = 0
    dest = 3
    test(n, edges, src, dest, comment)
    
    comment = "LC ex4; answer = False"
    n = 3
    edges = [[0,1],[1,1],[1,2]]
    src = 0
    dest = 2
    test(n, edges, src, dest, comment)
    
    comment = "LC ex5; answer = False"
    n = 2
    edges = [[0,1],[1,1]]
    src = 0
    dest = 1
    test(n, edges, src, dest, comment)
    