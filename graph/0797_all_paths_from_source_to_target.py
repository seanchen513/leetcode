"""
797. All Paths From Source to Target
Medium

Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

Example:
Input: [[1,2], [3], [3], []] 
Output: [[0,1,3],[0,2,3]] 

Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Note:

The number of nodes in the graph will be in the range [2, 15].
You can print different paths in any order, but you should keep the order of nodes inside one path.
"""

from typing import List

###############################################################################
"""
Solution: 
"""
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def rec(x=0, path=[0]):
            if x == n-1:
                res.append(path[:])
                return
                
            for nbr in graph[x]:
                path.append(nbr)
                rec(nbr, path)
                path.pop() # backtrack
        
        n = len(graph)        
        res = []
        
        rec()
        
        return res

###############################################################################

if __name__ == "__main__":
    def test(graph, comment=None):
        print("="*80)
        if comment:
            print(comment, "\n")

        print(f"graph = {graph}")

        res = sol.allPathsSourceTarget(graph)

        print(f"\nresult = {res}\n")


    sol = Solution()

    comment = "LC ex1; answer = [[0,1,3],[0,2,3]]"
    graph = [[1,2], [3], [3], []]
    test(graph, comment)
    