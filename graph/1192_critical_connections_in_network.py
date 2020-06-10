"""
1192. Critical Connections in a Network
Hard

There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

Example 1:

Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]

Explanation: [[3,1]] is also accepted.

Constraints:

1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.
"""

from typing import List
import collections

###############################################################################
"""
Solution: find bridges in the graph.

Critical connections in the network are the bridges in the graph.

O(V+E) time
O(V) extra space

Runtime: 2388 ms, faster than 67.32% of Python3 online submissions
Memory Usage: 83.6 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def rec(x):
            nonlocal time
            disc[x] = time
            low[x] = time
            time += 1
            
            for nbr in graph[x]:
                if disc[nbr] == -1: # not visited yet
                    parent[nbr] = x
                    rec(nbr)
                    
                    low[x] = min(low[x], low[nbr])
                    
                    if low[nbr] > disc[x]: # [x, nbr] is bridge
                    #if low[nbr] == disc[nbr]:
                        res.append([x, nbr])
                
                elif nbr != parent[x]:
                    low[x] = min(low[x], disc[nbr])

        # undirected graph is acyclic is E < V
        if len(connections) < n:
            return []

        # Build adjacency list for *directed* graph from the input list of edges.
        graph = collections.defaultdict(list)
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)
            
        # input n = number of nodes in graph

        # Incremented by 1 each time we visit a node for the first time in DFS.
        # Ranges from 0 to n-1.
        time = 0 

        # disc[x] = time/order when node x first visited.
        # Also used to check if node has been visited.
        # Remains constant once set.
        disc = [-1] * n 
        
        # low[x] = time/order of earliest visited vertex reachable from 
        # subtree rooted at x (ie, oldest ancestor).
        # May be updated throughout DFS.
        # Used to find back edges to ancestors.        
        low = [n] * n # can also initialize all values with float('inf')

        # parent[x] = previous node in DFS when x is first visited
        parent = [-1] * n

        res = [] # the critical connections in the network (bridges in the graph)
        
        # Since this is a connected graph, we don't have to loop over all nodes.
        rec(0)
                
        return res

"""
Solution 1b: same, but instead of using parent array, pass parent node as 
a parameter to the recursive function.
"""
class Solution1b:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def rec(x, parent):
            nonlocal time
            disc[x] = time
            low[x] = time
            time += 1
            
            for nbr in graph[x]:
                if disc[nbr] == -1: # not visited yet
                    rec(nbr, x)
                    
                    low[x] = min(low[x], low[nbr])

                    if low[nbr] > disc[x]: # [x, nbr] is bridge
                    #if low[nbr] == disc[nbr]:
                        res.append([x, nbr])
                
                elif nbr != parent:
                    low[x] = min(low[x], disc[nbr])

        # undirected graph is acyclic is E < V
        if len(connections) < n:
            return []

        graph = collections.defaultdict(list)
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)

        time = 0 
        disc = [-1] * n 
        low = [n] * n # can also initialize all values with float('inf')

        res = [] # the critical connections in the network (bridges in the graph)

        # Since this is a connected graph, we don't have to loop over all nodes.
        rec(0, -1)
                
        return res

###############################################################################
"""
Solution 2:

https://leetcode.com/problems/critical-connections-in-a-network/discuss/382638/No-TarjanDFS-detailed-explanation-O(orEor)-solution-(I-like-this-question)

"""
class Solution2():
    def criticalConnections(self, n, connections):
        def dfs(node, depth):
            if rank[node] >= 0:
                # visiting (0 <= rank < n), or visited (rank = n)
                return rank[node]

            rank[node] = depth
            min_back_depth = n

            for nbr in graph[node]:
                if rank[nbr] == depth - 1:
                    # Don't immmediately go back to parent.
                    # That's why we didn't choose -1 as the special value, in case depth==0.
                    continue 
                
                back_depth = dfs(nbr, depth + 1)
                
                if back_depth <= depth:
                    #connections.discard(tuple(sorted((node, nbr))))
                    if node <= nbr:
                        connections.remove((node, nbr))
                    else:
                        connections.remove((nbr, node))
                
                min_back_depth = min(min_back_depth, back_depth)
            
            rank[node] = n  # not necessary
            
            return min_back_depth

        graph = collections.defaultdict(list)
        # for x, y in connections:
        #     graph[x].append(y)
        #     graph[y].append(x)

        for i in range(len(connections)):
            x, y = connections[i]
            graph[x].append(y)
            graph[y].append(x)
            if x > y:
                connections[i] = (y, x)
            else:
                connections[i] = (x, y)
            
        connections = set(connections)
        #connections = set(map(tuple, (map(sorted, connections))))

        rank = [-2] * n

        # Since this is a connected graph, we don't have to loop over all nodes.
        dfs(0, 0)

        return list(connections)

###############################################################################
"""
Solution 3:

https://leetcode.com/problems/critical-connections-in-a-network/discuss/410345/Python-(98-Time-100-Memory)-clean-solution-with-explanaions-for-confused-people-like-me

Differences
- Uses rank parametr instead of nonlocal time
- parent is a parameter instead of an array
- Doesn't use disc array. Instead, combines these two equations into the former:
low[x] = min(low[x], low[nbr])
low[x] = min(low[x], disc[nbr])

This is considered bad, but works.

"""
class Solution3:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def dfs(rank, curr, parent):
            low[curr] = rank
            res = []

            for nbr in graph[curr]:
                if nbr == parent: 
                    continue
                
                if low[nbr] == -1: # nbr not yet visited
                    res += dfs(rank + 1, nbr, curr)
                
                low[curr] = min(low[curr], low[nbr])
                
                if low[nbr] >= rank + 1: # bridge found
                    res.append([curr, nbr])
            
            return res

        graph = collections.defaultdict(list)
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)

        low = [-1] * n # using values of 0 also works

        return dfs(1, 0, -1)

###############################################################################

if __name__ == "__main__":
    def test(n, arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\nn = {n}")
        print(f"\nconnections = {arr}")

        res = sol.criticalConnections(n, arr)

        print(f"\nres = {res}\n")


    sol = Solution()
    #sol = Solution1b() # same, but pass parent as parameter to recursive fn

    #sol = Solution2()
    #sol = Solution3()

    comment = "LC example; answer = [[1,3]]"
    n = 4
    edges = [[0,1],[1,2],[2,0],[1,3]]
    test(n, edges, comment)

    comment = "g4g example; answer = []"
    n = 10
    edges = [[0,1],[1,2],[2,0],[2,3],[3,0], 
        [2,4],[4,5],[5,6],[6,2],[6,4], 
        [5,7],[7,8],[8,5],[8,9],[9,5]]
    test(n, edges, comment)
