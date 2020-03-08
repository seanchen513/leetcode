"""
1377. Frog Position After T Seconds
Hard

Given an undirected tree consisting of n vertices numbered from 1 to n. A frog starts jumping from the vertex 1. In one second, the frog jumps from its current vertex to another unvisited vertex if they are directly connected. The frog can not jump back to a visited vertex. In case the frog can jump to several vertices it jumps randomly to one of them with the same probability, otherwise, when the frog can not jump to any unvisited vertex it jumps forever on the same vertex. 

The edges of the undirected tree are given in the array edges, where edges[i] = [fromi, toi] means that exists an edge connecting directly the vertices fromi and toi.

Return the probability that after t seconds the frog is on the vertex target.

Example 1:

Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4
Output: 0.16666666666666666 
Explanation: The figure above shows the given graph. The frog starts at vertex 1, jumping with 1/3 probability to the vertex 2 after second 1 and then jumping with 1/2 probability to vertex 4 after second 2. Thus the probability for the frog is on the vertex 4 after 2 seconds is 1/3 * 1/2 = 1/6 = 0.16666666666666666. 

Example 2:

Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7
Output: 0.3333333333333333
Explanation: The figure above shows the given graph. The frog starts at vertex 1, jumping with 1/3 = 0.3333333333333333 probability to the vertex 7 after second 1. 

Example 3:

Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 20, target = 6
Output: 0.16666666666666666

Constraints:

1 <= n <= 100
edges.length == n-1
edges[i].length == 2
1 <= edges[i][0], edges[i][1] <= n
1 <= t <= 50
1 <= target <= n
Answers within 10^-5 of the actual value will be accepted as correct.
"""

from typing import List
import collections

###############################################################################
"""
Solution: tree-based approach.  Make 1 the root of the tree, count children for
each node, and trace parents from target to root.

Trace from the target to the root (node 1). 
Check that the given time t is compatible with how many times we traced up the
tree using the parents dict; if they're not compatible, return 0. 
Start with probability 1. At each step, divide the probability by the number
of children the parent has.

Notes:
1. Node 1 might not be the root of the tree, but you can make it the root by
re-ordering each edge: if (x, y) is a given edge with x > y, reverse it to (y, x).
2. We don't actually need to build adjacency lists of children, just a dict to
count how many children each node has.

Let E = number of edges, and V = number of nodes/vertices.  Note that every 
node except the root has an edge going to its parent, so E = V - 1.

O(E) time: due to looping over edges to build dict "d" and "parent".
O(V) extra space: both dict "d" and "parent" are indexed by nodes.

https://leetcode.com/problems/frog-position-after-t-seconds/discuss/532563/Python3-Tree-based-Approach
"""
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        d = collections.defaultdict(int) # counts how many children each node has
        parent = {} # maps nodes to their parents
        
        for x, y in edges:
            if x > y:
                x, y = y, x
                
            d[x] += 1
            parent[y] = x
        
        prob = 1.0
        target_is_leaf = (d[target] == 0)
        
        # Traverse tree from target to root (node 1)
        while target != 1:
            t -= 1
            prob /= d[parent[target]] # divide prob by how many children the parent has
            target = parent[target]
            
        if target_is_leaf: # the frog keeps jumping on the target
            if t < 0:
                return 0
        elif t != 0: # and target is not leaf; there's only one moment when frog is on target
            return 0
        
        return prob

###############################################################################

if __name__ == "__main__":
    def test(n, edges, t, target, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(f"n = {n}")
        print(edges)
        print(f"t = {t}")
        print(f"target = {target}")

        res = sol.frogPosition(n, edges, t, target)

        print(f"\nres = {res}\n")


    sol = Solution()

    comment = "LC ex1; answer ~ 0.16666666"
    n = 7
    edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
    t = 2
    target = 4
    test(n, edges, t, target, comment)

    comment = "LC ex2; answer ~ 0.33333333"
    n = 7
    edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
    t = 1
    target = 7
    test(n, edges, t, target, comment)

    comment = "LC ex3; answer ~ 0.16666666"
    n = 7
    edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
    t = 20
    target= 6
    test(n, edges, t, target, comment)

    comment = "LC test case; answer = 1"
    n = 3
    edges = [[2,1],[3,2]]
    t = 1
    target = 2
    test(n, edges, t, target, comment)
